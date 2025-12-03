"""

Write a python program to make a module named cal.py which
contain all the basic functions related to calculator 
like addition, subtraction, multiplication, and division
import that module in another file and use that functions 
with number inputs given by user.

"""

from modules import cal

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print(cal.addition(num1, num2))

print(cal.subtraction(num1, num2))

print(cal.multiplication(num1, num2))

print(cal.division(num1, num2))