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

# Get list information about given paths
def mini_ls(paths, recursive=False):
    for path in paths:
        if os.path.exists(path):
            # If it's a file
            if os.path.isfile(path):
                owner, permission, modified_time = get_file_info(path)
                if owner:
                    print(f"{owner}  {permission}  {modified_time}  {path}")
            # If it's a folder        
            elif os.path.isdir(path):
                if recursive:
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            owner, permission, modified_time = get_file_info(file_path)
                            if owner:
                                print(f"{owner}  {permission}  {modified_time}  {file_path}")
                else:
                    print(f"Error: {path} is a directory. Use -r option for recursive listing.", file=sys.stderr)
                    sys.exit(1)
            else:
                print(f"Error: {path} is not a regular file or directory.", file=sys.stderr)
                sys.exit(1)
        else:
            print(f"Error: {path} does not exist.", file=sys.stderr)
            sys.exit(1)

def main():
    args = sys.argv[1:]

    if not args or "--help" in args:
        # Print usage information if no arguments provided or if argument is "--help"
        print("\nUsage: ./mini_ls.py [-r] [FILE ...]\n\n" +
              "- [-r] option will make mini_ls run recursively on any directory it comes across\n"+
              "- FILE can be zero or more arguments. If zero args are given, mini_ls will list information about the current directory.\n")
        sys.exit(1)

    recursive = False
    paths = []

    for arg in args:
        if arg == "-r":
            recursive = True
        else:
            paths.append(arg)

    if not paths:
        paths.append(".")

    mini_ls(paths, recursive)

if __name__ == "__main__":
    main()
