"""

Write a program to check if year is a leap year or not (Nested If).

"""

year = int(input("Enter year: "))


if (year % 4 == 0):
    if((year % 100 != 0) or (year % 400 == 0)):
        print('Yes')
    else:
        print('No')
else:
    print('No')