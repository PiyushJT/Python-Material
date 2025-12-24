"""

Create a class student with following member attributes: roll no,
name, age and total marks. Create suitable methods for
reading and printing member variables. Write a python program
to overload ‘==’ operator to print the details of students
having same marks.

"""

class Student:
    def __init__(self, roll_no, name, age, total_marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.total_marks = total_marks

    def __eq__(self, other):
        return self.total_marks == other.total_marks

    def __str__(self):
        return f"Roll No: {self.roll_no}, Name: {self.name}, Age: {self.age}, Total Marks: {self.total_marks}"

stud1 = Student(1, "John", 20, 90)
stud2 = Student(2, "Jane", 21, 90)

print(stud1 == stud2)
print(stud1)
print(stud2)

"""

True
Roll No: 1, Name: John, Age: 20, Total Marks: 90
Roll No: 2, Name: Jane, Age: 21, Total Marks: 90

"""