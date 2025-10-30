"""

Write a Python program to Find length of a string in python.

Write a Python function to find length of a string in python without using len function.

"""

str = input("Enter The string: ")

print(len(str))

length = 0

for i in str:
    length += 1

print(length)