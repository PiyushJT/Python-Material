"""

Write a program to compare two text files. If they are different,
give the line and column numbers 
in the files where the first difference occurs.

"""

file1 = open('6. Working with files/data/python1.txt', 'r')
file2 = open('6. Working with files/data/python2.txt', 'r')

lines1 = file1.readlines()
lines2 = file2.readlines()

file1.close()
file2.close()

line_num = 1
col_num = 1
found_difference = False

min_lines = min(len(lines1), len(lines2))

for i in range(min_lines):
    line1 = lines1[i]
    line2 = lines2[i]
    
    min_len = min(len(line1), len(line2))
    
    for j in range(min_len):
        if line1[j] != line2[j]:
            line_num = i + 1
            col_num = j + 1
            found_difference = True
            break
    
    if found_difference:
        break
    
    if len(line1) != len(line2):
        line_num = i + 1
        col_num = min_len + 1
        found_difference = True
        break

if not found_difference and len(lines1) != len(lines2):
    line_num = min_lines + 1
    col_num = 1
    found_difference = True

if found_difference:
    print(f"line number {line_num} colNo. {col_num}")
else:
    print("Files are identical.")
