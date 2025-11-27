"""

Write a function cust_data() to ask user to enter their
names and age to store data in customer.txt file.

"""

def cust_data():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    file = open('6. Working with files/data/customer.txt', 'a')
    file.write(name + ' ' + age + '\n')
    file.close()

    print("Done!")

cust_data()