"""

Write a Python program to return another string similar
to the input string, but with its case inverted.
For example, input of “Mr. Ed” will result
in “mR. eD” as the output string.
Note: Use of built in swapcase function is prohibited. 

"""

st = input("enter the string ")

n = ''

for i in st:
    if i.isupper():
      n+= i.lower()
    else:
       n+= i.upper()

print(n)