"""

Write a python program to demonstrate the use of custom
exceptions in Exception handling.

"""




def isStringEmpty(a):
    if (type(a) != str):
        raise TypeError('a has to be string')

    if (not a):
        raise ValueError('a cannot be null')

    a.strip()

    if(a == ''):
        return False

    return True

try:
    a = 123
    print('isStringEmpty:', isStringEmpty(a))

except ValueError as e:
    print('ValueError raised:', e)
    
except TypeError as e:
    print('TypeError raised:', e)