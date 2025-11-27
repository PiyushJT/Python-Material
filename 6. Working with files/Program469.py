"""

Write a Python program to read a text file and do following:
1. Print no. of words 2. Print no. statements

"""

file = open('6. Working with files/data/friends.txt', 'r')
data = file.read()

words = data
word_trans = words.maketrans('', '', '!@#$%^&*()')
words = words.translate(word_trans)
words = words.split()

lines = data.split('\n')

print(f"No. of words: {len(words)}")
print(f"No. of lines: {len(lines)}")

file.close()