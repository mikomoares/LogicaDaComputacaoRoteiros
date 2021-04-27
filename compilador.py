from sys import argv
import re
from nodes import *

reserved = ["println"]
PRINTLN = reserved

class Token:
    def __init__(self, token_type, token_value):
        self.type = token_type
        self.value = token_value

class Tokenizer:
    def __init__(self, origin):
        self.origin = origin
        self.position = 0
        self.actual = self.selectNext()

    def selectNext(self):
        num=''
        while self.position<len(self.origin) and (self.origin[self.position]==" " or  self.origin[self.position]=="\n"):
            self.position+=1
        if self.position == len(self.origin):
            new = Token("EOF", "")
        elif self.origin[self.position] == ';':
            new = Token("LB", ";")
            self.position+=1
        elif(self.origin[self.position].isdigit()):
            while(self.position<len(self.origin) and self.origin[self.position].isdigit()):
                num+=self.origin[self.position]
                self.position+=1
            new = Token('INT', int(num))
        elif(self.origin[self.position] == '-'):
            new = Token('MINUS','-')
            self.position+=1
        elif(self.origin[self.position] == '+'):
            new = Token('PLUS','+')
            self.position+=1
        elif(self.origin[self.position] == '*'):
            new = Token('MULT','*')
            self.position+=1
        elif(self.origin[self.position] == '/'):
            new = Token('DIV','/')
            self.position+=1
        elif(self.origin[self.position] == '('):
            new = Token('(','(')
            self.position+=1
        elif(self.origin[self.position] == ')'):
            new = Token(')',')')
            self.position+=1
        elif self.origin[self.position] == '=':
            new = Token("ASSIG", "=")
            self.position+=1
        elif self.origin[self.position].isalpha():
            num+=self.origin[self.position]
            self.position+=1
            while self.position<len(self.origin) and (self.origin[self.position].isdigit() or self.origin[self.position].isalpha() or self.origin[self.position]=="_"):
                num+=self.origin[self.position]
                self.position+=1

            new = num.upper()

            if num in reserved:
                new = Token(new, new)
            else: 
                new = Token("IDENT", new)
        else:
            raise ValueError("ValueError exception thrown")
        self.actual = new
        return new

class Parser:

    def parseBlock():
        results=[]
        while Parser.tokens.actual.type != 'EOF':
            results.append(Parser.parseCommand())
            if Parser.tokens.actual.type != 'LB':
                raise ValueError("ValueError exception thrown")
            else:
                Parser.tokens.selectNext()

        return BlockOp("block", results)

    def parseCommand():
        if Parser.tokens.actual.type == 'IDENT':
            var = Parser.tokens.actual.value
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == 'ASSIG':
                Parser.tokens.selectNext()
                result = AssignmentOp("=", [var, Parser.parseExpression()])
            else:
                raise ValueError("ValueError exception thrown")

        elif Parser.tokens.actual.type == 'PRINTLN':
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == '(':
                Parser.tokens.selectNext()
                result_tmp = Parser.parseExpression()
                if Parser.tokens.actual.type == ')':
                    Parser.tokens.selectNext()
                else:
                    raise ValueError("ValueError exception thrown")
            result = PrintOp("PRINTLN", [result_tmp])

        else:
            result = NoOp(0, [])

        return result



    def parseFactor():

        if Parser.tokens.actual.type == 'PLUS':
            Parser.tokens.selectNext()
            result = UnOp('+', [Parser.parseFactor()])

        elif Parser.tokens.actual.type == 'MINUS':
            Parser.tokens.selectNext()
            result = UnOp('-', [Parser.parseFactor()])

        elif Parser.tokens.actual.type == '(':
            Parser.tokens.selectNext()
            result = Parser.parseExpression()
            if Parser.tokens.actual.type == ')':
                Parser.tokens.selectNext()
            else:
                raise ValueError("ValueError exception thrown")

        elif Parser.tokens.actual.type == 'INT':
            result = IntVal(Parser.tokens.actual.value, [])
            Parser.tokens.selectNext()

        elif Parser.tokens.actual.type == 'IDENT':
            result = IdentifierOp(Parser.tokens.actual.value, [])
            Parser.tokens.selectNext()

        else:
            raise ValueError("ValueError exception thrown")

        return result

    def parseTerm():
        result = Parser.parseFactor()

        while Parser.tokens.actual.type == 'MULT' or Parser.tokens.actual.type == 'DIV':

            if Parser.tokens.actual.type == 'DIV':
                Parser.tokens.selectNext()
                result = BinOp('/', [result, Parser.parseFactor()])

            elif Parser.tokens.actual.type == 'MULT':
                Parser.tokens.selectNext()
                result = BinOp('*', [result, Parser.parseFactor()])

        return result

    def parseExpression():
        result = Parser.parseTerm()

        while Parser.tokens.actual.type == 'PLUS' or Parser.tokens.actual.type == 'MINUS':

            if Parser.tokens.actual.type == 'MINUS':
                Parser.tokens.selectNext()
                result = BinOp('-', [result, Parser.parseTerm()])

            elif Parser.tokens.actual.type == 'PLUS':
                Parser.tokens.selectNext()
                result = BinOp('+', [result, Parser.parseTerm()])

        return result
    
    def run(code):
        table = SymbolTable()
        filtered_code = Preproc.filter(code)
        Parser.tokens = Tokenizer(filtered_code)
        resposta = Parser.parseBlock()
        if Parser.tokens.actual.type == 'EOF':
            resposta.Evaluate(table)
        else:
            raise ValueError("ValueError exception thrown")

class Preproc:
    def filter(code):
        filtered_code = re.sub(r"\/\*(.*?)\*\/", "", code)
        return filtered_code

file = argv[1] 
with open (file, 'r') as file:
    entry = file.read()

Parser.run(entry)
