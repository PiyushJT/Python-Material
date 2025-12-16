"""

Write a Python class named Student with two attributes
student_name, marks. Modify the attribute values of the said
class and print the original and modified values of the said attributes.

"""

class Student():

    def __init__(self, name, marks):
        self.student_name = name
        self.marks = marks
    
stud = Student("Piyush", 94)

print("Original")
print(stud.student_name)
print(stud.marks)

stud.student_name = "Piyush JT"
stud.marks = 95

print("Updated")
print(stud.student_name)
print(stud.marks)
