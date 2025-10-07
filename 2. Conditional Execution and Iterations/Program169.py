"""

Draw a pattern using a python program:
   1
  2 2
 3 3 3
4 4 4 4

"""

n = int(input()) + 1

for i in range(1, n):
    print((n-i)*' ', end = '')
    for j in range(1, i+1):
        print(i, end = ' ')
    print()