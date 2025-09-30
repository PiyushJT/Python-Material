"""

Write a Python program that prompts the user to enter
numbers and stops only when the user enters “stop”. After this,
print the minimum even, maximum even, average of
even number, minimum odd, maximum odd, average of odd
number from among all the numbers entered by the user.
Note: You are not allowed to use any built-in
structures like lists, tuples, etc. or any built-in
functions like max, min, sum

Example: input and output
enter number or 'stop' for stop: -1
enter number or 'stop' for stop: -5
enter number or 'stop' for stop: 9
enter number or 'stop' for stop: 2
enter number or 'stop' for stop: 4
enter number or 'stop' for stop: 6
enter number or 'stop' for stop: stop
Output:
for even 6 2 4.0 (max, min, avg)
for odd 9 -5 1.0 (max, min, avg)

"""

print("Enter numbers. Type 'stop' to finish.")

# Even
even_min = 999999999
even_max = -999999999
even_sum = 0.0
even_count = 0

# Odd
odd_min = 999999999
odd_max = -999999999
odd_sum = 0.0
odd_count = 0

while True:
    inp = input("enter number or 'stop' for stop: ")

    if inp == 'stop':
        break

    n = int(inp)

    # even
    if n % 2 == 0:
        even_sum += n
        even_count += 1

        if n < even_min:
            even_min = n
        if n > even_max:
            even_max = n
    # odd
    else:
        odd_sum += n
        odd_count += 1
        if n < odd_min:
            odd_min = n
        if n > odd_max:
            odd_max = n


if even_count > 0:
    even_avg = even_sum / even_count
    print(f"for even {even_max} {even_min} {even_avg} (max, min, avg)")
else: 
    print("No even value")

if odd_count > 0:
    odd_avg = odd_sum / odd_count
    print(f"for odd {odd_max} {odd_min} {odd_avg} (max, min, avg)")
else:
    print("No odd value")


