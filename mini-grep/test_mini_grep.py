#!/usr/bin/env python3

import os
import subprocess

def test_mini_grep():
    failed_tests = []

    # Test Case 1
    pattern = "hello"
    test_files = ["test_files/test1.txt", "test_files/test2.txt"]
    expected_output = ["test_files/test1.txt:1: hello", "test_files/test2.txt:2: hello world"]
    actual_output = run_mini_grep(pattern, test_files)
    try:
        assert actual_output == expected_output
    except AssertionError:
        failed_tests.append("Test Case 1: Test with a simple pattern")
    else:
        print("Test Case 1: Test with a simple pattern - Passed")

    # Test Case 2: Test with a quiet option
    pattern = "world"
    test_files = ["test_files/test1.txt", "test_files/test2.txt"]
    expected_output = ["hello world", "world domination"]
    actual_output = run_mini_grep(pattern, test_files, quiet=True)
    try:
        assert actual_output == expected_output
    except AssertionError:
        failed_tests.append("Test Case 2: Test with a quiet option")
    else:
        print("Test Case 2: Test with a quiet option - Passed")

    # Test Case 3: Test with missing pattern
    process = subprocess.Popen(['python3', 'mini_grep.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Capture the stdout and stderr output (ignored in this case)
    _, _ = process.communicate()
    return_code = process.returncode
    assert return_code != 0, "Test Case 3 Failed: Missing pattern error not raised"
    print("Test Case 3: Test with missing pattern - Passed")

    # Test Case 4: Test with missing files
    process = subprocess.Popen(['python3', 'mini_grep.py', '-e', 'hello'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
    output, _ = process.communicate(input="hello world\n")
    return_code = process.returncode
    assert return_code == 0, "Test Case 4 Failed: Missing files error not raised"
    print("Test Case 4: Test with missing files - Passed")

    # Test Case 5: Test with invalid number of arguments
    process = subprocess.Popen(['python3', 'mini_grep.py', '-e', 'hello', 'test_files/test1.txt', 'test_files/test2.txt', 'extra_argument'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, _ = process.communicate()
    return_code = process.returncode
    assert return_code != 0, "Test Case 5 Failed: Invalid number of arguments error not raised"
    print("Test Case 5: Test with invalid number of arguments - Passed")

    # Test Case 6: Test with non-existent file
    process = subprocess.Popen(['python3', 'mini_grep.py', '-e', 'hello', 'non_existent_file.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, _ = process.communicate()
    return_code = process.returncode
    assert return_code != 0, "Test Case 6 Failed: Non-existent file error not raised"
    print("Test Case 6: Test with non-existent file - Passed")

    # Print results
    if failed_tests:
        print("\nSome tests failed:")
        for test in failed_tests:
            print(test)
    else:
        print("\nAll tests passed!")


def run_mini_grep(pattern, test_files, quiet=False):
    # Run mini_grep and return output
    command = ['python3', 'mini_grep.py', '-e', pattern]
    if quiet:
        command.append('-q')
    command.extend(test_files)

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    return output.decode('utf-8').splitlines()


if __name__ == "__main__":
    test_mini_grep()
