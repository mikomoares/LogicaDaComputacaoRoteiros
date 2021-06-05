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
FUNCDEFBLOCK = (λ | TYPE,IDENTIFIER, "(", {TYPE, IDENTIFIER},{(",",TYPE,IDENTIFIER)}, ")", COMMAND);
BLOCK = "{", { COMMAND }, "}" ; 
COMMAND = ( λ | ASSIGNMENT | PRINT | BLOCK | WHILE | IF | DECLARATOR | RETURN), ";" ; 
RETURN = "return", OREXPRESSION
DECLARATOR = (INT | BOOL | STRING), IDENTIFIER;
WHILE = "while", "(", OREXPR ,")", COMMAND;
IF = "if", "(", OREXPR ,")", COMMAND, (("else", COMMAND) | λ );
ASSIGNMENT = IDENTIFIER, "=", EXPRESSION ; 
PRINT = "println", "(", OREXPR, ")" ; 
OREXPR = ANDEXPR, { "||", ANDEXPR } ;
ANDEXPR = EQEXPR, { "&&", EQEXPR } ;
EQEXPR = RELEXPR, { "==", RELEXPR } ;
RELEXPR = EXPRESSION, { (">"|"<"),  EXPRESSION }
EXPRESSION = TERM, { ("+" | "-"), TERM } ; 
TERM = FACTOR, { ("*" | "/"), FACTOR } ; 
FACTOR = (("+" | "-" | "!" ), FACTOR) | NUMBER | STRING | BOOL | "(", OREXPR,  ")" | IDENTIFIER | READLN;
READLN = "readln", "(",")";
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" }, { "(", {(OREXPR), ","}, ")" } ;
NUMBER = DIGIT, { DIGIT } ; 
STRING = '"', { LETTER | DIGIT }, '"' ; 
LETTER = ( a | ... | z | A | ... | Z ) ; 
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;

```