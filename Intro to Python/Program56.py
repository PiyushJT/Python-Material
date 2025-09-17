"""

Write a python program to convert Days into Years, Months and Days. (Ex: if input of Days = 370 then output will be, years=1, months=0 and days = 5).

"""

total_days = int(input("Enter total number of days: "))

years = total_days // 365
remaining_days = total_days % 365

months = remaining_days // 30
days = remaining_days % 30

print("years=", years, ", months=", months, "and days =", days)