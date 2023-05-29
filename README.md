# CME dat parser


convert YAML to Json

install remarshal

    sudo snap install remarshal
    yaml2json map.yaml > map.json


run with python3

./parse.py

output

```
mreider@mrxmini ~/d/secdef (master)> ./parse.py
total lines processed: 677857

How many instruments of each security type (tag 167) exist?

> total # of instruments (167) = 5 -> {'FUT', 'MLEG', 'FXSPOT', 'IRS', 'OOF'}


How many futures (tag 167) instruments exist in each product complex (tag 462)?

> product 5 (Equity) has 2384 Futures instruments
> product 16 (Energy) has 115639 Futures instruments
> product 2 (Commodity/Agriculture) has 12815 Futures instruments
> product 14 (Interest Rate) has 4989 Futures instruments
> product 12 (Other) has 1391 Futures instruments
> product 17 (Metals) has 9864 Futures instruments
> product 4 (Currency) has 1148 Futures instruments

What are the names (tag 55) of the earliest four expirations (tag 200) for the futures (tag 167) instruments with asset (tag 6937) 'GE' and have zero legs (tag 555)?

> name: ['GEM3'] - expiration: 202306

total parse time: 9.28242016211152


```