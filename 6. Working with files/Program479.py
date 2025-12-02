"""

Write a Python program to count words, characters, and spaces from a text file.

"""

file = open('6. Working with files/data/friends.txt', 'r')
content = file.read()
file.close()

space_count = content.count(' ')
words = content.split()
word_count = len(words)
char_count = len(content) - content.count("\n")

print(f"No of space: {space_count}")
print(f"No of word: {word_count}")
print(f"No of characters: {char_count}")
