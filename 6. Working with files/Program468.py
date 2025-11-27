"""

Write a function display_oddLines() to display odd number line
 from the text file. Consider the following lines for the file
– friends.txt.
Friends are crazy, Friends are naughty !
Friends are honest, Friends are best !
Friends are like keygen, friends are like license key !
We are nothing without friends, Life is not possible without friends !

"""

def display_oddLines(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()
    
    for i in range(0, len(lines), 2):
        print(lines[i], end = '')

display_oddLines('6. Working with files/data/friends.txt')