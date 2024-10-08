# # lex_bla.py
# import sys
# import ply.lex as lex

# # List of token names for the lexer (Assignment 2A)
# lexer_tokens = (
#     'ID',
#     'BINARY_LITERAL',
#     'A',
#     'S',
#     'M',
#     'D',
#     'EQUALS',
#     'LPAREN',
#     'RPAREN',
#     'WHITESPACE',
#     'COMMENT',
# )

# # List of token names for the parser (Assignment 2B)
# parser_tokens = (
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

# # Choose token list based on usage
# # By default, assume lexer (Assignment 2A)
# tokens = lexer_tokens

# # Operators as literals are now defined as tokens
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

# # Comments (both /* */ and //)
# def t_COMMENT(t):
#     r'(//[^\n]*)|(/\*(.|\n)*?\*/)'
#     return t  # Return COMMENT token

# # Whitespace
# def t_WHITESPACE(t):
#     r'[ \t\r\n]+'
#     return t  # Return WHITESPACE token

# # Ignore illegal characters
# def t_error(t):
#     print(f"Illegal character '{t.value[0]}'")
#     t.lexer.skip(1)

# lexer = lex.lex()

# def lex_file(filename, output_tokens=True, exclude_tokens=None):
#     """
#     Lex the input file and optionally write tokens to a list.
#     If exclude_tokens is provided, those tokens are ignored.
#     """
#     try:
#         with open(filename, 'r') as file:
#             data = file.read()
#     except IOError:
#         print(f"Cannot open {filename}")
#         sys.exit(1)

#     lexer.input(data)
#     tokens_output = []

#     while True:
#         tok = lexer.token()
#         if not tok:
#             break
#         if exclude_tokens and tok.type in exclude_tokens:
#             continue  # Skip excluded tokens
#         if output_tokens:
#             if tok.type in parser_tokens:
#                 token_str = tok.value
#             elif tok.type == 'ID':
#                 token_str = f"ID,{tok.value}"
#             elif tok.type == 'BINARY_LITERAL':
#                 token_str = f"BINARY_LITERAL,{tok.value}"
#             elif tok.type == 'WHITESPACE':
#                 token_str = "WHITESPACE"
#             elif tok.type == 'COMMENT':
#                 token_str = "COMMENT"
#             tokens_output.append(token_str)
#             print(token_str)
#     return tokens_output

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: lex_bla.py <filename.bla>")
#         sys.exit(1)

#     filename = sys.argv[1]
#     tkn_filename = filename.rsplit('.', 1)[0] + '.tkn'
#     tokens_output = lex_file(filename)

#     # Write tokens to .tkn file
#     with open(tkn_filename, 'w') as tkn_file:
#         for token in tokens_output:
#             tkn_file.write(token + '\n')

# lex_bla.py
import sys
import ply.lex as lex

# List of token names
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
    'WHITESPACE',
    'COMMENT',
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

# Comments (both /* */ and //)
def t_COMMENT(t):
    r'(//[^\n]*)|(/\*(.|\n)*?\*/)'
    return t

# Whitespace
def t_WHITESPACE(t):
    r'[ \t\r\n]+'
    return t

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

def main():
    if len(sys.argv) != 2:
        print("Usage: lex_bla.py <filename.bla>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            data = file.read()
    except IOError:
        print(f"Cannot open {filename}")
        sys.exit(1)

    lexer.input(data)
    tokens_output = []

    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type in {'WHITESPACE', 'COMMENT'}:
            token_str = tok.type
        elif tok.type in {'A', 'S', 'M', 'D', 'EQUALS', 'LPAREN', 'RPAREN'}:
            token_str = tok.value
        elif tok.type == 'ID':
            token_str = f"ID,{tok.value}"
        elif tok.type == 'BINARY_LITERAL':
            token_str = f"BINARY_LITERAL,{tok.value}"
        tokens_output.append(token_str)
        print(token_str)

    # Write tokens to .tkn file
    tkn_filename = filename.rsplit('.', 1)[0] + '.tkn'
    with open(tkn_filename, 'w') as tkn_file:
        for token in tokens_output:
            tkn_file.write(token + '\n')

if __name__ == "__main__":
    main()
