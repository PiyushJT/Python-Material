"""

Write a Python Program to Find the Net Salary of Employee using Inheritance.
Create three Class Employee, Perks, NetSalary. Make an Employee class as an abstract class.
Employee class should have methods for following tasks.
- To get employee details like employee id, name and salary from user.
- To print the Employee details.
- return Salary.
- An abstract method emp_id.
Perks class should have methods for following tasks.
- To calculate DA, HRA, PF.
- To print the individual and total of Perks (DA+HRA-PF).
Netsalary class should have methods for following tasks.
- Calculate the total Salary after Perks.
- Print employee detail also prints DA, HRA, PF and net salary.
9
Note 1: DA-35%, HRA-17%, PF-12%
Note 2: It is compulsory to create objects and demonstrating the methods with Correct output.

"""

from abc import ABC, abstractmethod

class Employee(ABC):

    def display(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
    
    @abstractmethod
    def display(self):
        pass

class Perks(Employee):
    def __init__(self, emp_id, name, salary):

        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        
        self.DA = 0.35 * self.salary
        self.HRA = 0.17 * self.salary
        self.PF = 0.12 * self.salary

    def display(self):
        print(f"DA: {self.DA}")
        print(f"HRA: {self.HRA}")
        print(f"PF: {self.PF}")

    def get_total_perks(self):
        return self.DA + self.HRA - self.PF
    

class NetSalary:
    def __init__(self, perks):
        self.perks = perks
        
    def display(self):
        print(f"Employee ID: {self.perks.emp_id}")
        print(f"Name: {self.perks.name}")
        print(f"Basic Salary: {self.perks.salary}")

        self.perks.display()
        print(f"Total Salary: {self.perks.salary + self.perks.get_total_perks()}")

    
perks = Perks(1, "John", 25000)
net_salary = NetSalary(perks)
net_salary.display()


"""

Employee ID: 1
Name: John
Basic Salary: 25000
DA: 8750.0
HRA: 4250.0
PF: 3000.0
Total Salary: 35000.0

"""