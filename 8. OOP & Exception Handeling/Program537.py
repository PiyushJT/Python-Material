"""

Write a python program that has a class Point with attributes
as the x and y co-ordinates.
1.Add a method ‘distance from origin’ to class Point which
returns the distance of the given point from origin. The
equation is
2.Add a method ‘translate’ to class Point, which returns
a new position of point a er transla on
3.Add a method ‘reflect_x’ to class Point, which returns
a new point which is the reflec on of the point about the x-axis.
4.Add a method ‘distance’ to return distance of the given
point with respect to the other point. The formula for calcula ng
distance between A(x1,y1) and B(x2,y2) is

"""

from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return sqrt(self.x**2 + self.y**2)

    def translate(self, dx, dy):
        return Point(self.x + dx, self.y + dy)

    def reflect_x(self):
        return Point(self.x, -self.y)

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return f"({self.x}, {self.y})"



p = Point(1, 2)
print("Point:", p)
print("Distance from origin:", round(p.distance_from_origin(), 2))

p_translated = p.translate(1, 1)
print("Translated by (1,1):", p_translated)

p_reflected = p_translated.reflect_x()
print("Reflected about x-axis:", p_reflected)

other = Point(3, 4)
print("Distance between", p_reflected, "and", other, ":", round(p_reflected.distance(other), 2))