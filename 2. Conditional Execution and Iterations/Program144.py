"""

Write a Python Program to print all Happy Numbers between the given
range entered by user. (Include both Start and End Range Number).

"""


a = int(input("Enter start of range: "))
b = int(input("Enter end of range: "))

if (a not in range(0, 100) or b not in range(0, 100)):
    print("Invalid range!")
else:
    for i in range(a, b+1):
        
        j = i
        sum = 0;
        while j != 0:
            
            r = j%10
            j = int(j/10)
            sum += r**2
            
            if sum > 9 and j==0:
                j = sum
                sum = 0
        if sum==1:
            print(i, end = ' ')