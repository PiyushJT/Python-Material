"""

Write a program to build a simple Student Management
System using Object Oriented Programming in Python which can
perform the following operations:

accept-This method takes details from the user like name,
roll number, and marks for two different subjects.

display-This method displays the details of every student.

search-This method searches for a particular student
from the list of students. This method will ask the user for roll
number and then search according to the roll number

delete-This method deletes the record of a particular student with
a matching roll number.

update-This method updates the roll number of the student.
This method will ask for the old roll number and new roll
number. It will replace the old roll number with a new roll number.

The following instructions need to be considered while making a program.
1.Give class name as Student
2.Include methods name as accept, display, search, delete
and update. (1 mark for each correct method to be formed).
3.Also form constructor with __init__ () method (2 marks
for forming constructor).
4.2 marks for correct object prepared like after deletion
of one roll no of student it should update the list with new roll
no. and should display it.

"""


class Student:
    
    def __init__(self):
        self.records = []

    def accept(self, name, roll, marks1, marks2):
        self.records.append(
            {"name": name, "roll": roll, "marks1": marks1, "marks2": marks2}
        )

    def display(self):
        for rec in self.records:
            print(f"Name : {rec['name']}")
            print(f"RollNo : {rec['roll']}")
            print(f"Marks1 : {rec['marks1']}")
            print(f"Marks2 : {rec['marks2']}")
            print()

    def search(self, roll):
        
        for rec in self.records:
            if rec['roll'] == roll:
                return rec
        else:
            print("404 Student not found!")
            return None

    def delete(self, roll):
        for rec in self.records:
            if rec['roll'] == roll:
                self.records.remove(rec)

    def update(self, old_roll, new_roll):
        rec = self.search(old_roll)
        if rec:
            rec["roll"] = new_roll


# Demo usage with sample data
s = Student()
s.accept("A", 1, 100, 100)
s.accept("B", 2, 90, 90)
s.accept("C", 3, 80, 80)

print("List of Students")
s.display()

print("Student Found,")
found = s.search(2)
if found:
    print(f"Name : {found['name']}")
    print(f"RollNo : {found['roll']}")
    print(f"Marks1 : {found['marks1']}")
    print(f"Marks2 : {found['marks2']}")
    print()

s.delete(2)
print("List after deletion")
s.display()

s.update(3, 2)
print("List after updation")
s.display()

