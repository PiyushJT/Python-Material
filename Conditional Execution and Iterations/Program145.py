"""

Write a Python Program to Compute the product of the odd
digits in a given number, 0 if there are not any
odd digits in a given number.

"""

n = int(input("Enter the number: "))

isOddFound = False

prod = 1;
while n != 0:

    r = n%10
    n = int(n/10)
    
    if r % 2 == 1:
        prod *= r
        isOddFound = True

if (not(isOddFound)):
    prod = 0
print(prod)