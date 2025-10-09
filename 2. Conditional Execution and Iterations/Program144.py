"""

Write a Python Program to print all Happy Numbers between the given
range entered by user. (Include both Start and End Range Number).

"""


a = int(input("Enter start of range: "))
b = int(input("Enter end of range: "))

for i in range(a, b+1):
        
    j = i
    sum = 0;
    while j != 0:

        r = j%10
        j //= 10
        sum += r**2
        
        # if addition is done and sum is not single digit ->
        # redo with the same with sum
        if j==0 and sum > 9:
            j = sum
            sum = 0
    if sum==1:
        print(i, end = ' ')