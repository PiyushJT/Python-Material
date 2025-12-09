"""

Write a Python class named Circle constructed by a
radius and two methods which will compute the area and the
perimeter of a circle.

"""

from math import pi


class Circle():

    radius = None

    def __init__(self, rad):
        self.radius = rad

    def get_area(self):
        return pi*(self.radius**2)

    def get_peri(self):
        return 2*pi*self.radius

circle = Circle(7)

print(circle.get_area())
print(circle.get_peri())