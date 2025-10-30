"""

Write a program to print sum of even numbers and sum of odd numbers from elements given in tuple.

"""

tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even = 0
odd = 0

for i in tp:
    if i % 2 == 0:
        even += i
    else:
        odd += i

print(f"Sum of even numbers: {even}")
print(f"Sum of odd numbers: {odd}")