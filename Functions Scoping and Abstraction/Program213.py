"""

Write a Python function to calculate the factorial of a given number.

"""

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

n = int(input("Enter number: "))
ans = fact(n)
print(f"Factorial: {ans}")
