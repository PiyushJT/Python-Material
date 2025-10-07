"""

Write a Python program to convert Fahrenheit to Celsius and vice versa.

"""

print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
choice = input("Choose conversion (1/2): ")

if choice == "1":
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print("Temperature in Celsius: ", c)
elif choice == "2":
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9 / 5) + 32
    print("Temperature in Fahrenheit: ", f)
else:
    print("Invalid choice")
