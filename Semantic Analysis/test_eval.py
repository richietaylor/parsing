# test_evaluation.py
import subprocess
import os

def run_eval_test(test_name):
    source_file = f"test_cases/{test_name}.bla"
    expected_output_file = f"test_cases/{test_name}_expected.eva"
    output_file = f"{test_name}.eva"

    # First, check for errors using errors_bla.py
    try:
        subprocess.run(
            ["python3", "errors_bla.py", source_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"{test_name}: Failed during semantic analysis.")
        return

    # Run eval_bla.py
    try:
        result = subprocess.run(
            ["python3", "eval_bla.py", source_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"{test_name}: Failed during evaluation.")
        return

    # Read expected and actual outputs
    with open(expected_output_file, "r") as f:
        expected_output = f.read().strip()

    if os.path.exists(output_file):
        with open(output_file, "r") as f:
            actual_output = f.read().strip()
    else:
        actual_output = ""

    # Compare outputs
    if expected_output == actual_output:
        print(f"{test_name}: Passed")
    else:
        print(f"{test_name}: Failed")
        print("Expected Output:")
        print(expected_output)
        print("Actual Output:")
        print(actual_output)

if __name__ == "__main__":
    # List of test cases that should be evaluated
    eval_tests = ["test1", "test2", "test3", "test8", "test9", "test11", "test13", "test14", "test15"]

    for test in eval_tests:
        run_eval_test(test)
