"""

Write a Python program to find multiplication of first n natural numbers.

"""

n = int(input("Enter n: "))

prod = 1
for i in range(1, n+1):
    prod *= i

print("Product:", prod)
