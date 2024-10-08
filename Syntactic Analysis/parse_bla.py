# # parse_bla.py
# import sys
# import ply.lex as lex
# import ply.yacc as yacc

# # ------------------------
# # Lexer for Parser
# # ------------------------

# # List of token names (excluding WHITESPACE and COMMENT)
# tokens = (
#     'ID',
#     'BINARY_LITERAL',
#     'A',
#     'S',
#     'M',
#     'D',
#     'EQUALS',
#     'LPAREN',
#     'RPAREN',
# )

# # Regular expressions for simple tokens
# t_A = r'A'
# t_S = r'S'
# t_M = r'M'
# t_D = r'D'
# t_EQUALS = r'='
# t_LPAREN = r'\('
# t_RPAREN = r'\)'

# # Identifier
# def t_ID(t):
#     r'[a-z_][a-z0-9_]*'
#     return t

# # Binary Literal
# def t_BINARY_LITERAL(t):
#     r'[+-]?[01]+'
#     return t

# # Comments (both /* */ and //) to be ignored
# def t_COMMENT(t):
#     r'(//[^\n]*)|(/\*(.|\n)*?\*/)'
#     pass  # Ignore comments

# # Ignore whitespace (space, tab, newline, etc.)
# t_ignore = ' \t\r\n'

# # Error handling
# def t_error(t):
#     print(f"Illegal character '{t.value[0]}'")
#     t.lexer.skip(1)

# # Build the lexer
# lexer = lex.lex()

# # ------------------------
# # AST Node Definition
# # ------------------------

# class ASTNode:
#     def __init__(self, type, children=None, value=None):
#         self.type = type
#         self.children = children if children else []
#         self.value = value

#     def __repr__(self):
#         return f"ASTNode({self.type}, {self.value}, {self.children})"

# # ------------------------
# # Parser Rules
# # ------------------------

# # Program -> Statement*
# def p_program(p):
#     '''program : statement_list'''
#     p[0] = ASTNode('Program', p[1])

# def p_statement_list(p):
#     '''statement_list : statement_list statement
#                       | statement'''
#     if len(p) == 3:
#         p[0] = p[1] + [p[2]]
#     else:
#         p[0] = [p[1]]

# # Statement -> EQUALS ID BINARY_LITERAL
# def p_statement(p):
#     '''statement : ID EQUALS expression'''
#     equals_node = ASTNode('=', [ASTNode('ID', value=p[1]), p[3]])
#     p[0] = equals_node

# # Expression Rules
# def p_expression_add(p):
#     'expression : expression A term'
#     add_node = ASTNode('A', [p[1], p[3]])
#     p[0] = add_node

# def p_expression_sub(p):
#     'expression : expression S term'
#     sub_node = ASTNode('S', [p[1], p[3]])
#     p[0] = sub_node

# def p_expression_term(p):
#     'expression : term'
#     p[0] = p[1]

# # Term Rules
# def p_term_mul(p):
#     'term : term M factor'
#     mul_node = ASTNode('M', [p[1], p[3]])
#     p[0] = mul_node

# def p_term_div(p):
#     'term : term D factor'
#     div_node = ASTNode('D', [p[1], p[3]])
#     p[0] = div_node

# def p_term_factor(p):
#     'term : factor'
#     p[0] = p[1]

# # Factor Rules
# def p_factor_expr(p):
#     'factor : LPAREN expression RPAREN'
#     p[0] = p[2]

# def p_factor_binary(p):
#     'factor : BINARY_LITERAL'
#     binary_node = ASTNode('BINARY_LITERAL', value=p[1])
#     p[0] = binary_node

# def p_factor_id(p):
#     'factor : ID'
#     id_node = ASTNode('ID', value=p[1])
#     p[0] = id_node

# # Error rule for syntax errors
# def p_error(p):
#     if p:
#         print(f"Syntax error at token {p.type}, value {p.value}")
#     else:
#         print("Syntax error at EOF")

# # Build the parser
# parser = yacc.yacc()

# # ------------------------
# # AST Traversal
# # ------------------------

# def traverse_ast(node, output):
#     if node is None:
#         return
#     if node.value is not None:
#         output.append(f"{node.type},{node.value}")
#     else:
#         output.append(node.type)
#     for child in node.children:
#         traverse_ast(child, output)

# # ------------------------
# # Main Function
# # ------------------------

# def main():
#     if len(sys.argv) != 2:
#         print("Usage: parse_bla.py <filename.bla>")
#         sys.exit(1)

