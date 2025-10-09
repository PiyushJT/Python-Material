"""

Gross Pay, Annual Income and Income Tax Calculator
Write a Python Program to make the gross pay, annual income
and income tax calculator using following data.
The gross pay consists of Basic Pay, House Rent
Allowance (hra), Dearness Allowance (dra), other allowances and
professional tax and provident fund.
Gross Pay= Basic Pay+ House Rent Allowance (hra) + Dearness
Allowance (dra) +other allowances +Transport Allowance
(TA)– Professional tax –Employees’ Provident fund (EPF)
Basic Pay for different grade levels are indicated in table given.
The Professional tax remains constant and that is equal
to 200 Rs. for each grade levels and each month.
House Rent Allowance (hra) varies as per the city- For Class 1
Cities it is 0.3 times of Basic Pay of each grade levels, for
Class 2 Cities it is 0.2 times of Basic Pay of each grade levels,
for Class 3 Cities it is 0.1 times of Basic Pay of each grade
levels,
Dearness Allowance (dra)= 0.5 times of Basic Pay of each grade
levels, Other allowances are given in table which varies
according to different grade levels, Provident Fund= 0.11
times of Basic Pay for each grade levels, Transport Allowance
remains constant as 900 Rs. for each levels.
For different grade pays:


The gross pay calculated is only for one month.
After calculating Gross Pay of each employee calculate the
annual pay for employee by multiplying gross pay calculated,
by 12.
So, Annual Pay of an employee=Gross Pay of an employee*12
From Annual Pay of an Employee Calculate the income tax as
per the slabs of India Income Tax 2022-23 given below.
Tax Slabs for AY 2022-23

Input & Output:
Enter the grade_level (A,B,C,D,E or F:)A
city 1 is a tier 1 (metro), city 2 is tier 2 and city 3 is tier 3
Enter the city (1,2 or 3)1
Gross Pay of an Employee is: 110100.0
Annual income of an employee is: 1321200.0
Income Tax to be paid by an employee is: 142800.0

"""


# constants
professionalTax = 200.0
providentFundRate = 0.11
daRate = 0.50
transportAllowance = 900.0

# inputs
grade_level = input("Enter the grade_level (A,B,C,D,E or F): ")
city = int(input("Enter the city (1,2 or 3):"))

basic = 0
other = 0

if grade_level == "A":
    basic = 60000.0
    other = 8000.0
elif grade_level == "B":
    basic = 50000.0
    other = 7000.0
elif grade_level == "C":
    basic = 40000.0
    other = 6000.0
elif grade_level == "D":
    basic = 30000.0
    other = 5000.0
elif grade_level == "E":
    basic = 20000.0
    other = 4000.0
elif grade_level == "F":
    basic = 10000.0
    other = 3000.0
else:
    print("Invalid grade level")


hra = 0

if city == 1:
    hra = 0.30 * basic
elif city == 2:
    hra = 0.20 * basic
elif city == 3:
    hra = 0.10 * basic
else:
    print("Invalid city tier")


if basic == 0 or other == 0:
    print("Invalid grade or city level")
else:

    da = daRate * basic
    pf = providentFundRate * basic

    gross_pay = (
        basic
        + hra
        + da
        + other
        + transportAllowance
        - professionalTax
        - pf
    )

    annual_income = gross_pay * 12

    # income tax calculation as per slabs
    ai = annual_income
    tax = 0.0

    if ai <= 250000:
        tax = 0.0
    elif ai <= 500000:
        tax = (ai - 250000) * 0.05
    elif ai <= 750000:
        tax = 12500 + (ai - 500000) * 0.10
    elif ai <= 1000000:
        tax = 37500 + 12500 + (ai - 750000) * 0.15  # 37,500 already includes 5%*2.5L
    elif ai <= 1250000:
            tax = 75000 + 37500 + 12500 + (ai - 1000000) * 0.20
    elif ai <= 1500000:
        tax = 125000 + (ai - 1250000) * 0.25
    else:
        tax = 187500 + (ai - 1500000) * 0.30

    print("Gross Pay of an Employee is:", gross_pay)
    print("Annual income of an employee is:", annual_income)
    print("Income Tax to be paid by an employee is:", tax)
