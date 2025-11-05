"""

Write a Program to Print Longest Common Prefix from a
given list of strings. The longest common prefix for list of strings
is the common prefix (starting of string) between
all strings. For example, in the given list [“apple”, “ape”, “zebra”], there
is no common prefix because the 2 most dissimilar
strings of the list “ape” and “zebra” do not share any starting
characters. If there is no common prefix between
all strings in the list than return -1.

"""

words = ["python", "pythonprogramming", "pythonlist"]

# Edge-case: empty list -> no common prefix
if not words:
    print(-1)
    exit()

"""
Use the first word as the initial prefix. 
We'll compare characters
at each index i of this word with the character
at index i of all other words.
If any word is shorter than i or has a mismatch, we
stop and return the prefix up to i (or -1 if i == 0).
"""
prefix = words[0]

# index
i = 0
while i < len(prefix):

    for word in words[1:]:

        # If the current word is too short (i >= len(word)) or the
        # characters don't match, we've found the end of the common
        # prefix. Print the prefix up to i (if any) or -1.
        if i >= len(word) or word[i] != prefix[i]:
            
            # If i > 0, there is a non-empty prefix; otherwise print -1
            print(prefix[:i] if i > 0 else -1)
            exit()

    # No mismatch at index i — move to next character
    i += 1

# If we finish the loop, the entire first word is a common prefix
print(prefix)