#     filename = sys.argv[1]
#     try:
#         with open(filename, 'r') as file:
#             data = file.read()
#     except IOError:
#         print(f"Cannot open {filename}")
#         sys.exit(1)

#     # Parse the data
#     result = parser.parse(data, lexer=lexer)

#     if result:
#         # Traverse the AST
#         ast_output = []
#         traverse_ast(result, ast_output)

#         for line in ast_output:
#             print(line)

#         # Write AST to .ast file
#         ast_filename = filename.rsplit('.', 1)[0] + '.ast'
#         with open(ast_filename, 'w') as ast_file:
#             for line in ast_output:
#                 ast_file.write(line + '\n')
#     else:
#         print("Parsing failed.")

# if __name__ == "__main__":
#     main()

# parse_bla.py
import sys
import ply.lex as lex
import ply.yacc as yacc

# ------------------------
# Lexer for Parser
# ------------------------

# List of token names (excluding WHITESPACE and COMMENT)
tokens = (
    'ID',
    'BINARY_LITERAL',
    'A',
    'S',
    'M',
    'D',
    'EQUALS',
    'LPAREN',
    'RPAREN',
)

# Regular expressions for simple tokens
t_A = r'A'
t_S = r'S'
t_M = r'M'
t_D = r'D'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Identifier
def t_ID(t):
    r'[a-z_][a-z0-9_]*'
    return t

# Binary Literal
def t_BINARY_LITERAL(t):
    r'[+-]?[01]+'
    return t

# Comments (both /* */ and //) to be ignored
def t_COMMENT(t):
    r'(//[^\n]*)|(/\*(.|\n)*?\*/)'
    pass  # Ignore comments

# Ignore whitespace (space, tab, newline, etc.)
t_ignore = ' \t\r\n'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# ------------------------
# AST Node Definition
# ------------------------

class ASTNode:
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.children = children if children else []
        self.value = value

    def __repr__(self):
        return f"ASTNode({self.type}, {self.value}, {self.children})"

# ------------------------
# Parser Rules
# ------------------------

# Program -> Statement*
def p_program(p):
    '''program : statement_list'''
    p[0] = ASTNode('Program', p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

# Statement -> ID EQUALS Expression
def p_statement(p):
    '''statement : ID EQUALS expression'''
    equals_node = ASTNode('=', [ASTNode('ID', value=p[1]), p[3]])
    p[0] = equals_node

# Expression Rules
def p_expression_add(p):
    'expression : expression A term'
    add_node = ASTNode('A', [p[1], p[3]])
    p[0] = add_node

def p_expression_sub(p):
    'expression : expression S term'
    sub_node = ASTNode('S', [p[1], p[3]])
    p[0] = sub_node

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

# Term Rules
def p_term_mul(p):
    'term : term M factor'
    mul_node = ASTNode('M', [p[1], p[3]])
    p[0] = mul_node

def p_term_div(p):
    'term : term D factor'
    div_node = ASTNode('D', [p[1], p[3]])
    p[0] = div_node

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

# Factor Rules
def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_factor_binary(p):
    'factor : BINARY_LITERAL'
    binary_node = ASTNode('BINARY_LITERAL', value=p[1])
    p[0] = binary_node

def p_factor_id(p):
    'factor : ID'
    id_node = ASTNode('ID', value=p[1])
    p[0] = id_node

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at token {p.type}, value {p.value}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# ------------------------
# AST Traversal with Indentation
# ------------------------

def traverse_ast(node, output, depth=0):
    if node is None:
        return
    indent = '\t' * depth
    if node.value is not None:
        output.append(f"{indent}{node.type},{node.value}")
    else:
        output.append(f"{indent}{node.type}")
    for child in node.children:
        traverse_ast(child, output, depth + 1)

# ------------------------
# Main Function
# ------------------------

def main():
    if len(sys.argv) != 2:
        print("Usage: parse_bla.py <filename.bla>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            data = file.read()
    except IOError:
        print(f"Cannot open {filename}")
        sys.exit(1)

    # Parse the data
    result = parser.parse(data, lexer=lexer)

    if result:
        # Traverse the AST with indentation
        ast_output = []
        traverse_ast(result, ast_output)

        for line in ast_output:
            print(line)

        # Write AST to .ast file
        ast_filename = filename.rsplit('.', 1)[0] + '.ast'
        with open(ast_filename, 'w') as ast_file:
            for line in ast_output:
                ast_file.write(line + '\n')
    else:
        print("Parsing failed.")

if __name__ == "__main__":
    main()
