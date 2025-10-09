"""

Create a pair of functions to convert Fahrenheit to Celsius and vice versa.
Where C = (F - 32) * (5/9) and F = C * (9/5) + 32.

"""

def to_celsius(f):
    return (f - 32.0) * (5.0/9.0)


def to_fahrenheit(c):
    return c * (9.0/5.0) + 32.0


choice = input("Enter unit (C/F): ").upper()
value = float(input("Enter value: "))

if choice == 'F':
    print(f"Celsius: {to_celsius(value)}")
elif choice == 'C':
    print(f"Fahrenheit: {to_fahrenheit(value)}")
else:
    print("Invalid input")
