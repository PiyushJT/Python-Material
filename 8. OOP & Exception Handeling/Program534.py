"""

You own a pizzeria named Olly’s Pizzas and want to create a
Python program to handle the customers and revenue.
Create the following classes with the following methods:
Class Pizza containing
1.init method: to initialize the size (small, medium, large),
toppings (corn, tomato, onion, capsicum, mushroom, olives,
broccoli), cheese (mozzarella, feta, cheddar).
Note: One pizza can have only one size but many toppings and cheese. (1.5
marks)
Throw custom exceptions if the selects toppings or cheese
not available in lists given above. (1 mark)
2.price method: to calculate the prize of the pizza in
the following way:
small = 50, medium = 100, large = 200
Each topping costs 20 rupees extra, except broccoli, olives
and mushroom, which are exotic and so cost 50 rupees each.
Each type of cheese costs an extra 50 rupees. (1.5 marks)
Class Order containing
1.init method: to initialize the name, customerid of the
customer who placed the order (0.5 marks)
2.order method: to allow the customer to select pizzas
with choice of toppings and cheese (1 mark)
3.bill method: to generate details about each pizza
ordered by the customer and the total cost of the order. (2 marks)
*Note: A customer can get multiple pizzas in one order.
1.5 marks for creating appropriate objects of these classes and
writing correct output.

"""

from csv import Error
from math import cos


class Pizza:

    SIZES = {"small": 50, "medium": 100, "large": 200}
    TOPPINGS = {
        "corn": 20,
        "tomato": 20,
        "onion": 20,
        "capsicum": 20,
        "mushroom": 50,
        "olives": 50,
        "broccoli": 50,
    }
    CHEESE = {"mozzarella": 50, "feta": 50, "cheddar": 50}


    def __init__(self, size, toppings, cheese):
        size = size.lower()
        if size not in self.SIZES:
            raise Error(f"Invalid size: {size}")

        for t in toppings:
            if t not in self.TOPPINGS:
                raise Error("One or more toppings not available")

        for c in cheese:
            if c not in self.CHEESE:
                raise Error("Cheese selection not available")

        self.size = size
        self.toppings = toppings
        self.cheese = cheese

    def price(self):
        cost = self.SIZES[self.size]

        for t in self.toppings:
            cost += self.TOPPINGS[t]

        for c in self.cheese:
            cost += self.CHEESE[c]
            
        return cost

    def __str__(self):
        return (
            f"{self.size.title()} pizza | Toppings: {', '.join(self.toppings)} | "
            f"Cheese: {', '.join(self.cheese)} | Price: {self.price()}"
        )


class Order:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.pizzas = []

    def order(self, size, toppings, cheese):
        self.pizzas.append(Pizza(size, toppings, cheese))

    def bill(self):
        print(f"Bill for {self.name} (ID: {self.customer_id})")
        total = 0
        for idx, p in enumerate(self.pizzas, 1):
            print(f"{idx}. {p}")
            total += p.price()
        print(f"Total amount: {total}")
        return total


try:
    order = Order("Piyush", 101)
    order.order("medium", ["corn", "mushroom"], ["mozzarella"])
    order.order("large", ["tomato", "olives", "broccoli"], ["cheddar", "feta"])
    order.bill()
except Error as err:
    print(f"Order failed: {err}")