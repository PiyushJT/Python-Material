"""

Write a python program to read line by line from a given files file1 & file2 and write into file3.

"""

file1 = open('6. Working with files/data/friends.txt', 'r')
file2 = open('6. Working with files/data/city.txt', 'r')
file3 = open('6. Working with files/data/file3.txt', 'w')

for line in file1:
    file3.write(line)

for line in file2:
    file3.write(line)

file1.close()
file2.close()
file3.close()

print("Done!")
