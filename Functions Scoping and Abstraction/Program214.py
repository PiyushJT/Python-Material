"""

Write a Python function to check whether a number is in a given range.

"""

def in_range(num, low, high):
    return num in list(range(low, high+1))


x = int(input("Enter number: "))
l = int(input("Enter lower limit: "))
h = int(input("Enter upper limit: "))

print("In range:" if in_range(x, l, h) else "Not in range")
