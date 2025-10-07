"""

Write a program to print prime numbers between given interval from user

"""

a = int(input("Enter start of range: "))
b = int(input("Enter end of range: "))

if a > b:
    a,b = b,a

for i in range(a, b+1):
    
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)