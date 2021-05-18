
class Node:
    def __init__(self):
        self.value = None
        self.children = []

    def Evaluate(self, table):
        pass

class BinOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        if (self.children[0].Evaluate(table)[1] == "string"):
            if(self.value == "=="):
                return (self.children[0].Evaluate(table)[0] == self.children[1].Evaluate(table)[0], "bool")
            if (self.children[1][1] == "string"):
                if(self.value == "+"):
                    return (self.children[0].Evaluate(table)[0] + self.children[1].Evaluate(table)[0], "string")
                else:
                    raise NameError("ValueError exception thrown")
            elif (self.children[1].Evaluate(table)[1] == "int"):
                if(self.value == "*"):
                    res = self.children[0].Evaluate(table)[0]
                    for i in range(0,self.children[1].Evaluate(table)[0]):
                        res += self.children[0].Evaluate(table)[0]
                    return (res, "string")
                else: 
                    raise NameError("ValueError exception thrown")
            else:
                raise NameError("ValueError exception thrown")
        else:
            if self.value == '+':
                result =  self.children[0].Evaluate(table)[0] + self.children[1].Evaluate(table)[0]
            elif self.value == '-':
                result =  self.children[0].Evaluate(table)[0] - self.children[1].Evaluate(table)[0]
            elif self.value == '*':
                result =  self.children[0].Evaluate(table)[0] * self.children[1].Evaluate(table)[0]
            elif self.value == '/':
                result =  self.children[0].Evaluate(table)[0] // self.children[1].Evaluate(table)[0]
            elif(self.value == "&&"):
                result = (self.children[0].Evaluate(table)[0] and self.children[1].Evaluate(table)[0])
            elif(self.value == "||"):
                result = (self.children[0].Evaluate(table)[0] or self.children[1].Evaluate(table)[0])
            elif(self.value == ">"):
                result = (self.children[0].Evaluate(table)[0] > self.children[1].Evaluate(table)[0])
            elif(self.value == "<"):
                result = (self.children[0].Evaluate(table)[0] < self.children[1].Evaluate(table)[0])
            elif(self.value == "=="):
                result = (self.children[0].Evaluate(table)[0] == self.children[1].Evaluate(table)[0])
            if (type(result) == "int"):
                return(result, "int")
            return (result, "bool")

class UnOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        if self.value == '+':
            return self.children[0].Evaluate(table)[0]
        elif self.value == "-":
            return -self.children[0].Evaluate(table)[0]
        elif self.value == "!": 
            return not(self.children[0].Evaluate(table)[0])

class IntVal(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        return (self.value, "int")

class BoolVal(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        if(self.value  == "true"):
            return ("true", "bool")
        elif(self.value  == "false"):
            return ("false", "bool")
        else:
            raise ValueError("ValueError exception thrown")

class StringVal(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        return (self.value, "string")

class NoOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        pass

class PrintOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        print(self.children[0].Evaluate(table))

class AssignmentOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):

        return table.setter(self.children[0], self.children[1].Evaluate(table)[0], self.children[1].Evaluate(table)[1])

class IdentifierOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table, tp):
        if self.children[0] in table.dic_var:
            return table.setter(self.children[0], )
        return table.declare(self.children[0], )

class BlockOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        for f in self.children:
            f.Evaluate(table)
        
class InputOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        value = int(input())
        return value

class WhileOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        while(self.children[0].Evaluate(table)):
            self.children[1].Evaluate(table)

class IfOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        if(self.children[0].Evaluate(table)):
            self.children[1].Evaluate(table)
        elif(len(self.children) == 3):
            self.children[2].Evaluate(table)

class SymbolTable:
    def __init__(self):
        self.dic_var = {}

    def getter(self, var):
        if var in self.dic_var:
            return self.dic_var[var]
        else:
            raise ValueError("ValueError exception thrown")

    def setter(self, var, value, tp):
        if var in self.dic_var:
            if self.dic_var[var][1] == tp:
                self.dic_var[var] = (value)
            else:
                raise ValueError("ValueError exception thrown")
        else:
            raise ValueError("ValueError exception thrown")

    def Declare(self, var, tp):
        self.dic_var[var] = (None, tp)

