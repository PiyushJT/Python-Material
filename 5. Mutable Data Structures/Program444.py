"""

Create a python program which takes password as input and a
function which checks whether the given password is valid
or not under following conditions without using the
RegEx module in Python language.

Conditions required for a valid password:
1.Password strength should be at least 8 characters long
2.Password should contain at least one uppercase and
  one lowercase character.
3.Password must have at least one number.

"""

def validity1(pas):
    return len(pas) >= 8

def validity2(pas):
    return not(pas.islower()) and not(pas.isupper())

def validity3(pas):
    for i in pas:
        if i.isdigit():
            return True

    return False

password = input("Enter the password: ")

if validity1(password):
    if validity2(password):
        if validity3(password):
            print("Password is valid")
        else:
            print("Number missing")
    else:
        print("Both upper and lower case required")
else:
    print("Min 8 chars required")