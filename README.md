# RedHat Linux mini-utils

## mini-grep

`mini-grep` goes through every argument in FILE and prints the whole 
line in which PATTERN is found. By default `mini-grep` also outputs
the line number of each printed line.

### Usage

```bash
./mini_grep.py [-q] -e PATTERN [files ...]
```

- `-q`: Quiet mode. Display only matching lines.
- `-e PATTERN`: Specify the pattern to search for. Has to be valid regex.
- `[files ...]`: Optional list of files to search in. If not provided, it will parse entrie from the stdin.

### Example

To search for the pattern "hello" in the file `test_files/test1.txt`, run:

```bash
./mini_grep.py -e hello test_files/test1.txt
```

Alternatively, you can use:

```bash
python3 mini_grep.py -e hello test_files/test1.txt
```

This command will output:

```bash
test_files/test1.txt:1: hello
```

### Testing

Testing for mini-grep is included in the `test_mini_grep.py` file. This script tests the functionality of mini-grep with two sample files, `test_files/test1.txt` and `test_files/test2.txt`.

To run the tests, execute the following command:

```bash
./test_mini_grep.py
```

Or:

```bash
python3 test_mini_grep.py
```

The test script will run each test case and report whether it passed or failed. If any test case fails, it will provide details about the failed tests.