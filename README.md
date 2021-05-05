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
BLOCK = { COMMAND } ;
COMMAND = ( λ | ASSIGNMENT | PRINT), ";" ;
ASSIGNMENT = IDENTIFIER, "=", EXPRESSION ;
PRINT = "println", "(", EXPRESSION, ")" ;
EXPRESSION = TERM, { ("+" | "-"), TERM } ;
TERM = FACTOR, { ("*" | "/"), FACTOR } ;
FACTOR = (("+" | "-"), FACTOR) | NUMBER | "(", EXPRESSION, ")" | IDENTIFIER ;
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
NUMBER = DIGIT, { DIGIT } ;
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ; 
```