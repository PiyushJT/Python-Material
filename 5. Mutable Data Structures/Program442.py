"""

•Use appropriate comment lines to divide subprograms.
•Also demonstrate the program with one example test case.
(Example test input and output are given)

PART - A
Using map func on, write a Python program to convert
the given list into a tuple of strings.

PART - B
Write a Python program that multiply each number of
the given list with 10 using lambda func on.

PART - C
Write a Python program that mul ply all elements of
the given list using reduce func on and return the product.

PART - D
Write a Python program satisfying following conditions -
Create a python func on countchar()
that count the character of a string in a given
string without using inbuilt func ons.

Create a python func on findchar() that find the index of
first occurrence of a character in a given string without using
inbuilt functions. It should return -1 if it does
not find the character.

"""

from functools import reduce


lst = [1, 2, 3, 4]

# Part A
tpl = tuple(map(lambda x: str(x), lst))
print(tpl)

# Part B
tpl = tuple(map(lambda x: x * 10, lst))
print(tpl)

# Part C
prod = reduce(lambda x, y: x * y, lst)
print(prod)

# Part D
def countchar(str, char):
    count = 0

    for i in str:
        if i == char:
            count += 1

    return count

print(countchar("hello", "l"))

def findchar(str, char):

    ind = 0

    for i in str:
        if char == i:
            return ind
        ind += 1
    return -1

print(findchar('helloe', 'e'))