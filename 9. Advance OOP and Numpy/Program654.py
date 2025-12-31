"""

Write a python program to demonstrate the use of super() method to call the method of base class.

"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        # Use super() to call the constructor of the base class
        super().__init__(name, age)
        self.student_id = student_id
    
    def display(self):
        # Use super() to call the display method of the base class
        super().display()
        print(f"Student ID: {self.student_id}")


student = Student("John Doe", 20, "S12345")
print("Student Details:")
student.display()

"""

Student Details:
Name: John Doe
Age: 20
Student ID: S12345

"""