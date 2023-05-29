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
            try:
                instrument = re.search(f"{SOH}167=(.*?){SOH}", row).group(1)
            except (IndexError, AttributeError):
                continue

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

                    # question 2 - add Product to dict as list
                    if key == 462:
                        if not val in output["products"]:
                            output["products"][val] = [instrument]
                        else:
                            output["products"][val].append(instrument)

                    # question 3 - add to expirations dict as list
                    if key == 6937 and val == "GE" and instrument == "FUT":
                        try:
                            legs = re.search(f"{SOH}555=(\d+){SOH}", row).group(1)
                        except (IndexError, AttributeError):
                            legs = None

                        if not legs:
                            try:
                                expiration = re.search(f"{SOH}200=(\d+){SOH}", row).group(1)
                                name = re.search(f"{SOH}55=(.*?){SOH}", row).group(1)
                            except (IndexError, AttributeError):
                                continue

                            # create dict Expiration key if doesnt exist
                            if not expiration in output["expirations"]:
                                output["expirations"][expiration] = []
                                output["expirations"][expiration].append(name)
                            else:
                                output["expirations"][expiration].append(name)

                except (KeyError, ValueError, IndexError, TypeError, AttributeError) as error:
                    print(f"error on tag {tag} - {error}")
                    sys.exit(1)

            count = count + 1

    print(f"total lines processed: {count}\n")

    print("How many instruments of each security type (tag 167) exist?\n")
    print(f"> total # of instruments (167) = {len(output['instruments'])} -> {output['instruments']}\n")


    print("\nHow many futures (tag 167) instruments exist in each product complex (tag 462)?\n")
    for k, v in output["products"].items():
        try:
            product_name = tagmap["tags"]["462"]["val"][str(k)]
            futures_list = [x for x in v if x == "FUT"]
        except (KeyError, ValueError) as error:
            print(str(error))
            sys.exit(1)

        print(f"> product {k} ({product_name}) has {len(futures_list)} Futures instruments")

    # sort expiration dict by date, get 4 earliest, deduplicate
    exp_list = list(set(sorted(output["expirations"], key=output["expirations"].get, reverse=True)[:4]))

    print("\nWhat are the names (tag 55) of the earliest four expirations (tag 200) for the futures (tag 167) instruments with asset (tag 6937) 'GE' and have zero legs (tag 555)?\n")
    for exp in output["expirations"]:
        for exp in exp_list:
            print(f"> name: {output['expirations'][exp]} - expiration: {exp}")

    print(f"\ntotal parse time: {timeit.default_timer() - start_time}")


if __name__ == "__main__":
    parse()