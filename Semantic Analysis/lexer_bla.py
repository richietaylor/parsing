# lexer_bla.py
import ply.lex as lex

# Initialize source_file as None
source_file = None

# List of token names
tokens = (
    'IDENTIFIER',
    'NUMBER',
    'ASSIGN',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV',
    'LPAREN',
    'RPAREN',
)

# Regular expression rules for simple tokens
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Ignore spaces and tabs
t_ignore  = ' \t'

# Define a rule for single-line comments (// ...)
def t_LINE_COMMENT(t):
    r'//.*'
    pass  # Ignore comments

# Define a rule for multi-line comments (/* ... */)
def t_COMMENT(t):
    r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/'
    pass  # Ignore comments

# ----- Operator-Invalid Rules -----
# These rules flag operators directly followed by digits as lexical errors.
# They must be defined BEFORE the valid operator tokens to take precedence.

def t_PLUS_INVALID(t):
    r'A(?=\d)'
    global source_file
    if source_file:
        with open(source_file + ".err", "w") as err_file:
            err_file.write(f"lexical error on line {t.lineno}\n")
    else:
        print(f"lexical error on line {t.lineno}")
    t.lexer.skip(1)
    exit(1)

def t_MINUS_INVALID(t):
    r'S(?=\d)'
    global source_file
    if source_file:
        with open(source_file + ".err", "w") as err_file:
            err_file.write(f"lexical error on line {t.lineno}\n")
    else:
        print(f"lexical error on line {t.lineno}")
    t.lexer.skip(1)
    exit(1)

def t_MULT_INVALID(t):
    r'M(?=\d)'
    global source_file
    if source_file:
        with open(source_file + ".err", "w") as err_file:
            err_file.write(f"lexical error on line {t.lineno}\n")
    else:
        print(f"lexical error on line {t.lineno}")
    t.lexer.skip(1)
    exit(1)

def t_DIV_INVALID(t):
    r'D(?=\d)'
    global source_file
    if source_file:
        with open(source_file + ".err", "w") as err_file:
            err_file.write(f"lexical error on line {t.lineno}\n")
    else:
        print(f"lexical error on line {t.lineno}")
    t.lexer.skip(1)
    exit(1)

# ----- Define Valid Operator Tokens -----
def t_PLUS(t):
    r'A'
    return t

def t_MINUS(t):
    r'S'
    return t

def t_MULT(t):
    r'M'
    return t

def t_DIV(t):
    r'D'
    return t

# Define a rule for invalid identifiers (must not contain hyphens)
def t_INVALID_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*-[a-zA-Z0-9_]+'
    global source_file
    if source_file:
        with open(source_file + ".err", "w") as err_file:
            err_file.write(f"lexical error on line {t.lineno}\n")
    else:
        print(f"lexical error on line {t.lineno}")
    t.lexer.skip(len(t.value))
    exit(1)

# Define a rule for valid identifiers (no hyphens)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Define a rule for binary numbers (sequence of 0s and 1s), possibly negative
def t_NUMBER(t):
    r'-?[01]+'
    return t

# Define a rule for newlines to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule for any other invalid characters
def t_error(t):
    r'.'
    global source_file
    if source_file:
        with open(source_file + ".err", "w") as err_file:
            err_file.write(f"lexical error on line {t.lineno}\n")
    else:
        print(f"lexical error on line {t.lineno}")
    t.lexer.skip(1)
    exit(1)

# Build the lexer
def build_lexer():
    lexer = lex.lex()
    return lexer
