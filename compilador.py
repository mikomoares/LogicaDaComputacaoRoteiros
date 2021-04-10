from sys import argv
import re
from nodes import *

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
        while self.position<len(self.origin) and self.origin[self.position]==" ":
            self.position+=1
        if self.position == len(self.origin):
            new = Token("EOF", "")
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
        else:
            raise ValueError("ValueError exception thrown")
        self.actual = new
        return new

class Parser:
    def parseFactor():

        if Parser.tokens.actual.type == 'PLUS':
            Parser.tokens.selectNext()
            resultado = UnOp('+', [Parser.parseFactor()])

        elif Parser.tokens.actual.type == 'MINUS':
            Parser.tokens.selectNext()
            resultado = UnOp('-', [Parser.parseFactor()])

        elif Parser.tokens.actual.type == '(':
            Parser.tokens.selectNext()
            resultado = Parser.parseExpression()
            if Parser.tokens.actual.type == ')':
                Parser.tokens.selectNext()
            else:
                raise ValueError("ValueError exception thrown")

        elif Parser.tokens.actual.type == 'INT':
            resultado = IntVal(Parser.tokens.actual.value, [])
            Parser.tokens.selectNext()

        else:
            raise ValueError("ValueError exception thrown")

        return resultado

    def parseTerm():
        resultado = Parser.parseFactor()

        while Parser.tokens.actual.type == 'MULT' or Parser.tokens.actual.type == 'DIV':

            if Parser.tokens.actual.type == 'DIV':
                Parser.tokens.selectNext()
                resultado = BinOp('/', [resultado, Parser.parseFactor()])

            elif Parser.tokens.actual.type == 'MULT':
                Parser.tokens.selectNext()
                resultado = BinOp('*', [resultado, Parser.parseFactor()])

        return resultado

    def parseExpression():
        resultado = Parser.parseTerm()

        while Parser.tokens.actual.type == 'PLUS' or Parser.tokens.actual.type == 'MINUS':

            if Parser.tokens.actual.type == 'MINUS':
                Parser.tokens.selectNext()
                resultado = BinOp('-', [resultado, Parser.parseTerm()])

            elif Parser.tokens.actual.type == 'PLUS':
                Parser.tokens.selectNext()
                resultado = BinOp('+', [resultado, Parser.parseTerm()])

        return resultado
    
    def run(code):
        filtered_code = Preproc.filter(code)
        Parser.tokens = Tokenizer(filtered_code)
        resposta = Parser.parseExpression()
        if Parser.tokens.actual.type == 'EOF':
            print(resposta.Evaluate())
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