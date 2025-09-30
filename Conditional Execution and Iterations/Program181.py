"""

Write a program that enters a single digit integer number
and produces all possible 6-digit numbers for which the product
of their digits is equal to the entered number.

Example: "number" → 2
•111112 → 1 * 1 * 1 * 1 * 1 * 2 = 2
•111121 → 1 * 1 * 1 * 1 * 2 * 1 = 2
•111211 → 1 * 1 * 1 * 2 * 1 * 1 = 2
•112111 → 1 * 1 * 2 * 1 * 1 * 1 = 2
•121111 → 1 * 2 * 1 * 1 * 1 * 1 = 2
•211111 → 2 * 1 * 1 * 1 * 1 * 1 = 2

"""

n = int(input('Enter a single digit number: '))
for i in range(100000, 1000000):
    m = 1
    for j in str(i):
        m *= int(j)
    if m == n:
        print(i)