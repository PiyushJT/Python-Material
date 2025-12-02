"""

Write a Python program to copy the contents of a file to another file.

"""


def copy(org_file):
    original = open(org_file, 'r')

    copied = open(org_file + '_copy', 'w')

    data = original.read()

    copied.write(data)
    copied.close()

    original.close()


copy("6. Working with files/data/Story.txt")