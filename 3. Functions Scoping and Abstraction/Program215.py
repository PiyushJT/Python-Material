"""

Write a Python function to display the Fibonacci sequence till the given n.

"""

def fibonacci(n):
    
    if n == 0:
        print("No terms to display")
    elif n == 1:
        print("0")
    elif n == 2:
        print("0 1")

    # For n >= 3
    else:
        a, b = 0, 1
        print(a, b, end = " ")
        for _ in range(2, n):
            c = a + b
            print(c, end = " ")
            a, b = b, c

n = int(input("Enter n: "))
fibonacci(n)

