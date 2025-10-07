"""

Write a program to implement the calculator for the date of Easter.
The following algorithm computes the date for Easter Sunday
for any year between 1900 to 2099.
Ask the user to enter a year. Compute the following:
1.a = year % 19
2.b = year % 4
3.c = year % 7
4.d = (19 * a + 24) % 30
5.e = (2 * b + 4 * c + 6 * d + 5) % 7
6.dateofeaster = 22 + d + e
Special note: The algorithm can give a date in April. You will know
that the date is in April if the calculation gives you an
answer greater than 31. (You’ll need to adjust) Also, if the year
is one of four special years (1954, 1981, 2049, or 2076)
then subtract 7 from the date.
Eg:
Input: Year : 2022
Expected Outcome: 2022-04-17 (i.e. 17th April 2022)

"""

year = int(input('Enter year (1900-2099): '))
a = year % 19
b = year % 4
c = year % 7
d = (19 * a + 24) % 30
e = (2 * b + 4 * c + 6 * d + 5) % 7
dateofeaster = 22 + d + e

# Special adjustment for years
special_years = [1954, 1981, 2049, 2076]
if year in special_years:
    dateofeaster -= 7

if dateofeaster > 31:
    # April
    print(f"Easter Sunday: {year}-04-{dateofeaster-31}")
else:
    # March
    print(f"Easter Sunday: {year}-03-{dateofeaster}")
