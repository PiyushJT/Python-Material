"""

Write a python program to swap first and last digits of a number using loop.
(for example: input = 123456 then output=623451) 

"""

num = int(input("Enter the number: "))

num_digits = 0
temp_number = num

while temp_number > 0:
    temp_number //= 10
    num_digits += 1

# Swap the first and last digits only if there are more than one digit
if num_digits > 1:

    # Extract the first digit
    first_digit = num // (10 ** (num_digits - 1))

    # Extract the last digit
    last_digit = num % 10

    # Calculate the remaining digits between the first and last digits
    middle_digits = (num % (10 ** (num_digits - 1))) // 10

    # Construct the swapped number
    swapped_number = last_digit * (10 ** (num_digits - 1)) + middle_digits * 10 + first_digit

    print(swapped_number)