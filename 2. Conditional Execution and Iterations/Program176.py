"""

Print the following pattern using loop

*                   * 
* *               * * 
* * *           * * * 
* * * *       * * * * 
* * * * *   * * * * * 
* * * * * * * * * * * 
* * * * *   * * * * * 
* * * *       * * * * 
* * *           * * * 
* *               * * 
*                   * 

"""

num = int(input('Enter number:'))

for i in range(1,num):

    # First *s
    for j in range(0,i,1):
        print('* ',end="")

    # Spacing till middle
    for j in range(num,i,-1):
        print('  ',end="")
    
    # Spacing from middle
    for j in range(num,i+1,-1):
        print('  ',end="")

    # Last *s
    for j in range(0,i,1):
        print('* ',end="")

    # next line
    print()

# middle horizontal line with maximum *s
print((num*2-1)* "* ")

for i in range(1,num+1,1):

    # First *s
    for j in range(num,i,-1):
        print('* ',end="")

    # Spacing till middle
    for j in range(1,i+1,1):
        print('  ',end="")

    # Spacing from middle
    for j in range(1,i,1):
        print('  ',end="")

    # last *s
    for j in range(num,i,-1):
        print('* ',end="")
    
    # next line
    print()