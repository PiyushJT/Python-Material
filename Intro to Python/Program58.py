"""

Write a Python program to find an integer exponent x such that a^x = n.

"""

a = int(input("Enter the base (a): "))
n = int(input("Enter the result (n): "))

x = 0
power = 1

while power < n:
    power = power * a
    x = x + 1

if power == n:
    print(x)
else:
    print("No integer exponent found")
