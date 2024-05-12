#!/usr/bin/env python3

import os
import subprocess

# Run mini_ls with recursive flag and return outputs 
def run_mini_ls(paths, recursive=False):
    command = ['python3', 'mini_ls.py']
    if recursive:
        command.append('-r')
    command.extend(paths)

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    return output.decode('utf-8').splitlines()

# Test Case 1: List information about a single file
def test_single_file():
    test_file_path = "test_files/test1.txt"
    expected_output = "tomas-svoboda  -rw-rw-r--  2024-05-12 13:27:51  test_files/test1.txt"
    actual_output = run_mini_ls([test_file_path])
    try:
        assert actual_output == [expected_output], "Test Case 1: List information about a single file - Failed"
    except AssertionError as e:
        print(e)
    else:
        print("Test Case 1: List information about a single file - Passed")

# Test Case 2: List information about multiple files
def test_multiple_files():
    test_files = ["test_files/test1.txt", "test_files/test2.txt"]
    expected_output = [
        "tomas-svoboda  -rw-rw-r--  2024-05-12 13:27:51  test_files/test1.txt",
        "tomas-svoboda  -rw-rw-r--  2024-05-12 13:27:48  test_files/test2.txt"
    ]
    actual_output = run_mini_ls(test_files)
    try:
        assert actual_output == expected_output, "Test Case 2: List information about multiple files - Failed"
    except AssertionError as e:
        print(e)
    else:
        print("Test Case 2: List information about multiple files - Passed")

# Test Case 3: List information about a directory
def test_directory():
    test_directory_path = "test_files"
    actual_output = run_mini_ls([test_directory_path])
    try:
        assert actual_output == [], "Test Case 3: List information about a directory - Failed"
    except AssertionError as e:
        print(e)
    else:
        print("Test Case 3: List information about a directory - Passed")

# Test Case 4: List information about a non-existing path
def test_non_existing_path():
    non_existing_file_path = "non_existing_file.txt"
    actual_output = run_mini_ls([non_existing_file_path])
    try:
        assert actual_output == [], "Test Case 4: List information about a non-existing path - Failed"
    except AssertionError as e:
        print(e)
    else:
        print("Test Case 4: List information about a non-existing path - Passed")

# Test Case 5: List information about multiple paths including a non-existing path
def test_multiple_paths_with_non_existing():
    test_files = ["test_files/test1.txt", "test_files/test2.txt", "non_existing_file.txt"]
    actual_output = run_mini_ls(test_files)
    try:
        assert len(actual_output) == 2, "Test Case 5: List information about multiple paths including a non-existing path - Failed"
    except AssertionError as e:
        print(e)
    else:
        print("Test Case 5: List information about multiple paths including a non-existing path - Passed")

if __name__ == "__main__":
    test_single_file()
    test_multiple_files()
    test_directory()
    test_non_existing_path()
    test_multiple_paths_with_non_existing()