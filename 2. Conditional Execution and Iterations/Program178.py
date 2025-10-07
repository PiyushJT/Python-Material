"""

Write a Python program to compute the greatest common divisor (GCD)
of two positive integers.
The greatest common divisor (GCD) of two nonzero integers a and b
is the greatest positive integer d such that d is a
divisor of both a and b; that is, there are integers e and f such
that a = de and b = df, and d is the largest such integer. The
GCD of a and b is generally denoted gcd(a, b).
For example, the greatest common factor of 15 and 10 is 5,
since both the numbers can be divided by 5.

"""

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

x = a
y = b
while y != 0:
    temp = y
    y = x % y
    x = temp
    
print(f"GCD of {a} and {b} is {x}")