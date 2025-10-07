"""

Write a python program that prompts the user to enter numbers and
stops only when the use enter “QUIT” . After this
print sum and average of the numbers, minimum and maximum number
from given numbers entered by user.
Note: you are not allowed to use any built in structures like,
list ,tuple etc. or any builtin function like min, max etc.
For Example: Input: 4,1,5,”QUIT”

Output:
Sum=10
Average=3.333
Minimum number=1
Maximum number=5

"""

print('Enter numbers one by one. Type QUIT to stop.')
sum = 0.0
count = 0
min = 99999999
max = -99999999

while True:

    inp = input('Enter number (or QUIT): ')

    if inp == 'QUIT':
        break

    num = float(inp)

    sum += num
    count += 1

    if num < min:
        min = num

    if num > max:
        max = num

if count == 0:
    print('No numbers entered.')
else:
    print(f'Sum = {sum}')
    print(f'Average =  {sum / count}')
    print(f'Minimum number = {min}')
    print(f'Maximum number = {max}')
