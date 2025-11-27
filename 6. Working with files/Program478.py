"""

Write a python program to read a text file “Story.txt”
and print only word starting with ‘I’ in reverse order.
Example: If value in text file is : ‘INDIA IS MY COUNTRY’
Output will be: ‘AIDNI SI MY COUNTRY’

"""

file =  open('6. Working with files/data/Story.txt', 'r')
data = file.read()

words = data.split()

file.close()

for word in words:
    if word[0] == 'I':
        print(word[::-1], end = ' ')
    else:
        print(word, end = ' ')