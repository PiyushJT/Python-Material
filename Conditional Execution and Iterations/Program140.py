"""

Write a program to determine a given number is ‘odd’ or ‘even’ and
print the following message “Number is ODD” or
“Number is Even”. 

"""

num = int(input('Enter the number: '))

if num % 2 == 1:
    print("Number is ODD")
else:
    print("Number is EVEN")