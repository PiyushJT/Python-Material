"""

d={"student0":'Student@0',"student1":'Student@11',"student2":'Student@121',
"student3":'Student@052',"student4":'Student@01278',"student5":'Student@0125',
Student6":'Student@042',
"student7":'Student@07800',"student8":'Student@012'}

Write a python program to update the password of any user given the above
dictionary(d) which stores the username as
the key of the dictionary and the username's password as the value of the dictionary.
print the updated dictionary and
print the username and password according to ascending order of password
length of the updated dictionary.
For the password updating of that username follow some instructions.
Give the three chances to user enter the correct username and password.
If the user does not enter the correct
username and password then display “enter correct password and username”.
if the user does not enter the correct
username and password in a given three chances then display “enter correct
password and username” and “try after 24h”
If the user enters the correct username and password in a given three chances.
Give the three chances to user enter a
new password to update the password of that username. If the user enters a
new password not follow the below format,
then display “follow the password format”.
if the user does not enter the password in a given format in a given three
chances, then display “follow the password format” and “try after 24h”
The check, of whether the new password format is correct or wrong makes
the user define a function. That user define a
function to return True or False for password valid or not. 
hat user define function return value used in this program for
new password validation.
oNew password must have the below format:
1. at least 1 number between 0 and 9
2. at least 1 upper letter (between a and z)
3. at least 1 lower letter (between A and Z)
4. at least 1 special character out of @$_
5. minimum length of the password is 8 and the maximum length is 15
6. Do not use space and other special characters. Only uses @$_
If the new password follows the format of the password in a given three chances.
then print the updated dictionary and
print the username and password according to ascending order of password
length of an updated dictionary. If the dictionary is not
updated then take the old dictionary

"""

d = {"student0":'Student@0', "student1":'Student@11',"student2":'Student@121',
"student3":'Student@052',"student4":'Student@01278',"student5":'Student@0125',
"Student6":'Student@042',
"student7":'Student@07800',"student8":'Student@012'}


username = ""
stored_password = ""

def is_login_valid(username, password):
    if d.get(username) == password:
        print("Correct Password")
        print("Login Successful")
        return True
    else:
        return False


def is_passowrd_valid(password):
    
    if not (len(password) >= 8 and len(password) <= 15):
        return False

    for i in password:
        if i.isdigit():
            break
    else:
        return False

    if password.isupper() or password.islower():
        return False

    for i in password:
        if i in "@$_":
            break
    else:
        return False

    return True


count = 0

while count < 3:
    username = input("Enter username: ")
    stored_password = input("Enter password: ")
    
    if not is_login_valid(username, stored_password):
        count += 1
        print("enter correct password and username")
    else:
        count = 0
        break
    
else:
    print("try after 24h")
    exit(1)


new_password = ""

while count < 3:
    new_password = input("Enter new Password: ")

    if not is_passowrd_valid(new_password):
        count += 1
        print("enter valid password: ")
    else:

        print("Valid Password")

        d[username] = new_password

        # sorting
        sorted_list = sorted(d.items(), key = lambda x: len(x[1]))

        d = {}

        for i in sorted_list:
            key = i[0]
            value = i[1]
            d[key] = value

        break


print(d)