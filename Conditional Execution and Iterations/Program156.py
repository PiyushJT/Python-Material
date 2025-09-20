"""

Write a program to check whether a number is Armstrong number or not

"""

n = int(input("Enter number: "))
t = n

digit = len(str(n))

sum = 0

while t != 0:
    r = t%10
    sum += r**digit
    t = int(t/10)
    
if sum == n:
    print(f"{n} is armstrong")
else:
    print(f"{n} is not armstrong")
    