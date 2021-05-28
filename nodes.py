
class Node:
    i = 0
    def __init__(self):
        self.value = None
        self.children = []
        self.id = Node.newId()

    def Evaluate(self, table):
        pass

    @staticmethod
    def newId():
        Node.i += 1
        return Node.i

class BinOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.id = Node.newId()

    def Evaluate(self, table):
        left = self.children[0].Evaluate(table)[0]
        Assembly().writeText("PUSH EBX")
        right = self.children[1].Evaluate(table)[0]
        Assembly().writeText("POP EAX")

        if self.value == '+':
            Assembly().writeText("ADD EAX, EBX")
            Assembly().writeText("MOV EBX, EAX")
            result =  left + right
        elif self.value == '-':
            Assembly().writeText("SUB EAX, EBX")
            Assembly().writeText("MOV EBX, EAX")
            result =  left - right
        elif self.value == '*':
            Assembly().writeText("IMUL EBX")
            Assembly().writeText("MOV EBX, EAX")
            result =  left * right
        elif self.value == '/':
            Assembly().writeText("DIV EBX")
            Assembly().writeText("MOV EBX, EAX")
            result =  left // right
        elif(self.value == "&&"):
            Assembly().writeText("AND EAX, EBX")
            Assembly().writeText("MOV EBX, EAX")
            result = bool((left) and bool(right))
        elif(self.value == "||"):
            Assembly().writeText("OR EAX, EBX")
            Assembly().writeText("MOV EBX, EAX")
            result = bool((left) or bool(right))
        elif(self.value == ">"):
            Assembly().writeText("CMP EAX, EBX")
            Assembly().writeText("CALL binop_jg")
            result = (left > right)
        elif(self.value == "<"):
            Assembly().writeText("CMP EAX, EBX")
            Assembly().writeText("CALL binop_jl")
            result = (left < right)
        elif(self.value == "=="):
            Assembly().writeText("CMP EAX, EBX")
            Assembly().writeText("CALL binop_je")
            result = (left == right)

        if (type(result) == int):
            return(result, "int")
        return (result, "bool")

class UnOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.id = Node.newId()

    def Evaluate(self, table):
        resp = self.children[0].Evaluate(table)[0];
        if self.value == '+':
            Assembly().writeText("MOV EBX, " + str(resp))
            return (resp,"int")
        elif self.value == "-":
            Assembly().writeText("MOV EBX, -" + str(resp))
            return (-resp, "int")
        elif self.value == "!": 
            Assembly().writeText("MOV EBX, !" + str(resp))
            return (not(resp), "bool")

class IntVal(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.id = Node.newId()

    def Evaluate(self, table):
        Assembly().writeText("MOV EBX, " + str(self.value))
        return (self.value, "int")


class BoolVal(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.id = Node.newId()

    def Evaluate(self, table):
        if(self.value  == "true"):
            Assembly().writeText("MOV EBX, True")
            return (True, "bool")
        elif(self.value  == "false"):
            Assembly().writeText("MOV EBX, False")
            return (False, "bool")

class StringVal(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.id = Node.newId()

    def Evaluate(self, table):
        if type(self.value) == bool:
            return (self.value, "string")
        else:
            raise ValueError("ValueError exception thrown")

class NoOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.id = Node.newId()

    def Evaluate(self, table):
        pass

class PrintOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.id = Node.newId()

    def Evaluate(self, table):
        self.children[0].Evaluate(table)[0]
        Assembly().writeText("PUSH EBX")
        Assembly().writeText("CALL print")
        Assembly().writeText("POP EBX")

class DefineOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.id = Node.newId()

    def Evaluate(self, table):
        Assembly().writeText("PUSH DWORD 0")
        return table.declare(self.children[0], self.children[1])

class AssignmentOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.id = Node.newId()

    def Evaluate(self, table):
        resp = self.children[1].Evaluate(table)[0]
        Assembly().writeText("MOV [EBP -" + str(table.getter(self.children[0])[2]) + "], EBX")
        return table.setter(self.children[0], resp)

class IdentifierOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.id = Node.newId()

    def Evaluate(self, table):
        Assembly().writeText("MOV EBX, [EBP -" + str(table.getter(self.value)[2]) + "]")
        return table.getter(self.value)

class BlockOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.id = Node.newId()

    def Evaluate(self, table):
        for f in self.children:
            f.Evaluate(table)
        
class InputOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.id = Node.newId()

    def Evaluate(self, table):
        value = input()
        return (value, "int")

class WhileOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.id = Node.newId()

    def Evaluate(self, table):
        Assembly().writeText("LOOP_" + str(self.id) + ": ")
        self.children[0].Evaluate(table)[0]
        Assembly().writeText("CMP EBX, False")
        Assembly().writeText("JE ENDWHILE_" + str(self.id))
        self.children[1].Evaluate(table)
        Assembly().writeText("JMP LOOP_" + str(self.id))
        Assembly().writeText("ENDWHILE_" + str(self.id) + ": ")

class IfOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.id = Node.newId()

    def Evaluate(self, table):
        self.children[0].Evaluate(table)[0]
        Assembly().writeText("COMP EBX, False")
        Assembly().writeText("JE ELSE_" + str(self.id))
        self.children[1].Evaluate(table)
        Assembly().writeText("JMP ENDBLOCK_" + str(self.id))

        Assembly().writeText("ELSE_" + str(self.id) +": ")
        if len(self.children) == 3:
            self.children[2].Evaluate(table)

        Assembly().writeText("ENDBLOCK_" + str(self.id) +": ")


class Assembly:
    @staticmethod
    def startText():
        with open('program.asm', 'w') as f:
            for line in open('start.txt'):
                f.write(line)
    
    @staticmethod
    def writeText(text):
        with open("program.asm", "a") as f:
            f.write("\n" + text)

    @staticmethod
    def endText():
        with open('program.asm', 'a') as f:
            for line in open('end.txt'):
                f.write(line)


class SymbolTable:
    def __init__(self):
        self.dic_var = {}
        self.shift = 0

    def getter(self, var):
        if var in self.dic_var:
            return self.dic_var[var]
        else:
            raise ValueError("ValueError exception thrown")

    def setter(self, var, value):
        if var in self.dic_var:
            if self.dic_var[var][1] == "int":
                self.dic_var[var] = (int(value), self.dic_var[var][1], self.dic_var[var][2])
            elif self.dic_var[var][1] == "bool":
                self.dic_var[var] = (bool(value), self.dic_var[var][1], self.dic_var[var][2])
            elif self.dic_var[var][1] == "string":
                self.dic_var[var] = (str(value), self.dic_var[var][1], self.dic_var[var][2])
        else:
            raise ValueError("ValueError exception thrown")

    def declare(self, var, tp):
        self.shift +=4;
        self.dic_var[var] = (None, tp, self.shift)

