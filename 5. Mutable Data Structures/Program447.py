"""

Write a Python Program using function to count number of strings
where the string length is 3 or more and the first and
last character are same from a given list of string.

"""

lst = ['abc','xyz','aba','2112','123451','12345']

count = 0

for i in lst:
    if len(i) >= 3:
        if i[0] == i[-1]:
            count += 1


print(count)