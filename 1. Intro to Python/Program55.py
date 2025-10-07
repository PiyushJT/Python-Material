"""

Write a python code to demonstrate calculator functionality.

"""

print("Simple Calculator")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = num1 + num2
print("Result:", result)
result = num1 - num2
print("Result:", result)
result = num1 * num2
print("Result:", result)
result = num1 / num2
print("Result:", result)