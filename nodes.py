
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
        if (self.children[0].Evaluate(table)[1] == "string" and self.children[1].Evaluate(table)[1] == "string"):
            if(self.value == "=="):
                return (self.children[0].Evaluate(table)[0] == self.children[1].Evaluate(table)[0], "bool")
            elif(self.value == "+"):
                return (self.children[0].Evaluate(table)[0] + self.children[1].Evaluate(table)[0], "string")
            else:
                raise ValueError("ValueError exception thrown")

        
        elif (self.children[0].Evaluate(table)[1] != "string" and self.children[1].Evaluate(table)[1] != "string"):
            if self.value == '+':
                result =  self.children[0].Evaluate(table)[0] + self.children[1].Evaluate(table)[0]
            elif self.value == '-':
                result =  self.children[0].Evaluate(table)[0] - self.children[1].Evaluate(table)[0]
            elif self.value == '*':
                result =  self.children[0].Evaluate(table)[0] * self.children[1].Evaluate(table)[0]
            elif self.value == '/':
                result =  self.children[0].Evaluate(table)[0] // self.children[1].Evaluate(table)[0]
            elif(self.value == "&&"):
                result = bool((self.children[0].Evaluate(table)[0]) and bool(self.children[1].Evaluate(table)[0]))
            elif(self.value == "||"):
                result = bool((self.children[0].Evaluate(table)[0]) or bool(self.children[1].Evaluate(table)[0]))
            elif(self.value == ">"):
                result = (self.children[0].Evaluate(table)[0] > self.children[1].Evaluate(table)[0])
            elif(self.value == "<"):
                result = (self.children[0].Evaluate(table)[0] < self.children[1].Evaluate(table)[0])
            elif(self.value == "=="):
                result = (self.children[0].Evaluate(table)[0] == self.children[1].Evaluate(table)[0])
            if (type(result) == int):
                return(result, "int")
            return (result, "bool")
        else:
            raise ValueError("ValueError exception thrown")

class UnOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        if self.value == '+':
            return (self.children[0].Evaluate(table)[0],"int")
        elif self.value == "-":
            return (-self.children[0].Evaluate(table)[0], "int")
        elif self.value == "!": 
            return (not(self.children[0].Evaluate(table)[0]), "bool")

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
            return (True, "bool")
        elif(self.value  == "false"):
            return (False, "bool")

class StringVal(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        if type(self.value) == str:
            return (self.value, "string")
        else:
            raise ValueError("ValueError exception thrown")

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
        if(self.children[0].Evaluate(table)[1] == "bool"):
            if(self.children[0].Evaluate(table)[0]):
                print("true")
            else:
                print("false")
        else:
            print(self.children[0].Evaluate(table)[0])


class AssignmentOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        if self.children[0] not in table.dic_var:
            return table.declare(self.children[0], self.children[1])
        else:
            raise ValueError("ValueError exception thrown")
            
class SetterOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        if self.children[0] in table.dic_var:
            return table.setter(self.children[0], self.children[1].Evaluate(table)[0])
        else: 
            raise ValueError("ValueError exception thrown")



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
        value = input()
        return (value, "int")

class WhileOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        while(self.children[0].Evaluate(table)[0]):
            self.children[1].Evaluate(table)

class IfOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, table):
        if self.children[0].Evaluate(table)[1] == "string":
            raise ValueError("ValueError exception thrown")
        elif self.children[0].Evaluate(table)[0]:
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
        if var in self.dic_var:
            if self.dic_var[var][1] == "int":
                self.dic_var[var] = (int(value), self.dic_var[var][1])
            elif self.dic_var[var][1] == "bool":
                self.dic_var[var] = (bool(value), self.dic_var[var][1])
            elif self.dic_var[var][1] == "string":
                self.dic_var[var] = (str(value), self.dic_var[var][1])
        else:
            raise ValueError("ValueError exception thrown")

    def declare(self, var, tp):
        self.dic_var[var] = (None, tp)

