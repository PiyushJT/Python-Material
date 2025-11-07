"""

Write Python Program to create a dictionary with the key as
the first character and value as a list of words starting with
that character.

"""

str = input("Enter string: ")

list = str.split()

dict = {}

for word in list:

    key = word[0]

    if key not in dict.keys():
        dict[key] = []
        
    dict[key].append(word)

print(dict)