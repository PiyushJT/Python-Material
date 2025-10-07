"""

Write a program to encode a number by changing the digits in the given
positive integer by user. The rule for changing
the digits in number will be:
If the digit in number is between 0 to 8 than replace the number with
1 to 9 respectively. (incrementing each digit by +1).
If the digit is 9, then replace it with 0.
To encode a number, replace digits in following manner:
For example:
Input: 31590218
Output: The number after encoding is: 42601329
For example:
Input: 9259
Output: The number after encoding is: 360
For example:
Input: 65217001
Output: The number after encoding is: 76328112
0 1
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 0
Note: Use of Python Data structures like string, list, tuple etc.
and their inbuilt function is not allowed.

"""

num = int(input("Enter the number: "))

encoded = 0
place = 1

while num > 0:
    digit = num % 10
    num = num // 10

    if digit == 9:
        new_digit = 0
    else:
        new_digit = digit + 1

    encoded = encoded + new_digit * place
    place = place * 10

print("The number after encoding is:", encoded)
