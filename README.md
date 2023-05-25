# CME dat parser


convert YAML to Json

install remarshal

    sudo snap install remarshal
    yaml2json map.yaml > map.json


run with python3

./parse.py

output

```
mreider@mrxmini ~/d/secdef> ./parse.py
total lines processed: 677857

> total # of instruments (167) = 5 -> {'MLEG', 'FXSPOT', 'IRS', 'OOF', 'FUT'}

> product 5 (Equity) has 2384 Futures instruments
> product 16 (Energy) has 115639 Futures instruments
> product 2 (Commodity/Agriculture) has 12815 Futures instruments
> product 14 (Interest Rate) has 4989 Futures instruments
> product 12 (Other) has 1391 Futures instruments
> product 17 (Metals) has 9864 Futures instruments
> product 4 (Currency) has 1148 Futures instruments

top 4 earliest expirations:

total parse time: 9.614769841078669

```