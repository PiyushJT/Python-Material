"""

Write a Python program to calculate the sum of the positive
and negative numbers of a given list of numbers using
lambda function.

"""

numbers = [5, -3, 7, -2, 0, 9, -6]

# Using lambda and filter to separate positive and negative numbers
positive_sum = sum(filter(lambda x: x > 0, numbers))
negative_sum = sum(filter(lambda x: x < 0, numbers))

print("Sum of positive numbers:", positive_sum)
print("Sum of negative numbers:", negative_sum)
