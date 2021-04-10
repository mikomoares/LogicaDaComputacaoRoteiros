# LogicaDaComputacaoRoteiros
Roteiros da matéria de Lógica da Computação


Para utilizar o compilador crie um arquivo c, e utilize o comando a seguir:

`python compilador.py <in.c>`

Exemplo (criando um arquivo "expressão1.c):

`python compilador.py expressão1.c`

### Diagrama Sintático:

<img src=Diagrama+-.png>

### EBNF:

```
EXPRESSION = TERM, { ("+" | "-"), TERM } ;
TERM = FACTOR, { ("*" | "/"), FACTOR } ;
FACTOR = ("+" | "-"), FACTOR | "(", EXPRESSION,")" | number ;

```