"""

Write a Python function that accepts a string and calculate the number of
uppercase letters and lowercase letters.

"""

str = input("Enter The string: ")

upper_count = 0
lower_count = 0

for char in str:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
