# LogicaDaComputacaoRoteiros
Roteiros da matéria de Lógica da Computação


Para utilizar o compilador utilize o comando a seguir:

`python compilador.py "<operações>"`

Exemplo:

`python compilador.py "+(2+2)-3*23/244"`

### Diagrama Sintático:

<img src=Diagrama+-.png>

### EBNF:

```
EXPRESSION = TERM, { ("+" | "-"), TERM } ;
TERM = FACTOR, { ("*" | "/"), FACTOR } ;
FACTOR = ("+" | "-"), FACTOR | "(", EXPRESSION,")" | number ;

```