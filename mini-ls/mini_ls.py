#!/usr/bin/env python3

import os
import sys
import stat
import datetime

# Find owner name from user ID
def find_owner_name(owner_id):
    with open("/etc/passwd", "r") as passwd_file:
        for line in passwd_file:
            fields = line.strip().split(":")
            if int(fields[2]) == owner_id:
                return fields[0]  # Return username
    return str(owner_id)  # If owner not found, return ID as string

# Get file information (owner, permissions, modified time)
def get_file_info(path):
    try:
        stat_info = os.stat(path)
        owner_id = stat_info.st_uid
        owner_name = find_owner_name(owner_id)
        permission = stat.filemode(stat_info.st_mode)
        modified_time = datetime.datetime.fromtimestamp(stat_info.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
        return owner_name, permission, modified_time
    except Exception as e:
        print(f"Error getting information for {path}: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    args = sys.argv[1:]

    if not args or "--help" in args:
        # Print usage information if no arguments provided or if argument is "--help"
        print("\nUsage: ./mini_ls.py [-r] [FILE ...]\n\n" +
              "- [-r] option will make mini_ls run recursively on any directory it comes across\n"+
              "- FILE can be zero or more arguments. If zero args are given, mini_ls will list information about the current directory.\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
