"""

Write a Python program to print even length words in a string.

"""


str = input("Enter the string: ")

lst = str.split()

for i in lst:
    if len(i) % 2 == 0:
        print(i, end = ' ')