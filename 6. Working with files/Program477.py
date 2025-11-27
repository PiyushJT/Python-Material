"""

Write a python program to extract a list of all four-letter
words that start and end with the same letter from a given text file.

"""

file = open('6. Working with files/data/some words.txt', 'r')

data = file.read()

words = data
word_trans = words.maketrans('', '', '!@#$%^&*()')
words = words.translate(word_trans)
words = words.split()

file.close()

list = []

for word in words:
    if len(word) == 4 and word[0] == word[-1]:
        list.append(word)

print(list)