"""

Write a program to find the factorial of a number provided by the user.

"""

n = int(input("Enter number: "))

fact = 1

for i in range(1, n +1):
    fact *= i
    
print(fact)
