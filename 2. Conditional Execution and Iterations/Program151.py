"""

Write a Python program to print the multiplication table of given number by user.

"""

n = int(input("Enter number: "))

for i in range(1, 11):
    print(n, 'x', i , '=', i*n)