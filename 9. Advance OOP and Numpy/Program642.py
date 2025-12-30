"""

Write a program to create a class called Data having “value” as its data member.
Overload the (>) and the (<) operator for
the class. Instantiate the class and compare the objects using _lt_ and _gt_.

"""

class Data:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value
    
data1 = Data(10)
data2 = Data(20)

print(data1 < data2)
print(data1 > data2)

"""

True
False

"""