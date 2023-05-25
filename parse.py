#!/usr/bin/env python3
import sys
import timeit
import json
import re

SOH="\x01"

def parse():
    """ parse secdef.dat and extract required info """

    output = dict()
    output["instruments"] = set()
    output["products"] = dict()
    output["expirations"] = dict()

    start_time = timeit.default_timer()

    # import Tag map file
    with open("map.json") as jsonfile:
        tagmap = json.load(jsonfile)

    count = 0

    with open("secdef.dat") as file:
        for row in file:

            # remove any line breaks from row
            row = row.replace("\n", "")

            # get Instrument value
            instrument = re.findall(f"167=[A-Z]*{SOH}", row)[0].split("=")[1].replace(SOH, "")

            # convert each row in .dat into list element
            rowlist = row.split(SOH)

            # remove empty tags and empty elements
            rowlist = [x for x in rowlist if x]

            # decode each list element
            for tag in rowlist:
                try:
                    taglist = tag.split("=")
                    key = int(taglist[0])
                    val = taglist[1]

                    # question 1 - get SecurityType and append to instruments set
                    if key == 167:
                        output["instruments"].add(val)

                    # question 2 - add Product to dict as set
                    if key == 462:
                        if not val in output["products"]:
                            output["products"][val] = {instrument}
                        else:
                            output["products"][val].add(instrument)

                    # question 3 - add to expirations dict as list
                    if key == 6937 and val == "GE":
                        try:
                            legs = re.findall(f"{SOH}555=[0-9]*{SOH}", row)[0].split("=")[1].replace(SOH, "")
                            expiration = re.findall(f"{SOH}200=[0-9]*{SOH}", row)[0].split("=")[1].replace(SOH, "")
                            name = re.findall(f"{SOH}55=.*{SOH}", row)[0].split("=")[1].replace(SOH, "")
                            if not expiration in output["expirations"]:
                                output["expirations"][expiration] = [f"{legs}, {name}"]
                            else:
                                output["expirations"][expiration].append(f"{legs}, {name}")

                        except IndexError:
                            pass

                except (KeyError, ValueError, IndexError, TypeError, AttributeError) as error:
                    print(f"error on tag {tag} - {error}")
                    sys.exit(1)

            count = count + 1

    print(f"total lines processed: {count}\n")

    print(f"> total # of instruments (167) = {len(output['instruments'])} -> {output['instruments']}\n")

    # question 2 - display all products and all instruments in each product
    for k, v in output["products"].items():
        try:
            product_name = tagmap["tags"]["462"]["val"][str(k)]
        except (KeyError, ValueError) as error:
            print(str(error))
            sys.exit(1)

        print(f"> product {k} ({product_name}) has {len(v)} instruments -> {v}")


    # question 3
    print("\ntop 4 earliest expirations:")

    # sort expiration dict by date, get 4 earliest
    exp_list = sorted(output["expirations"], key=output["expirations"].get, reverse=True)[:4]

    for exp in exp_list:
        print(f"\n{exp}:")

        # remove duplicates
        current_exp = list(set(output["expirations"][exp]))
        for data in current_exp:
            legs = data.split(",")[0]
            name = data.split(",")[1].strip()
            print(f"name: {name}  (legs: {legs})")


    print(f"\ntotal parse time: {timeit.default_timer() - start_time}")


if __name__ == "__main__":
    parse()