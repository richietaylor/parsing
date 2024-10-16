# test_lexer.py
import sys
import lexer_bla  # Import the entire lexer_bla module

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 test_lexer.py <source_file.bla>")
        sys.exit(1)
    
    source_file = sys.argv[1].rsplit('.', 1)[0]
    
    # Set the source_file for error reporting
    lexer_bla.source_file = source_file  # Now 'lexer_bla' is defined
    
    lexer = lexer_bla.build_lexer()  # Use the build_lexer function from lexer_bla
    
    try:
        with open(sys.argv[1], 'r') as file:
            data = file.read()
    except FileNotFoundError:
        print(f"File {sys.argv[1]} not found.")
        sys.exit(1)
    
    lexer.input(data)
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

if __name__ == "__main__":
    main()
