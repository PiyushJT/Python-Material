"""

One of the ways to encrypt a string is by rearranging 
its characters by certain rules, they are broken up
by threes, fours or something larger.
For instance, in the case of threes,
the string ‘secret message’ would be broken into three groups.
The first group is sr sg, the characters at indices 0, 3, 6, 9 and 12.
The second group is eemse, the characters at indices 1, 4, 7,
10, and 13.
The last group is ctea, the characters at indices 2, 5, 8, and 11.
The encrypted message is sr sgeemsectea.
If the string ‘secret message’ would be broken into four groups.
The first group is seeg, the characters at indices 0, 4, 8
and 12.
The second group is etse, the characters at indices 1, 5, 9 and 13.
The third group is c s, the characters at indices
2, 6 and 10.
The fourth group is rma, the characters at indices 3, 7 and 11.
The encrypted message is seegetsec srma.

(A). Write a program that asks the user for a string,
and an integer determining whether to break things up by threes,
fours, or whatever user inputs.
Encrypt the string using above method.

⚠️ Output of (B) is wrong in example

(B). If you get a message which is encoded by the method above then,
Write a decryption program for the general case.
Taking input of any encrypted string from user
with key number used while breaking message apart during encryption.

(C). From the output string (Output Decrypted Message) of above
program (Part-B), create a Dictionary with Key as First
Character and Value as list of words Starting with that Character
from above string.
And print that dictionary by sorting it
based on the number of elements in a list of values in descending order.

Note: Consider capital and lower first character of words as
same character in this program. For ex. ‘Hi’ and ‘hello’ both
will be considered starting from ‘h’.

"""

import math

def encode(str, gap):
    
    encoded = ""
    for g in range(gap):
        encoded += str[g::gap]

    return encoded



def decode(str, gap):

    numCols = math.ceil(len(str) / gap)
    numRows = gap
    numShadedBoxes = (numCols * numRows) - len(str)
    plainText = [""] * numCols
    col = 0
    row = 0

    for symbol in str:
        plainText[col] += symbol
        col += 1

        if (
            (col == numCols)
            or (col == numCols - 1)
            and (row >= numRows - numShadedBoxes)
        ):
            col = 0
            row += 1

    return "".join(plainText)



def getDict(str):

    list = str.lower().split()
    dict = {}
 
    for word in list:
        key = word[0]
 
        if key not in dict.keys():
            dict[key] = []
        
        dict[key].append(word)

    sorted_list = sorted(dict.items(), key = lambda x: len(x[1]), reverse = True)

    dict = {}

    for i in sorted_list:
        key = i[0]
        value = i[1]
        dict[key] = value

    return dict




ch = input("1. Encrypt\n2. Decrypt\n3. Get Dictionary\nEnter your choice: ")

str = input("Enter the string: ")

if ch == '1':
    gap = int(input("Enter the gap: "))
    print(encode(str, gap))

elif ch == '2':
    gap = int(input("Enter the gap: "))
    print(decode(str, gap))

elif ch == '3':
    print(getDict(str))

else:
    print("Invalid choice.")