"""

Write a Python program to accept string/sentence from the user till the user enters "END". 
Each string/sentence entered by the user should be a newline in the file. 
Save all the lines in the file and display only those lines which begin with a capital letter.

"""

file = open('6. Working with files/data/user_input.txt', 'w')

while True:
    user_input = input("Enter Something (for quit enter END): ")
    if user_input == "END":
        break
    file.write(user_input + '\n')

file.close()

# Display lines starting with capital letter
file = open('6. Working with files/data/user_input.txt', 'r')

print("\nLines started with Capital Letters:")

for line in file:
    line = line.strip()
    
    if line and line[0].isupper():
        print(line)

file.close()
