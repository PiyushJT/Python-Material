"""

Write a Python program to accept two numbers and check odd or even.

"""

def is_even(n):
    return n % 2 == 0


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("First is even" if is_even(a) else "First is odd")
print("Second is even" if is_even(b) else "Second is odd")
