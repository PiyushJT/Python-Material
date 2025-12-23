"""

Implement the following hierarchy . The Staff function has name and
salary as its data members, the derived class
Teaching has subject as its data member and the class NonTeaching
has department as its data member. The derived
class method overrides (extends) the methods of the base class.

⚠️ Staff function is actually Staff class

"""

class Staff:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Teaching(Staff):
    def __init__(self, name, salary, subject):
        super().__init__(name, salary)
        self.subject = subject

    def display(self):
        super().display()
        print(f"Subject: {self.subject}")

class NonTeaching(Staff):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")

staff = Staff("John Doe", 100000)
staff.display()

teaching = Teaching("Jane Doe", 100000, "Mathematics")
teaching.display()

non_teaching = NonTeaching("Jim Doe", 100000, "Human Resources")
non_teaching.display()

"""

Name: John Doe, Salary: 100000
Name: Jane Doe, Salary: 100000
Subject: Mathematics
Name: Jim Doe, Salary: 100000
Department: Human Resources

"""