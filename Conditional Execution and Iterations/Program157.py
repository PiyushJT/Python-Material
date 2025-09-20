"""

Write a program to check if a number is prime or not

"""

n = int(input("Enter number: "))

for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not Prime")
        break
else:
    print(f"{n} is Prime")
