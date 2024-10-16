# eval_bla.py
import sys
from lexer_bla import build_lexer
from parser_bla import build_parser, ast
from ast_nodes import Assignment, BinaryOp, Variable, Number

def evaluate_expression(expr, sym_table):
    if isinstance(expr, Number):
        return expr.value
    elif isinstance(expr, Variable):
        if expr.name not in sym_table:
            print(f"semantic error on line {expr.lineno}")
            with open(source_file + ".eva", "w") as eva_file:
                eva_file.write(f"semantic error on line {expr.lineno}\n")
            sys.exit(1)
        return sym_table[expr.name]
    elif isinstance(expr, BinaryOp):
        left = evaluate_expression(expr.left, sym_table)
        right = evaluate_expression(expr.right, sym_table)
        operator = expr.operator
        if operator == 'PLUS':
            return left + right
        elif operator == 'MINUS':
            return left - right
        elif operator == 'MULT':
            return left * right
        elif operator == 'DIV':
            if right == 0:
                print(f"Division by zero on line {expr.lineno}")
                with open(source_file + ".eva", "w") as eva_file:
                    eva_file.write(f"Division by zero on line {expr.lineno}\n")
                sys.exit(1)
            return left // right  # Integer division
        else:
            print(f"Unknown operator {operator} on line {expr.lineno}")
            with open(source_file + ".eva", "w") as eva_file:
                eva_file.write(f"Unknown operator {operator} on line {expr.lineno}\n")
            sys.exit(1)
    else:
        print(f"Unknown expression type on line {expr.lineno}")
        with open(source_file + ".eva", "w") as eva_file:
            eva_file.write(f"Unknown expression type on line {expr.lineno}\n")
        sys.exit(1)

def int_to_binary(n):
    if n == 0:
        return '0'
    binary = ''
    is_negative = n < 0
    n = abs(n)
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return f"-{binary}" if is_negative else binary

def evaluate(ast_nodes):
    sym_table = {}
    results = []
    for node in ast_nodes:
        if isinstance(node, Assignment):
            try:
                value = evaluate_expression(node.expression, sym_table)
                sym_table[node.variable] = value
                binary_value = int_to_binary(value)
                result = f"{node.variable}[{binary_value}]"
                results.append(result)
                print(result)
            except Exception as e:
                # Errors are already handled in evaluate_expression
                sys.exit(1)
    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 eval_bla.py <source_file.bla>")
        sys.exit(1)

    source_file = sys.argv[1].rsplit('.', 1)[0]

    import parser_bla
    import lexer_bla

    # Set the source_file in lexer and parser BEFORE building them
    parser_bla.source_file = source_file
    lexer_bla.source_file = source_file

    # Build lexer and parser
    lexer = build_lexer()
    parser = build_parser()

    try:
        with open(sys.argv[1], 'r') as file:
            data = file.read()
        parser.parse(data, lexer=lexer)
    except FileNotFoundError:
        print(f"File {sys.argv[1]} not found.")
        sys.exit(1)
    except SystemExit:
        sys.exit(1)
    except Exception as e:
        print(f"Error during parsing: {e}")
        sys.exit(1)

    # Perform Evaluation
    try:
        results = evaluate(ast)
    except SystemExit:
        sys.exit(1)
    except Exception as e:
        # Errors are already handled in evaluate_expression
        sys.exit(1)

    # Write results to .eva file
    with open(source_file + ".eva", "w") as eva_file:
        for res in results:
            eva_file.write(res + "\n")
