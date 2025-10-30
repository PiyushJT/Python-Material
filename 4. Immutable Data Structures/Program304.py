"""

Write a program to Create a string made of the middle three characters

"""


str = input("Enter the string: ")

mid = len(str) // 2

str = str[mid-1: mid+2]

print(str)