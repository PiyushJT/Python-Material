"""

Write a python program to check the validity of a Password.
Primary conditions for password validation:
1. Minimum 8 characters.
2. The alphabet must be between [a-z]
3. At least one alphabet should be of Upper Case [A-Z]
4. At least 1 number or digit between [0-9]
5. At least 1 character from [ _ or @ or $]

"""

l,u,d,s=0,0,0,0

st=(input("Enter the password :: "))

for i in st :
    if i.islower():
        l+=1
    elif i.isdigit():
        d+=1            
    elif i.isupper():
        u+=1
    elif i in "@_$" :
        s+=1

if l and d and u and s :
    print("valid password ")
else :
    print("invalid")  