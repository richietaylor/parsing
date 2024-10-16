# test_parser.py
from lexer_bla import build_lexer
from parser_bla import build_parser, ast
import parser_bla

def main():
    # Define the source file name (without extension)
    source_file = 'valx_valy'
    # Assign it to parser_bla's source_file
    parser_bla.source_file = source_file
    
    lexer = build_lexer()
    parser = build_parser()
    
    data = "valx = 10101\nvaly = 101Avalz"
    parser.parse(data, lexer=lexer)
    
    # Print the AST
    for node in ast:
        print(node)

if __name__ == "__main__":
    main()
