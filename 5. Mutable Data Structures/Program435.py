"""

Write a Python program to rearrange positive and negative
numbers in a given array using Lambda.

"""

lst = [-1, 2, -3, 5, 7, 8, 9, -10]

lst.sort(key = lambda x: (x < 0, abs(x)))

print(lst)