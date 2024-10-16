# parser_bla.py
import ply.yacc as yacc
from lexer_bla import tokens
from ast_nodes import Assignment, BinaryOp, Variable, Number

# Initialize source_file as None
source_file = None

# Precedence rules to handle operator precedence
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV'),
)

# The AST root
ast = []

# Start symbol: statements
def p_statements_multiple(p):
    'statements : statements statement'
    p[0] = p[1]
    ast.append(p[2])

def p_statements_single(p):
    'statements : statement'
    p[0] = p[1]
    ast.append(p[1])

# Assignment statement
def p_statement_assign(p):
    'statement : IDENTIFIER ASSIGN expression'
    assignment = Assignment(p[1], p[3], p.lineno(1))
    p[0] = assignment

# Expression rules
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULT expression
                  | expression DIV expression'''
    p[0] = BinaryOp(p.slice[2].type, p[1], p[3], p.lineno(2))

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    try:
        if p[1].startswith('-'):
            value = -int(p[1][1:], 2)
        else:
            value = int(p[1], 2)
    except ValueError:
        print(f"parse error on line {p.lineno(1)}")
        with open(source_file + ".err", "w") as err_file:
            err_file.write(f"parse error on line {p.lineno(1)}\n")
        exit(1)
    p[0] = Number(value, p.lineno(1))

def p_expression_variable(p):
    'expression : IDENTIFIER'
    p[0] = Variable(p[1], p.lineno(1))

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"parse error on line {p.lineno}")
        with open(source_file + ".err", "w") as err_file:
            err_file.write(f"parse error on line {p.lineno}\n")
    else:
        print("parse error at EOF")
        with open(source_file + ".err", "w") as err_file:
            err_file.write("parse error at EOF\n")
    exit(1)

# Build the parser with 'statements' as the start symbol
def build_parser():
    return yacc.yacc(start='statements')
