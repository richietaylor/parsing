# ast_nodes.py

class Assignment:
    def __init__(self, variable, expression, lineno):
        self.variable = variable
        self.expression = expression
        self.lineno = lineno

    def __str__(self):
        return f"Assignment({self.variable} = {self.expression})"

class BinaryOp:
    def __init__(self, operator, left, right, lineno):
        self.operator = operator
        self.left = left
        self.right = right
        self.lineno = lineno

    def __str__(self):
        return f"BinaryOp({self.operator}, {self.left}, {self.right})"

class Variable:
    def __init__(self, name, lineno):
        self.name = name
        self.lineno = lineno

    def __str__(self):
        return f"Variable({self.name})"

class Number:
    def __init__(self, value, lineno):
        self.value = value
        self.lineno = lineno

    def __str__(self):
        return f"Number({self.value})"
