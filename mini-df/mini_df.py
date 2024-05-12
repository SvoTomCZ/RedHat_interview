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
