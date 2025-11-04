"""

Write a Python Program to print the largest odd number in a list.

"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

largest_odd = lst[0]

for i in lst:
    if i % 2 == 1 and i > largest_odd:
        largest_odd = i

print(largest_odd)