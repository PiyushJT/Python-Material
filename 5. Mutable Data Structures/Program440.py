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

(B). If you get a message which is encoded by the method above then,
Write a decryption program for the general case.
Taking input of any encrypted string from user
with key number used while breaking message apart during encryption.

"""

def encode(str, gap):
    
    encoded = ""
    for g in range(gap):
        encoded += str[g::gap]

    return encoded


# ⚠️ Baaki
def decode(str, gap):
    return str


ch = input("1. Encrypt\n2. Decrypt\nEnter your choice: ")

str = input("Enter the string: ")
gap = int(input("Enter the gap: "))

if ch == '1':
    print(encode(str, gap))

elif ch == '2':
    print(decode(str, gap))