"""

Draw a pattern using a python program:
   *
  # #
 * * *
# # # #

"""

n = int(input()) + 1


for i in range(n):
    print((n-i)*' ', end = '')
    if (i%2 == 1):
        print('* ' * i) 
    else:
        print('# ' * i)