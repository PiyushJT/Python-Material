"""

Write a "pager" program. Your solution should prompt for a filename,
and display the text file 25 lines at a time, 
pausing each time to ask the user to enter the word "continue",
in order to show the next 25 lines or enter the word "stop" to close the file.

"""

filename = input("Enter the filename: ")

file = open("6. Working with files/data/" + filename, 'r')
lines = file.readlines()
file.close()

line_count = len(lines)
current_index = 0

while current_index < line_count:

    if current_index % 25 != 0 or current_index == 0:
        print(lines[current_index])

    else:

        inp = input("continue or stop: ").lower()

        if inp == 'continue':
            print("\n\nPrinting next lines\n")

        elif inp == 'stop':
            break

        else:
            print("invalid input")
            break

    
    current_index += 1