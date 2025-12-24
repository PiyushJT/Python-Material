"""

Write program that has a class point. Define another class location
which has two objects (Location and Destination) of class point.
Also define function in Location that prints reflection of Destination on the x axis.

"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Location:
    def __init__(self, location, destination):
        self.location = location
        self.destination = destination

    def reflect_x(self):
        return Point(self.destination.x, -self.destination.y)

location = Location(Point(1, 2), Point(3, 4))
print(location.reflect_x())

"""

(3, -4)

"""