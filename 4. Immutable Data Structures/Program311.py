"""

Write a Python programme that accepts a string and calculate the number of uppercase letters, lowercase letters and
number of digits.

"""

str = input("Enter a string: ")

upper = 0
lower = 0
digit = 0


for i in str:
    if i.isupper():
        upper += 1
    if i.islower():
        lower += 1
    if i.isdigit():
        digit += 1

print("Uppercase letters: ", upper)
print("Lowercase letters: ", lower)
print("Digits: ", digit)