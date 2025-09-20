"""

Write a Python Program to calculate the sum of three given numbers,
if the values are equal then return thrice their sum. 

"""

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a == b == c:
    print((a+b+c)*3)
else:
    print(a+b+c)