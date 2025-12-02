"""

Write a Python program to reverse the content of a one file and
store it in second file and also convert content of second file 
into uppercase and store it in third file and also count number
of Vowels in third file and also print only 2nd line from
the content of third file.

"""


# Step 1: Read file1, reverse content and store in file2
file1 = open('6. Working with files/data/friends.txt', 'r')
file2 = open('6. Working with files/data/friends2.txt', 'w')

lines = file1.readlines()
file1.close()

reversed_lines = []
for line in lines:
    reversed_line = line.rstrip('\n')[::-1] + '\n'
    reversed_lines.append(reversed_line)
    file2.write(reversed_line)

file2.close()



# Step 2: Read file2, convert to uppercase and store in file3
file2 = open('6. Working with files/data/friends2.txt', 'r')
file3 = open('6. Working with files/data/friends3.txt', 'w')

uppercase_lines = []
for line in file2:
    uppercase_line = line.upper()
    uppercase_lines.append(uppercase_line)
    file3.write(uppercase_line)

file2.close()
file3.close()

# Step 3: Count vowels in file3
file3 = open('6. Working with files/data/friends3.txt', 'r')
content = file3.read()
file3.close()

vowels = 'AEIOUaeiou'
vowel_count = 0
for char in content:
    if char in vowels:
        vowel_count += 1

# Step 4: Print 2nd line from file3
file3 = open('6. Working with files/data/friends3.txt', 'r')
lines = file3.readlines()
file3.close()

# Output results
print("Output 1 (Reversed content, original case):")
for line in reversed_lines:
    print(line, end='')

print("\nOutput 2 (Reversed content, uppercase):")
for line in uppercase_lines:
    print(line, end='')

print(f"\nOutput 3 (Vowel count):")
print(f"Vowels = {vowel_count}")

print("\nOutput 4 (Only the 2nd line from the uppercase reversed content):")
if len(lines) >= 2:
    print(lines[1], end='')
else:
    print("File has less than 2 lines.")
