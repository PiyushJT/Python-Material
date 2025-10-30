"""

Write a Python program to Uppercase Half String from the given string.

"""

str = input("Emter the string: ")

mid = len(str) // 2
str = str[:mid].upper() + str[mid:]

print(str)