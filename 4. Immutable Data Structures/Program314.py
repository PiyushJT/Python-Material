"""

Write a Python program to create a Caesar encryption.
Note: In cryptography, a Caesar cipher, also known as Caesar's
cipher, the shift cipher, Caesar's code or Caesar
shift, is one of the simplest and most widely known
encryption techniques. It is a type of substitution cipher in
which each letter in the plaintext is replaced by a letter
some fixed number of positions down the alphabet. For
example, with a right shift of 3, A would be replaced
by D, E would become H, and so on. The method is named
after Julius Caesar, who used it in his private correspondence.

"""

st = input("enter the text:")
key = int(input("enter the shift:"))
ans = ""

for ch in st :
    if ch.isupper():

        en = ord(ch)+key
        
        if en>90:
            en=(en%91)+65\
            
        ans=ans+chr(en)
        
    elif ch.islower():
         
         en = ord(ch)+key
         
         if en>123:
             en=(en%123)+97

         ans=ans+chr(en)

    else:
        ans+=ch

print(ans)