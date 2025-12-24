"""

637. Write a program that overload the + operator so that it can add two object of class fraction 

638. Write a program that overload the * operator so that it can add two object of class fraction

"""

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)


    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)


    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

print(f1 + f2)
print(f1 * f2)

"""

5/6
1/6

"""