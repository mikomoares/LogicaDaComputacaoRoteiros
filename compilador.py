from sys import argv

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
        else:
            raise ValueError("ValueError exception thrown")
        self.actual = new
        return new

class Parser:
    def parseExpression():
        if Parser.tokens.actual.type == 'INT':
            resultado = Parser.tokens.actual.value
            Parser.tokens.selectNext()
            while Parser.tokens.actual.type == 'PLUS' or Parser.tokens.actual.type == 'MINUS':
                if Parser.tokens.actual.type == 'MINUS':
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.type == 'INT':
                        resultado-=Parser.tokens.actual.value
                    else:
                        raise ValueError("ValueError exception thrown")
                elif Parser.tokens.actual.type == 'PLUS':
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.type == 'INT':
                        resultado+=Parser.tokens.actual.value
                    else:
                        raise ValueError("ValueError exception thrown")
                Parser.tokens.selectNext()
            if Parser.tokens.actual.type == 'EOF':
                return resultado
            else:
                raise ValueError("ValueError exception thrown")
        else:
            raise ValueError("ValueError exception thrown")
    
    def run(code):
        Parser.tokens = Tokenizer(code)
        print(Parser.parseExpression())


entry = argv[1]
Parser.run(entry)


