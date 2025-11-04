"""

Write a Python function to sum all the numbers in a list

"""

def sum_of_list(numbers):

    total = 0

    for num in numbers:
        total += num

    return total

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = sum_of_list(lst)

print(result)