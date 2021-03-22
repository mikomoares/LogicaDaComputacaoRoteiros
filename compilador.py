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
        else:
            raise ValueError("ValueError exception thrown")
        self.actual = new
        return new

class Parser:
    def parseTerm():
        if Parser.tokens.actual.type == 'INT':
            resultado = Parser.tokens.actual.value
            Parser.tokens.selectNext()
            while Parser.tokens.actual.type == 'MULT' or Parser.tokens.actual.type == 'DIV':
                if Parser.tokens.actual.type == 'DIV':
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.type == 'INT':
                        resultado//=Parser.tokens.actual.value
                    else:
                        raise ValueError("ValueError exception thrown")
                elif Parser.tokens.actual.type == 'MULT':
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.type == 'INT':
                        resultado*=Parser.tokens.actual.value
                    else:
                        raise ValueError("ValueError exception thrown")
                Parser.tokens.selectNext()
            return resultado
        else:
            raise ValueError("ValueError exception thrown")

    def parseExpression():
        resultado = Parser.parseTerm()
        while Parser.tokens.actual.type == 'PLUS' or Parser.tokens.actual.type == 'MINUS':
            if Parser.tokens.actual.type == 'MINUS':
                Parser.tokens.selectNext()
                if Parser.tokens.actual.type == 'INT':
                    resultado-=Parser.parseTerm()
                else:
                    raise ValueError("ValueError exception thrown")
            elif Parser.tokens.actual.type == 'PLUS':
                Parser.tokens.selectNext()
                if Parser.tokens.actual.type == 'INT':
                    resultado+=Parser.parseTerm()
                else:
                    raise ValueError("ValueError exception thrown")
        return resultado
    
    def run(code):
        filtered_code = Preproc.filter(code)
        Parser.tokens = Tokenizer(filtered_code)
        print(Parser.parseExpression())

class Preproc:
    def filter(code):
        filtered_code = re.sub(r"\/\*(.*?)\*\/", "", code)
        return filtered_code



entry = argv[1]
Parser.run(entry)


