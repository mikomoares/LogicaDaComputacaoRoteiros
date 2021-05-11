
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
        if self.value == '+':
            return self.children[0].Evaluate(table) + self.children[1].Evaluate(table)
        elif self.value == '-':
            return self.children[0].Evaluate(table) - self.children[1].Evaluate(table)
        elif self.value == '*':
            return self.children[0].Evaluate(table) * self.children[1].Evaluate(table)
        elif self.value == '/':
            return self.children[0].Evaluate(table) // self.children[1].Evaluate(table)
        elif(self.value == "&&"):
            return(self.children[0].Evaluate(table) and self.children[1].Evaluate(table))
        elif(self.value == "||"):
            return(self.children[0].Evaluate(table) or self.children[1].Evaluate(table))
        elif(self.value == ">"):
            return(self.children[0].Evaluate(table) > self.children[1].Evaluate(table))
        elif(self.value == "<"):
            return(self.children[0].Evaluate(table) < self.children[1].Evaluate(table))
        elif(self.value == "=="):
            return(self.children[0].Evaluate(table) == self.children[1].Evaluate(table))

class UnOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        if self.value == '+':
            return self.children[0].Evaluate(table)
        elif self.value == "-":
            return -self.children[0].Evaluate(table)
        elif self.value == "!": 
            return not(self.children[0].Evaluate(table))

class IntVal(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        return self.value

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
        return table.setter(self.children[0], self.children[1].Evaluate(table))

class IdentifierOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        return table.getter(self.value)

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

    def setter(self, var, value):
        self.dic_var[var] = value

