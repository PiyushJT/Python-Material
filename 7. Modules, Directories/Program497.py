"""

Write a python program to create a directory and subdirectory. 
It should print the current working directory path and list
of names of files present in the given directory.

"""

import os

# Print current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# Create a directory
dir_name = "test"
os.mkdir(dir_name)
print(f"\nDirectory '{dir_name}' created successfully!")

sub_dir_name = 'subtest'
os.mkdir(f"{dir_name}/{sub_dir_name}")
print(f"Directory Created")