"""

Write a Python program to check Armstrong number using user defined function.

"""

def is_armstrong(n):
    s = 0
    temp = n
    digits = len(str(n))
    while temp > 0:
        r = temp % 10
        s += r ** digits
        temp //= 10
    return s == n


x = int(input("Enter number: "))
print("Armstrong" if is_armstrong(x) else "Not Armstrong")
