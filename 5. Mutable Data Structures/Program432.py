"""

Write a Python program of Reversing a List.

"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 0

while i < len(lst) // 2:
    lst[i], lst[-1-i] = lst[-1-i], lst[i]
    i += 1

print(lst)