"""

Write a python program to demonstrate the use of try-except-else in Exception handling

"""


try:
    b = 10
    c = 2
    a = b/c
    print(a)
except:
    print('Exception raised')
else:
    print('no exceptions raised')