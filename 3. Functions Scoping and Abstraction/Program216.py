"""

Write a Python function to find the Max of TWO numbers.

"""

def max_two(a, b):
    if a >= b:
        return a
    return b


x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print("Max is:", max_two(x, y))
