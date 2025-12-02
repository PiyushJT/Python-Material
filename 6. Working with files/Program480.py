"""

File Filtering. Write all lines of a file1,
except those that start with a pound sign (#), 
the comment character for Python, to file2.
And display data of file2.

"""

file1 = open('6. Working with files/data/file1_with_comments.txt', 'r')
file2 = open('6. Working with files/data/file2_filtered.txt', 'w')

for line in file1:
    if not line.strip().startswith('#'):
        # Remove # and everything after it on the line
        if '#' in line:
            line = line[:line.index('#')].rstrip() + '\n'
        file2.write(line)

file1.close()
file2.close()

# Display data of file2
file2 = open('6. Working with files/data/file2_filtered.txt', 'r')
print(file2.read())
file2.close()
