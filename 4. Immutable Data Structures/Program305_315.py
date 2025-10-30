"""

Write a program to check if two strings are balanced. For example,
strings s1 and s2 are balanced if all the
characters in the s1 are present in s2 and length
of s1 & s2 should be same. The character’s position doesn’t
matter.

"""


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

is_balanced = True

for i in str1:
    if i not in str2:
        is_balanced = False
        break

for i in str2:
    if i not in str1:
        is_balanced = False
        break

if len(str1) != len(str2):
    is_balanced = False

for i in range(len(str1)):
    if str1.count(str1[i]) != str2.count(str1[i]):
        is_balanced = False
        break

if is_balanced:
    print("The strings are balanced.")
else:
    print("The strings are not balanced.")