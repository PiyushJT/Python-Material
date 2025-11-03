"""

Write a Python code which will return the sum of
the numbers of the list.
Return 0 for an empty list.
Except the number 13 is very unlucky, so it does
not count and number that come immediately after 13 also do not count
in sum.

"""

lst = [1, 13, 2, 3, 4]

was_13 = False
sum = 0

for i in lst:
    if i == 13:
        was_13 = True
        continue

    if was_13:
        was_13 = False
        continue

    sum += i

print("Sum is ", sum)
