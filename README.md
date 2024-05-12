# RedHat Linux mini-utils

## mini-grep

`mini-grep` goes through every argument in FILE and prints the whole 
line in which PATTERN is found. By default `mini-grep` also outputs
the line number of each printed line.

### Usage

```bash
./mini_grep.py [-q] -e PATTERN [FILE...]
```

- `-q`: Quiet mode. Display only matching lines.
- `-e PATTERN`: Specify the pattern to search for. Has to be valid regex.
- `[FILE...]`: Optional list of files to search in. If not provided, it will parse entrie from the stdin.

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




## mini-ls

`mini-ls` lists information about the paths given in FILE. The information required are: Owner, Permission, Modified Time.

### Usage

```bash
./mini_ls.py [-r] [FILE...]
```

- `[-r]`: option will make `mini-ls` run recursively on any directory it comes across.
- `[FILE...]`: can be zero or more arguments. If zero args are given, `mini-ls` will list information about the current directory.

### Example

```bash
./mini_ls.py -r test_files/test1.txt
```

Alternatively, you can use:

```bash
python3 mini_ls.py -r test_files/test1.txt
```

This command will output:

```bash
tomas-svoboda  -rw-rw-r--  2024-05-12 13:27:51  test_files/test1.txt
```

### Testing

Testing for mini-ls is included in the `test_mini_ls.py` file. This script tests the functionality of mini-ls with two sample files, `test_files/test1.txt` and `test_files/test2.txt`.

To run the tests, execute the following command:

```bash
./test_mini_ls.py
```

Or:

```bash
python3 test_mini_ls.py
```

The test script will run each test case and report whether it passed or failed. If any test case fails, it will provide details about the failed tests.


## mini-df

`mini-df` outputs the file system disk space usage of each entry in
PATH. The information required is: Total Space, Free Space, Used
Space. The result should be in Bytes.

### Usage

```bash
./mini_df.py [-h] [PATH...]
```

- `[-h]`: will output the result in human-readable format.
- `[PATH...]`: an be zero or more arguments. IF zero args are given, `mini-df` will list the disk space usage of the current directory.

### Example

```bash
./mini_df.py -h ..
```

Alternatively, you can use:

```bash
python3 mini_df.py -h ..
```

This command will output:

```bash
Total Space: 72.35 GB
Free Space: 53.19 GB
Folder: ..
Used space: 93.72 KB
```

### Testing

Testing for mini-grep is included in the `test_mini_df.py` file. This script tests the functionality of mini-grep with two sample files, `test_files/test1.txt` and `test_files/test2.txt`.

To run the tests, execute the following command:

```bash
./test_mini_df.py
```

Or:

```bash
python3 test_mini_df.py
```

The test script will run each test case and report whether it passed or failed. If any test case fails, it will provide details about the failed tests.