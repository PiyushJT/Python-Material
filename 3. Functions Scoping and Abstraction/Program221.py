"""

Write a Python program to find sum and average of first n natural numbers.

"""

n = int(input("Enter number: "))

s = 0
for i in range(1, n+1):
    s += i

avg = s / n if n > 0 else 0
print("Sum:", s)
print("Average:", avg)
