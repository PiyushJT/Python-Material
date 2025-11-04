"""

Write a python program with user defined function
that reads the words from paragraph and stores them as keys in a
dictionary and count the frequency of it as a value .

"""

str = input("Enter paragraph: ").lower()

dict = {}

lst = str.split()

for word in lst:

    if word not in dict.keys():
        dict[word] = 0

    dict[word] += 1

print(dict)