"""

Ask the user to enter 10 test scores. Write a program to do the following:

a)If user enters score greater than 100, then give warning to user that
  entered score is more than 100 and take that
input again from user.
b)Print out the highest and lowest scores.
c)Print out the average of the scores.
d)Print out the second largest score.
e)Drop the two lowest scores and print out the average of the rest of them.
Note: Use of Python Data structures like string, list, tuple etc. and their
inbuilt function is not allowed.

For Ex.
If Input is like following:
Enter Test Score: 80
Enter Test Score: 65
Enter Test Score: 98
Enter Test Score: 70
Enter Test Score: 93
Enter Test Score: 130
Entered score is more than hundred, so enter again
Enter Test Score: 95
Enter Test Score: 50
Enter Test Score: 40
Enter Test Score: 75
Enter Test Score: 72
Output should be:
Highest Score is: 98
Lowest Score is: 40
Average Test Score is: 73.8
Second Largest Score is: 95
Average after dropping the two lowest scores: 81.0

"""

totalNumbersAdded = 0
sum = 0

max = -1
secondMax = -1
lowest = 101
secondLowest = 101

while True:
    num = int(input("Enter the number: "))
    if num < 0 or num > 101:
        print("The number was invalid!")
        continue

    sum += num
    totalNumbersAdded += 1

    if num > max:
        max, secondMax = num, max
    elif num > secondMax:
        secondMax = num

    if num < lowest:
        lowest, secondLowest = num, lowest
    elif num < secondLowest:
        secondLowest = num

    if totalNumbersAdded == 10:
        break

print(f"Highest: {max}")
print(f"Lowest: {lowest}")
print(f"Average: {sum/10}")
print(f"Second Lowest: {secondLowest}")
print(f"Second Highest: {secondMax}")

print(f"Average after drop: {(sum - lowest - secondLowest)/8}")