"""

Write a program to find all occuences of a sub string in a given string by ignoring the case.

"""


str = input("Enter the string: ").lower()
sub_str = input("Enter the substring to find: ").lower()

count = str.count(sub_str)

print(count)