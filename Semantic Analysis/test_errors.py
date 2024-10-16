# test_errors.py
import subprocess
import os

def run_error_test(test_name):
    source_file = f"test_cases/{test_name}.bla"
    expected_error_file = f"test_cases/{test_name}_expected.err"
    output_error_file = f"{test_name}.err"

    # Run errors_bla.py
    try:
        result = subprocess.run(
            ["python3", "errors_bla.py", source_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        # errors_bla.py exits with non-zero code on errors
        pass

    # Read expected and actual error outputs
    with open(expected_error_file, "r") as f:
        expected_output = f.read().strip()

    if os.path.exists(output_error_file):
        with open(output_error_file, "r") as f:
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
    # List of test cases that should produce errors
    error_tests = ["test4", "test5", "test6", "test7", "test10", "test12"]

    for test in error_tests:
        run_error_test(test)
