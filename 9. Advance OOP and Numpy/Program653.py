"""

Create an abstract class named Shape.
Create an abstract method named calculate_area for the Shape class.
Create Two Classes named Rectangle and Circle which inherit Shape class.
Create calculate_area method in Rectangle class. It should return
the area of the rectangle object. (area of rectangle = (length * breadth))
Create calculate_area method in Circle class. It should return the area of the circle object.
(area of circle =πr^2))
Create objects of Rectangle and Circle class.
The python Program Should also check whether the area of one Rectangle object is greater
than another rectangle object by overloading > operator.
Execute the method resolution order of the Circle class.

"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.calculate_area() > other.calculate_area()
        return NotImplemented

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


rect1 = Rectangle(10, 5)
rect2 = Rectangle(5, 5)
circle = Circle(7)

print(f"Area of Rectangle 1 (10x5): {rect1.calculate_area()}")
print(f"Area of Rectangle 2 (5x5): {rect2.calculate_area()}")
print(f"Area of Circle (r=7): {circle.calculate_area():.2f}")

if rect1 > rect2:
    print("Rectangle 1 is greater than Rectangle 2")
else:
    print("Rectangle 1 is not greater than Rectangle 2")

print("\nMethod Resolution Order of Circle class:")
print(Circle.mro())

"""

Area of Rectangle 1 (10x5): 50
Area of Rectangle 2 (5x5): 25
Area of Circle (r=7): 153.94
Rectangle 1 is greater than Rectangle 2

Method Resolution Order of Circle class:
[<class '__main__.Circle'>, <class '__main__.Shape'>, <class 'abc.ABC'>, <class 'object'>]

"""