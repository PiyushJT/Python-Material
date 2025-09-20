"""

Draw a pattern using a python program:
*
# #
* * *
# # # #

"""

n = int(input()) + 1

for i in range(n):
    if (i%2 == 1):
        print('* ' * i) 
    else:
        print('# ' * i)