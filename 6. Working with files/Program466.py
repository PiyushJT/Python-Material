"""

Write a python program to create and read the city.txt
file in one go and print the contents on the output screen.

"""

file = open('6. Working with files/data/city.txt', 'w+')
lines = file.read()
print(lines)
file.close()