"""

Write a python program that has class store which keeps
record of code and price of each product. Display a menu of all
products to the user and prompt him to enter the
quantity of each item required. generate a bill and display total amount.


"""

class Store:
    def __init__(self):
        self.catalog = {}

    def add_item(self, code, price):
        self.catalog[code] = price

    def bill(self, quantities):
        total = 0
        print("*************** Bill ****************")
        print("ITEM\tPRICE\tQUANTITY\tSUBTOTAL")

        for code, qty in quantities.items():
            price = self.catalog.get(code, 0)
            sub = price * qty
            total += sub
            print(f"{code}\t{price}\t{qty}\t{sub}")

        print("*************************************")
        print(f"Total = {total}")


store = Store()
store.add_item("milk", 30)
store.add_item("apple", 35)
store.add_item("gems", 40)

quantities = {"milk": 2, "apple": 3, "gems": 4}
store.bill(quantities)
