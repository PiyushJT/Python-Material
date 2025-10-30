"""

Write a program to create a string made of first,middle and last character

"""

str = input("Enter String: ")


mid = len(str)//2

str = str[0] + str[mid] + str[-1]


print(str)
