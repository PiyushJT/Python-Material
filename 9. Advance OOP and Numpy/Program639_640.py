"""

639. Write a program to find the distance between two points in cartesian cordinate system

"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(a, b):
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5

    def slope(a, b):
        return (a.y - b.y) / (a.x - b.x)

p1 = Point(1, 2)
p2 = Point(3, 4)

distance = Point.distance(p1, p2)
print(f"The distance between the two points is: {distance}")

slope = Point.slope(p1, p2)
print(f"The slope between the two points is: {slope}")

"""

The distance between the two points is: 2.8284271247461903
The slope between the two points is: 1.0

"""