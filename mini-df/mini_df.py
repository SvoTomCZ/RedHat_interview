#!/usr/bin/env python3

import os
import sys

# Get total and free disk space in bytes
def get_disk_space():
    stat = os.statvfs(os.getcwd())
    total_space = stat.f_frsize * stat.f_blocks
    free_space = stat.f_frsize * stat.f_bfree
    return total_space, free_space

# Get disk space usage for a given file
def get_file_disk_space(path):
    try:
        stat = os.stat(path)
        return stat.st_size
    except Exception as e:
        print(f"Error getting disk space usage for {path}: {e}", file=sys.stderr)
        sys.exit(1)

# Get disk space usage for a given folder
def get_folder_disk_space(path):
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size

# Format bytes into human-readable format if -h arg is present
def format_bytes(bytes_value, human_readable=False):
    if human_readable:
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_value < 1024:
                return f"{bytes_value:.2f} {unit}"
            bytes_value /= 1024
    else:
        return f"{bytes_value:.0f} B"
    
# Print disk space usage for given paths
def mini_df(paths, human_readable=False):
    if not paths:
        paths = ['.']
    
    for path in paths:
        # If path is file
        if os.path.isfile(path):
            size = get_file_disk_space(path)
            size_str = format_bytes(size, human_readable)
            print(f"File: {path}")
            print(f"Used space: {size_str}")
            print()
        # If path is folder
        elif os.path.isdir(path):
            total_space, free_space = get_disk_space()
            total_space_str = format_bytes(total_space, human_readable)
            free_space_str = format_bytes(free_space, human_readable)
            print(f"\nTotal Space: {total_space_str}")
            print(f"Free Space: {free_space_str}")
            size = get_folder_disk_space(path)
            size_str = format_bytes(size, human_readable)
            print(f"Folder: {path}")
            print(f"Used space: {size_str}")
            print()
        # Path doesnt exists    
        else:
            print(f"Error: {path} does not exist.", file=sys.stderr)
            sys.exit(1)

def main():
    args = sys.argv[1:]
    
    # Bad argument check
    invalid_arg = next((arg for arg in args if arg.startswith("-") and arg not in ("-h", "--help")), None)
    if invalid_arg:
        print(f"Error: Invalid argument '{invalid_arg}'. Use --help for usage information.", file=sys.stderr)
        sys.exit(1)

    if "--help" in args:
        print("\nUsage: ./mini_df.py [-h] [PATH...]\n\n" +
              "- [-h] will output the result in human-readable format\n"+
              "- PATH can be zero or more arguments. IF zero args are given, mini_df will list the disk space usage of the current directory.\n")
        sys.exit(1)

    # if -h is present
    human_readable = "-h" in args
    paths = [path for path in args if path != "-h"]
    
    mini_df(paths, human_readable)

if __name__ == "__main__":
    main()
