"""

Write a function count_lines() to count and display the total number of lines from the file.
Consider the following lines for
the file – friends.txt.
Friends are crazy, Friends are naughty !
Friends are honest, Friends are best !
Friends are like keygen, friends are like license key !
We are nothing without friends, Life is not possible without friends !


"""


def count_lines(file_path):
    file = open(file_path, 'r')
    lines = file.readlines()

    return len(lines)

print(count_lines("6. Working with files/data/friends.txt"))