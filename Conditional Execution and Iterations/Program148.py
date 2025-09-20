"""

Write a program to find average of first N natural numbers given by user.

"""



n = int(input("Enter the number: "))
sum = 0

if n < 0:
    print("Invalid Number!")
else:
    for i in range(n+1):
        sum += i
        
    print(sum / n)
    