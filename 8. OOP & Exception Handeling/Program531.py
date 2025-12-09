"""

Write a python program to demonstrate the use of raise in Exception handling

"""


def safe_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Denominator must not be zero")
    return a / b


try:
    print(safe_divide(10, 2))
    print(safe_divide(5, 0))
    
except ZeroDivisionError as e:
    print(f"Exception caught: {e}")
