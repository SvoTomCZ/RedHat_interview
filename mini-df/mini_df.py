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

# Format bytes into human-readable format if requested
def format_bytes(bytes_value, human_readable=False):
    if human_readable:
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_value < 1024:
                return f"{bytes_value:.2f} {unit}"
            bytes_value /= 1024
    else:
        return str(bytes_value) + " B"

def main():
    args = sys.argv[1:]
    
    if "--help" in args:
        print("\nUsage: ./mini_df.py [-h] [PATH...]\n\n" +
              "- [-h] will output the result in human-readable format\n"+
              "- PATH can be zero or more arguments. IF zero args are given, mini_df will list the disk space usage of the current directory.\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
