"""

You need to create a class called Atm. It should have methods to
create the pin, to change the pin, to check balance, to
withdraw money, to deposit money. Also, you need to
create method called menu to choose from the above given
operations which you want to perform.
create_pin Method:
Ask user to enter the pin to create a new pin. Also ask
user to initialize the balance of your account.
change_pin Method:
Pin Validation is required before changing the pin.
If Pin entered is wrong then message should be displayed “Enter
correct pin”. if Pin is correct then update the Old Pin with New Pin.
check_balance Method:
Pin Validation is required for checking the balance.
It should display the current balance of account.
withdraw Method:
Pin Validation is required before withdrawing money.
 should ask user for amount to withdraw. It should also display
the insufficient fund message if withdraw amount is higher
than balance else balance should be updated after withdraw.
deposit Method:
after deposit.
Pin Validation is required before deposit of money. It
should ask user for amount to deposit. balance should be updated
After completion of every method it should ask for choice(menu() method) to perform new operation. If you don’t want
any operation to perform then you can choose choice of exit
to come out from the program

"""


class Atm:
    def __init__(self):
        self.pin = None
        self.balance = 0

    def _validate_pin(self, pin):
        return self.pin is not None and pin == self.pin

    def create_pin(self, pin, initial_balance=0):
        self.pin = pin
        self.balance = initial_balance
        print("PIN set. Account created.")

    def change_pin(self, old_pin, new_pin):
        if not self._validate_pin(old_pin):
            print("Enter correct pin")
            return
        self.pin = new_pin
        print("PIN updated.")

    def check_balance(self, pin):
        if not self._validate_pin(pin):
            print("Enter correct pin")
            return
        print(f"Balance: {self.balance}")

    def withdraw(self, pin, amount):
        if not self._validate_pin(pin):
            print("Enter correct pin")
            return
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
        print(f"Withdrawn {amount}. New balance: {self.balance}")

    def deposit(self, pin, amount):
        if not self._validate_pin(pin):
            print("Enter correct pin")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")



atm = Atm()
atm.create_pin("1234", 500)
atm.check_balance("1234")
atm.deposit("1234", 200)
atm.withdraw("1234", 100)
atm.change_pin("1234", "9999")
atm.check_balance("9999")