"""

Write a program to check if the input number is positive, negative or zero.

"""


num = int(input('Enter the number: '))

if num > 0:
    print("Number is Positive")
else:
    if num == 0:
        print("Number is Zero")
    else:
        print("Number is Negitive")