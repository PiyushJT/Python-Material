"""

Write a Python program to print the even numbers from a given list.

"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lst:
    if i % 2 == 0:
        print(i, end = " ")