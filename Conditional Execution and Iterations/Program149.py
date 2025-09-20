"""

Write a python program to read three numbers (a,b,c) and check how many
numbers between ‘a’ and ‘b’ are divisible by ‘c’. 

"""


a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a > b:
    a,b = b,a

sum = 0

for i in range(a, b+1):
    if i % c == 0:
        sum += 1
        
print(sum)