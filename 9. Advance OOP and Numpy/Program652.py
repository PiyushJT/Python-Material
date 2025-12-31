"""

Write a python program to create a Bus child class that inherits
from the Vehicle class. In Vehicle class vehicle name, mileage
and seatingcapacity as its data member. The default fare charge
of any vehicle is seating capacity * 100. If Vehicle is Bus instance,
we need to add an extra 10% on full fare as a maintenance charge. So
total fare for bus instance will become the
final amount = total fare + 10% of the total fare.

"""

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        total_fare = base_fare + (0.10 * base_fare)
        return total_fare


school_bus = Bus("School Volvo", 12, 50)
print(f"The bus seating capacity is {school_bus.capacity}. so, the final fare amount should be {int(school_bus.fare())}.")

car = Vehicle("Audi Q5", 18, 5)
print(f"The car seating capacity is {car.capacity}. so, the final fare amount should be {car.fare()}.")


"""

The bus seating capacity is 50. so, the final fare amount should be 5500.
The car seating capacity is 5. so, the final fare amount should be 500.

"""