# errors_bla.py
import sys
import lexer_bla
import parser_bla

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 errors_bla.py <source_file.bla>")
        sys.exit(1)
    
    source_file = sys.argv[1].rsplit('.', 1)[0]
    
    # Set the source_file in lexer and parser BEFORE building them
    lexer_bla.source_file = source_file
    parser_bla.source_file = source_file
    
    # Build lexer and parser
    lexer = lexer_bla.build_lexer()
    parser = parser_bla.build_parser()
    
    try:
        with open(sys.argv[1], 'r') as file:
            data = file.read()
    except FileNotFoundError:
        print(f"File {sys.argv[1]} not found.")
        sys.exit(1)
    
    # Parse the data
    parser.parse(data, lexer=lexer)
    
    print("Semantic analysis completed successfully.")

if __name__ == "__main__":
    main()
