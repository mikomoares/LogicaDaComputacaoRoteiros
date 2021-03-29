# LogicaDaComputacaoRoteiros
Roteiros da matéria de Lógica da Computação


Para utilizar o compilador modifique o arquivo input.c, e utilize o comando a seguir:

`python compilador.py`


### Diagrama Sintático:

<img src=Diagrama+-.png>

### EBNF:

```
EXPRESSION = TERM, { ("+" | "-"), TERM } ;
TERM = FACTOR, { ("*" | "/"), FACTOR } ;
FACTOR = ("+" | "-"), FACTOR | "(", EXPRESSION,")" | number ;

```