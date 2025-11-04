"""

Write a Python Program to print the largest even number in a list.

"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

largest_even = lst[0]

for i in lst:
    if i % 2 == 0 and i > largest_even:
        largest_even = i

print(largest_even)