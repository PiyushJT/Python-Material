"""

Draw a pattern using a python program:
1
0 1
1 0 1
0 1 0 1

"""

n = int(input()) + 1

a = True

for i in range(n):
    
    for j in range(i):
        
        print(int(a), end = ' ')
        a = not(a)
        
    print()