"""

Write a Python class named Rectangle constructed by a length and
width and a method which will compute the area of a rectangle.

"""

class Rectangle():
    
    def __init__(self, width, length):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

rect = Rectangle(4, 4)
print(rect.get_area())
