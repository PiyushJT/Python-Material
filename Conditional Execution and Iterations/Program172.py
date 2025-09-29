"""

Write a python program to print all numbers between 1 and 100
(including 1 and 100) that are both, Disarium and
Harshad numbers.

A number is said to be a Disarium number when the sum of
its digit raised to the power of their respective positions
becomes equal to the number itself.
For example, 175 is a Disarium number as follows:
11+ 72 + 53 = 1+ 49 + 125 = 175

A harshad number is a number that is divisible by the sum of
its digits. E.g., the number 18 is a harshad number, because
the sum of the digits 1 and 8 is 9 (1 + 8 = 9), and 18 is divisible by 9.

"""

for i in range(1, 101):
    j = i
    sum = 0
    
    while j != 0:
        leng = len(str(j))
        r = j%10
        sum += r ** leng
        j = int(j/10)
        
    # if it is dissarium, check for harshad
    if sum == i:
        
        sum = 0
        j = i

        while j != 0:

            r = j%10
            sum += r
            j = int(j/10)
            
        if i % sum == 0:
            print(i)

