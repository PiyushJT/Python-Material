"""

Write a Python program to find reverse of given number
using user defined function.

"""

def reverse_number(n):
    rev = 0
    temp = n
    while temp > 0:
        r = temp % 10
        rev = rev * 10 + r
        temp //= 10
    return rev


x = int(input("Enter number: "))
print("Reverse:", reverse_number(x))
