"""

Write a program to reverse a number.

"""

n = int(input("Enter number: "))

sum = 0

while n != 0:
    r = n%10
    sum = sum*10 + r
    n = int(n/10)
    
print(sum)