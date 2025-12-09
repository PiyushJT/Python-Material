"""

Bank Account class:
Create a Python class called BankAccount which represents a bank account,
having as attributes: accountNumber (numeric type), name
(name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method which manages withdrawals actions.
Create a display() method to display account details.
Give the complete code for the BankAccount class.
Create the object and call all methods of the BankAccount class.

"""


class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. Balance: {self.balance}")

    def display(self):
        print(f"Account: {self.account_number}")
        print(f"Name   : {self.name}")
        print(f"Balance: {self.balance}")


acc = BankAccount(1001, "Piyush", 1000)
acc.display()
acc.deposit(500)
acc.withdrawal(300)
acc.display()