"""

Write a Python program to calculate surface volume and area of a cylinder.

"""

import math

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

pi = 3.14
pi = math.pi

volume = pi * radius * radius * height
surface_area = 2 * pi * radius * (radius + height)

print("The volume of the cylinder is: ", volume)
print("The surface area of the cylinder is: ", surface_area)
