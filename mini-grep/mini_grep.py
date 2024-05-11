#!/usr/bin/env python3

import re
import sys

# Function to search for a pattern in files or standard input
def mini_grep(pattern, files, quiet=False):
    if not files:
        # Read from standard input
        for line_num, line in enumerate(sys.stdin, start=1):
            if re.search(pattern, line):
                if quiet:
                    print(line.rstrip())  # Print matching line without newline
                else:
                    print(f"<stdin>:{line_num}: {line.rstrip()}")  # Print filename, line number, and matching line
    else:
        # Read from files
        for file in files:
            with open(file, 'r') as f:
                for line_num, line in enumerate(f, start=1):
                    if re.search(pattern, line):
                        if quiet:
                            print(line.rstrip())  # Print matching line without newline
                        else:
                            print(f"{file}:{line_num}: {line.rstrip()}")  # Print filename, line number, and matching line

# Main function to handle command line arguments and execute the program
def main():
    args = sys.argv[1:]  # Get command line arguments, excluding script name

    if not args or "--help" in args:
        # Print usage information if no arguments provided or "--help" option specified
        print("\nUsage: ./mini_grep.py [-q] -e PATTERN [files ...]\n\n" +
              "- [-q] only outputs lines but omits the matching line numbers\n"+
              "- PATTERN has to be a valid regex\n"+
              "- FILE can be zero or more arguments. If zero args are given, mini-grep will parse entries from the stdin\n")
        sys.exit(1)

    pattern = None
    quiet = False
    files = []

    i = 0
    while i < len(args):
        if args[i] == "-q":
            quiet = True  # Set quiet flag if "-q" option is present
        elif args[i] == "-e":
            if i + 1 >= len(args):
                print("Error: Missing pattern after -e")
                sys.exit(1)
            pattern = args[i + 1]  # Set pattern to the next argument
            i += 1  # Increment loop counter to skip the pattern argument
        elif args[i].startswith("-"):
            print(f"Error: Unrecognized argument '{args[i]}'")
            sys.exit(1)
        else:
            files.append(args[i])  # Add filename argument to the list of files
        i += 1

    if not pattern:
        print("Error: Pattern is required.")
        sys.exit(1)

    try:
        mini_grep(pattern, files, quiet)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
