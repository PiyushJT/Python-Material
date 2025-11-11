"""

Write a Python program that accepts a list L of size N
from the user and reorders its elements in the following pattern:
[L[0], L[N-1], L[1], L[N-2], L[2], L[N-3], ...].
Note: You are not allowed to use any additional data
structures like lists, strings, or dictionaries.
The task must be accomplished by rearranging the elements of the original
list in-place,
without altering the values of the elements themselves.


Example:
Input list: [ 2, 4, 6, 8, 10]
Output: [ 2, 10, 4, 8, 6]
Input list: [10, 20, 30, 40]
Output: [ 10, 40, 20, 30]

"""

l = [2, 4, 6, 8, 10]

print(l)

for i in range(1,len(l)+1,2):
  l.insert(i,l.pop())
  
print(l)