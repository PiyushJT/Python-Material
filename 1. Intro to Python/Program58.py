"""

Write a Python program to find an integer exponent x such that a^x = n.

"""

a = int(input("Enter the base (a): "))
n = int(input("Enter the result (n): "))

v = a
p = 1

while p < n:

    if v == n:
        break
    if v > n:
        print("Invalid values for integer x")
        break

    v *= a
    p += 1

print(p)