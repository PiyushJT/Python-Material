"""

Write a Python program which takes a list and returns
a list with the elements "shifted left by number of positions
entered by user".

"""

lst = [1, 2, 3, 4, 5]

shift = int(input("Enter shift: "))

lst = lst[shift:] + lst[:shift]

print(lst)