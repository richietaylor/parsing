# symbol_table.py

class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def define(self, name, lineno):
        self.symbols[name] = lineno

    def is_defined(self, name):
        return name in self.symbols
