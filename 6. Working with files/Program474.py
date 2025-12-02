"""

Write a python program to search for a string in text files.

"""

search_string = input("Enter the string to search: ")
file_path = input("Enter the file path: ")

file = open(file_path, 'r')
content = file.read()

if search_string in content:
    print(f"String '{search_string}' found in the file.")
else:
    print(f"String '{search_string}' not found in the file.")

file.close()
