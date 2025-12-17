"""

Stacks and Queues. Write a class SQ that defines a data
structure that can behave as both a queue (FIFO) or a stack (LIFO),
There are five methods that should be implemented:
1.make a constructor with a valid parameter
2.shiftft() returns the first element and removes it from the list.
 Also, use the custom(raise) excep on in this method.
3.unshiftft() "pushes" a new element to the front or head of the list
4.push() adds a new element to the end of a list
5.pop() returns the last element and removes it from the list
6.remove() returns the maximum element of the list and removes it from the list.
7.Create the object and call all methods of the SQ class.

"""

class SQ():

    # Constructores
    def __init__(self, data):
        self.data = [data]
    
    def __init__(self):
        self.data = []

    def shift(self):
        frst = 0
        try:
            frst = self.data[0]
            self.data = self.data[1:]
        except:
            print("No Data found!")
        return frst

    def unshift(self, data):
        self.data.insert(0, data)

    def push(self, data):
        self.data.append(data)

    def pop(self):
        lst = 0
        try:
            lst = self.data.pop()
        except:
            print("Not enough data to pop")
        return lst

    def remove(self):
        mx = 0
        try:
            mx = max(self.data)
            self.data.remove(mx)
        except:
            print("Not enough data to remove")
        return mx

    def display(self):
        print(self.data)


lst = SQ()

lst.push(1)
lst.push(3)

lst.unshift(4)
print(lst.shift())

lst.push(5)
lst.push(6)

print(lst.remove())
print(lst.pop())

lst.display()