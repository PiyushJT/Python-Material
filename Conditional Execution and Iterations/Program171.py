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

# inputs
grade_level = input("Enter the grade_level (A,B,C,D,E or F): ")
city = int(input("Enter the city (1,2 or 3):"))

# data from the table
grade_to_basic_other = {
    "A": (60000.0, 8000.0),
    "B": (50000.0, 7000.0),
    "C": (40000.0, 6000.0),
    "D": (30000.0, 5000.0),
    "E": (20000.0, 4000.0),
    "F": (10000.0, 3000.0),
}

hra_factor_by_city = {1: 0.30, 2: 0.20, 3: 0.10}

PROFESSIONAL_TAX = 200.0
PROVIDENT_FUND_RATE = 0.11
DA_RATE = 0.50
TRANSPORT_ALLOWANCE = 900.0

# basic validation defaults (simple handling to keep consistent style)
if grade_level not in grade_to_basic_other:
    print("Invalid grade level")
else:
    if city not in hra_factor_by_city:
        print("Invalid city tier")
    else:
        basic_pay, other_allowances = grade_to_basic_other[grade_level]

        hra = hra_factor_by_city[city] * basic_pay
        da = DA_RATE * basic_pay
        pf = PROVIDENT_FUND_RATE * basic_pay

        gross_pay = (
            basic_pay
            + hra
            + da
            + other_allowances
            + TRANSPORT_ALLOWANCE
            - PROFESSIONAL_TAX
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


