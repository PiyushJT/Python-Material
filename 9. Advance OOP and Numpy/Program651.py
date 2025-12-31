from abc import abstractmethod
"""

Imagine you own a call center. Use the following abstract class template to create
three more classes, Respondent, Manager, and Director that inherit this
Employee Abstract Class. from abc import ABC, abstractmethod

Create a program using the instructions given below:

1.Create a constructor in all three classes (Respondent, Manager and Director)
which takes the id and name as input and
initializes two additional variables, rank and free. rank should be equal
to 3 for Respondent, 2 for Manager and 1 for
Director. free should be a boolean variable with value True initially. (1 mark)

2.Implement rest of the methods in all three classes in the following way: (2 marks)
    a.receive_call(): prints the message, “call received by (name of the employee)”
    and sets the free variable to False.
    b.end_call(): prints the message, “call ended” and sets the free variable to True.
    c. is_free(): returns the value of the free variable
    d. get_rank(): returns the value of the rank variable

3.Create a class Call, with a constructor that accepts id and name of the caller
and initializes a variable called assigned to False. (0.5 marks)

4.Create a class CallHandler, with three lists, respondents, managers and
directors as class variables. (0.5 marks)

5.Create an add_employee() method in CallHandler class that allows you to
add an employee (an object of Respondent/Manager/Director) into one of
the above lists according to their rank. (1 mark)

6.Create a dispatch_call() method in CallHandler class that takes a
call object as a parameter. This method should find the first available
employee starting from rank 3, then rank 2 and then rank 1.
If a free employee is found, call its receive_call() function and change
the call’s assigned variable value to True. If no free employee is found, print the
message: “Sorry! All employees are currently busy.” (2 marks)

7.Create 3 Respondent objects, 2 Manager objects and 1 Director object
and add them into the list of available employees using the
CallHandler’s add_employee() method. (1 mark)

8.Create a Call object and demonstrate how it is assigned to an employee. (1 mark)

"""

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def receive_call(self):
        pass
    @abstractmethod
    def end_call(self):
        pass
    @abstractmethod
    def is_free(self):
        pass
    @abstractmethod
    def get_rank(self):
        pass

class Respondent(Employee):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.rank = 3
        self.free = True
        
    def receive_call(self):
        print(f"call received by {self.name}")
        self.free = False
        
    def end_call(self):
        print(f"call ended by {self.name}")
        self.free = True
            
    def is_free(self):
        return self.free
    
    def get_rank(self):
        return self.rank
    
class Manager(Employee):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.rank = 2
        self.free = True
        
    def receive_call(self):
        print(f"call received by {self.name}")
        self.free = False
        
    def end_call(self):
        print(f"call ended by {self.name}")
        self.free = True
        
    def is_free(self):
        return self.free
    
    def get_rank(self):
        return self.rank

class Director(Employee):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.rank = 1
        self.free = True
        
    def receive_call(self):
        print(f"call received by {self.name}")
        self.free = False
        
    def end_call(self):
        print(f"call ended by {self.name}")
        self.free = True
        
    def is_free(self):
        return self.free
    
    def get_rank(self):
        return self.rank

class Call:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.assigned = False

class CallHandler:
    respondents = []
    managers = []
    directors = []

    def add_employee(self, employee):
        rank = employee.get_rank()
        if rank == 3:
            self.respondents.append(employee)
        elif rank == 2:
            self.managers.append(employee)
        elif rank == 1:
            self.directors.append(employee)
    
    def dispatch_call(self, call):
        # Try to find a respondent
        for emp in self.respondents:
            if emp.is_free():
                emp.receive_call()
                call.assigned = True
                return
        
        # Try to find a manager
        for emp in self.managers:
            if emp.is_free():
                emp.receive_call()
                call.assigned = True
                return
        
        # Try to find a director
        for emp in self.directors:
            if emp.is_free():
                emp.receive_call()
                call.assigned = True
                return
        
        print("Sorry! All employees are currently busy.")


    # Create employees
r1 = Respondent(1, "Alice")
r2 = Respondent(2, "Bob")
r3 = Respondent(3, "Charlie")
    
m1 = Manager(4, "David")
m2 = Manager(5, "Eve")
    
d1 = Director(6, "Frank")
    
# Create handler and add employees
handler = CallHandler()
handler.add_employee(r1)
handler.add_employee(r2)
handler.add_employee(r3)
handler.add_employee(m1)
handler.add_employee(m2)
handler.add_employee(d1)
    
# Create a call and dispatch it
call1 = Call(101, "John Doe")
print(f"Dispatching call from {call1.name}...")
handler.dispatch_call(call1)
    
# Let's test if the first respondent is busy now
print(f"Is {r1.name} free? {r1.is_free()}")
    
# Dispatch another call
call2 = Call(102, "Jane Smith")
print(f"Dispatching call from {call2.name}...")
handler.dispatch_call(call2)

# Dispatch more calls to test escalation
call3 = Call(103, "Caller 3")
handler.dispatch_call(call3)
call4 = Call(104, "Caller 4")
handler.dispatch_call(call4) # Should go to Manager
    
# Verify manager received it
print(f"Is {m1.name} free? {m1.is_free()}")

m1.end_call()
print(f"Is {m1.name} free? {m1.is_free()}")

"""

Dispatching call from John Doe...
call received by Alice
Is Alice free? False
Dispatching call from Jane Smith...
call received by Bob
call received by Charlie
call received by David
Is David free? False
call ended by David
Is David free? True

"""
