"""

Program to demonstrate the issue of invoking __init__() in case of multiple inheritance

"""

class ClassA:
    def __init__(self):
        print("Initializing Class A")

class ClassB(ClassA):
    def __init__(self):
        print("Initializing Class B")
        ClassA.__init__(self)

class ClassC(ClassA):
    def __init__(self):
        print("Initializing Class C")
        ClassA.__init__(self)

class ClassD(ClassB, ClassC):
    def __init__(self):
        print("Initializing Class D")
        ClassB.__init__(self)
        ClassC.__init__(self)


print("--- Instantiating Class D ---")
d = ClassD()

"""

--- Instantiating Class D ---
Initializing Class D
Initializing Class B
Initializing Class A <-- First call
Initializing Class C
Initializing Class A <-- Second call (Duplicate call)

"""