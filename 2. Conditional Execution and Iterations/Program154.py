"""

Write a program to take 10 values from keyboard using
loop and print their average on the screen

"""

sum = 0

for i in range(10):
    n = int(input(f"Enter the number {i+1}: "))
    sum += n

avg = sum / 10

print(f"Average is {avg}")