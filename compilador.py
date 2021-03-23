from sys import argv
import re

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
        resultado = 0
        if Parser.tokens.actual.type == 'PLUS':
            Parser.tokens.selectNext()
            resultado += Parser.parseFactor()
        elif Parser.tokens.actual.type == 'MINUS':
            Parser.tokens.selectNext()
            resultado -= Parser.parseFactor()
        elif Parser.tokens.actual.type == '(':
            Parser.tokens.selectNext()
            resultado = Parser.parseExpression()
            if Parser.tokens.actual.type == ')':
                Parser.tokens.selectNext()
            else:
                raise ValueError("ValueError exception thrown")
        elif Parser.tokens.actual.type == 'INT':
            resultado = Parser.tokens.actual.value
            Parser.tokens.selectNext()
        return resultado

    def parseTerm():
        resultado = Parser.parseFactor()
        while Parser.tokens.actual.type == 'MULT' or Parser.tokens.actual.type == 'DIV':
            if Parser.tokens.actual.type == 'DIV':
                Parser.tokens.selectNext()
                resultado//=Parser.parseFactor()
            elif Parser.tokens.actual.type == 'MULT':
                Parser.tokens.selectNext()
                resultado*=Parser.parseFactor()
        return resultado

    def parseExpression():
        resultado = Parser.parseTerm()
        while Parser.tokens.actual.type == 'PLUS' or Parser.tokens.actual.type == 'MINUS':
            if Parser.tokens.actual.type == 'MINUS':
                Parser.tokens.selectNext()
                resultado-=Parser.parseTerm()
            elif Parser.tokens.actual.type == 'PLUS':
                Parser.tokens.selectNext()
                resultado+=Parser.parseTerm()
        return resultado
    
    def run(code):
        filtered_code = Preproc.filter(code)
        Parser.tokens = Tokenizer(filtered_code)
        resposta = Parser.parseExpression()
        if Parser.tokens.actual.type == 'EOF':
            print(resposta)
        else:
            raise ValueError("ValueError exception thrown")

class Preproc:
    def filter(code):
        filtered_code = re.sub(r"\/\*(.*?)\*\/", "", code)
        return filtered_code



entry = argv[1]
Parser.run(entry)


