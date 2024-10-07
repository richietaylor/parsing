# TYLRIC007 - 1B

import ply.lex as lex
import sys



tokens = (
    'WORD',
    'NUMBER',
    'WHITESPACE',
    'PUNCTUATION',
    'HASHTAG',
    'NAME',
    'ILLEGAL'
)



# Regular expression rules for simple tokens
t_WORD = r'[A-Za-z]+'
t_NUMBER = r'\d+'
t_WHITESPACE = r'[ \t]+'
t_PUNCTUATION = r'[.,;!?]'
t_HASHTAG = r'\#[A-Za-z0-9]+'
t_NAME = r'\@[A-Za-z]+'
t_ignore = ''

# Define a rule for ILLEGAL characters by handling them in t_error
def t_error(t):
    # Create an ILLEGAL token with the illegal character
    t.type = 'ILLEGAL'
    t.value = t.value[0]
    # Skip the illegal character
    t.lexer.skip(1)
    return t

# Build the lexer
lexer = lex.lex()

# Main function to process the input file
def main():
    if len(sys.argv) != 2:
        print("Usage: lex_msg.py <filename>.msg")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        sys.exit(1)



    lexer.input(data)

    # Prepare the output token file name
    token_filename = filename.rsplit('.', 1)[0] + '.tkn'

    with open(token_filename, 'w', encoding='utf-8') as token_file:
        while True:
            tok = lexer.token()
            if not tok:
                break
            # Format the token as "TYPE,VALUE"
            token_output = f"{tok.type},{tok.value}"
            print(token_output)
            token_file.write(token_output + '\n')

if __name__ == "__main__":
    main()
