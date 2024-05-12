#!/usr/bin/env python3

import subprocess
import re

# Run mini_df with human-readable flag and return outputs 
def run_mini_df(paths, human_readable=False):
    command = ['python3', 'mini_df.py']
    if human_readable:
        command.append('-h')
    command.extend(paths)

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode('utf-8').splitlines() + stderr.decode('utf-8').splitlines()

# Test Case 1: No arguments provided
def test_no_arguments():
    expected_output = ['', r'Total Space: \d+\.?\d* ?\w+', r'Free Space: \d+\.?\d* ?\w+', 'Folder: .', r'Used space: \d+\.?\d* ?\w+', '']
    actual_output = run_mini_df([])
    try:
        assert all([bool(re.match(pattern, line)) for pattern, line in zip(expected_output, actual_output)]), "Test Case 1: No arguments provided - Failed"
    except AssertionError as e:
        print(e)
    else:
        print("Test Case 1: No arguments provided - Passed")

# Test Case 2: -h option provided
def test_h_option():
    expected_output = ['', r'Total Space: \d+\.?\d* ?\w+', r'Free Space: \d+\.?\d* ?\w+', 'Folder: .', r'Used space: \d+\.?\d* ?\w+', '']
    actual_output = run_mini_df([], human_readable=True)
    try:
        assert all([bool(re.match(pattern, line)) for pattern, line in zip(expected_output, actual_output)]), "Test Case 2: -h option provided - Failed"
    except AssertionError as e:
        print(e)
    else:
        print("Test Case 2: -h option provided - Passed")

# Test Case 3: Single file provided
def test_single_file():
    test_file_path = "test_files/test1.txt"
    expected_output = [r'File: test_files/test1.txt', r'Used space: \d+\.?\d* ?\w+']
    actual_output = run_mini_df([test_file_path])
    try:
        assert all([bool(re.match(pattern, line)) for pattern, line in zip(expected_output, actual_output)]), "Test Case 3: Single file provided - Failed"
    except AssertionError as e:
        print(e)
    else:
        print("Test Case 3: Single file provided - Passed")

# Test Case 4: Non-existing file provided
def test_non_existing_file():
    non_existing_file_path = "non_existing_file.txt"
    expected_output = ['Error: non_existing_file.txt does not exist.']
    actual_output = run_mini_df([non_existing_file_path])
    try:
        assert any(expected in output for output in actual_output for expected in expected_output), "Test Case 4: Non-existing file provided - Failed"
    except AssertionError as e:
        print(e)
    else:
        print("Test Case 4: Non-existing file provided - Passed")

# Test Case 5: Multiple files/folders provided
def test_multiple_files():
    test_files = ["test_files/test1.txt", "test_files/test2.txt"]
    expected_output = [r'File: test_files/test1.txt', r'Used space: \d+\.?\d* ?\w+', '', r'File: test_files/test2.txt', r'Used space: \d+\.?\d* ?\w+', '', r'File: test_files/test2.txt', r'Used space: \d+\.?\d* ?\w+']
    actual_output = run_mini_df(test_files)
    try:
        assert all(re.match(pattern, line) for pattern, line in zip(expected_output, actual_output)), "Test Case 5: Multiple files/folders provided - Failed"
    except AssertionError as e:
        print(e)
    else:
        print("Test Case 5: Multiple files/folders provided - Passed")

# Test Case 6: Bad argument provided
def test_bad_argument():
    bad_argument = "-x"
    expected_output = ["Error: Invalid argument '-x'. Use --help for usage information."]
    actual_output = run_mini_df([bad_argument])
    try:
        assert actual_output == expected_output, "Test Case 6: Bad argument provided - Failed"
    except AssertionError as e:
        print(e)
    else:
        print("Test Case 6: Bad argument provided - Passed")

if __name__ == "__main__":
    test_no_arguments()
    test_h_option()
    test_single_file()
    test_non_existing_file()
    test_multiple_files()
    test_bad_argument()
