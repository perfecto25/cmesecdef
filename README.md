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

> total # of instruments (167) = 5 -> {'FUT', 'IRS', 'OOF', 'MLEG', 'FXSPOT'}

> product 5 (Equity) has 2 instruments -> {'FUT', 'OOF'}
> product 16 (Energy) has 2 instruments -> {'FUT', 'OOF'}
> product 2 (Commodity/Agriculture) has 2 instruments -> {'FUT', 'OOF'}
> product 14 (Interest Rate) has 3 instruments -> {'IRS', 'FUT', 'OOF'}
> product 12 (Other) has 2 instruments -> {'FUT', 'OOF'}
> product 17 (Metals) has 2 instruments -> {'FUT', 'OOF'}
> product 4 (Currency) has 3 instruments -> {'FUT', 'OOF', 'FXSPOT'}

top 4 earliest expirations:

202306:
name: UD:U$: VT 281258948  (legs: 2)
name: UD:U$: GN 285557448  (legs: 4)
name: UD:U$: BO 285202048  (legs: 3)
name: UD:U$: BO 281101348  (legs: 3)
name: UD:U$: 12 283348048  (legs: 2)
name: UD:U$: BO 281100948  (legs: 3)
name: UD:U$: VT 285556748  (legs: 2)
name: UD:U$: VT 281259548  (legs: 2)
name: UD:U$: GN 281279348  (legs: 3)
name: UD:U$: 23 281703548  (legs: 2)
name: UD:U$: VT 280899748  (legs: 2)
name: UD:U$: VT 032782768548  (legs: 2)
name: UD:U$: VT 031588304948  (legs: 2)
name: UD:U$: VT 284631648  (legs: 2)
name: UD:U$: VT 281124248  (legs: 2)
name: UD:U$: CO 280157448  (legs: 4)
name: UD:U$:CGN 282904048  (legs: 2)
name: UD:U$: ST 280797848  (legs: 2)
name: UD:U$: VT 283913848  (legs: 2)
name: UD:U$: VT 280983148  (legs: 2)
name: UD:U$: VT 281258148  (legs: 2)
name: UD:U$: GN 283543048  (legs: 4)
name: UD:U$: VT 281259648  (legs: 2)
name: UD:U$: VT 280899648  (legs: 2)
name: UD:U$: BO 280558448  (legs: 3)
name: UD:U$: 12 281019548  (legs: 2)
name: UD:U$: VT 87961348  (legs: 2)
name: UD:U$: VT 280883748  (legs: 2)
name: UD:U$: VT 284631748  (legs: 2)
name: UD:U$: VT 072686260048  (legs: 2)
name: UD:U$: VT 281798648  (legs: 2)
name: UD:U$: BO 282050748  (legs: 3)
name: UD:U$: VT 280570748  (legs: 2)
name: UD:U$: VT 281051048  (legs: 2)
name: UD:U$: BO 281280348  (legs: 3)
name: UD:U$: ST 283492848  (legs: 2)
name: UD:U$: VT 280900548  (legs: 2)
name: UD:U$: BO 282050248  (legs: 3)
name: UD:U$: VT 281257548  (legs: 2)
name: UD:U$: ST 285546148  (legs: 2)
name: UD:U$: VT 280900248  (legs: 2)
name: UD:U$: VT 285556048  (legs: 2)
name: UD:U$: VT 280948248  (legs: 2)
name: UD:U$: VT 285179148  (legs: 2)
name: UD:U$: BO 280071648  (legs: 3)
name: UD:U$: VT 280575248  (legs: 2)
name: UD:U$: GN 280051348  (legs: 3)
name: UD:U$: VT 285234948  (legs: 2)
name: UD:U$: VT 281242548  (legs: 2)
name: UD:U$: BO 280051648  (legs: 3)
name: UD:U$: CO 280579348  (legs: 4)
name: UD:U$: 12 281018948  (legs: 2)
name: UD:U$: VT 281238548  (legs: 2)
name: UD:U$: VT 280562648  (legs: 2)
name: UD:U$: VT 280545948  (legs: 2)
name: UD:U$: BO 280219748  (legs: 3)
name: UD:U$: GN 284148648  (legs: 3)
name: UD:U$: VT 281256748  (legs: 2)
name: UD:U$: CO 282182548  (legs: 4)
name: UD:U$: VT 281260348  (legs: 2)
name: UD:U$: VT 281259348  (legs: 2)
name: UD:U$: VT 280900048  (legs: 2)
name: UD:U$: VT 201267848  (legs: 2)
name: UD:U$: GN 282903948  (legs: 3)
name: UD:U$: CO 284850848  (legs: 4)
name: UD:U$: VT 284148548  (legs: 2)
name: UD:U$: VT 284825948  (legs: 2)
name: UD:U$:CVT 285374348  (legs: 2)
name: UD:U$: VT 285557548  (legs: 2)
name: UD:U$: VT 84342148  (legs: 2)
name: UD:U$: GN 031588907348  (legs: 4)
name: UD:U$: VT 281257648  (legs: 2)
name: UD:U$: VT 284932748  (legs: 2)
name: UD:U$:CGN 282904448  (legs: 2)
name: UD:U$: VT 280089348  (legs: 2)
name: UD:U$: VT 281947748  (legs: 2)
name: UD:U$: BO 280051548  (legs: 3)
name: UD:U$: BO 280051248  (legs: 3)

total parse time: 9.584773981012404
```