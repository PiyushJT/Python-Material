"""

Draw a pattern using a python program:
   *
  * *
 * * *
* * * *

"""

n = int(input()) +1

for i in range(n):    
    print(' '*(n-i), '* ' * i)