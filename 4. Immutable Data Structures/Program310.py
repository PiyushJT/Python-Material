"""

Write a Python program using function to shift the decimal digits
n places to the left, wrapping the extra digits around. If
shift > the number of digits of n, then reverse the string.

"""


def shift_decimal(str, shift):
    if shift > len(str):
        str = str[::-1]
    else:
        str = str[shift:] + str[:shift]

    return str


n = input("Enter a number: ")
shift = int(input("Enter number of places to shift: "))

print(shift_decimal(n, shift))