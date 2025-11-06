"""

Write a python program to print all possible combinations
from the three Digits and also count unique values inside a list
and also find list product excluding duplicates and also
find sum of list’s elements excluding duplicates.

"""


lst = [1, 2, 3]

combinations = []

for i in range(3):

    for j in range(3):

        for k in range(3):

            if i != j and i != k and j != k:
                new_list = [lst[i], lst[j], lst[k]]

                if new_list not in combinations:
                    combinations.append(new_list)

print(combinations)

unique_list = set(lst)
sum = 0
prod = 1

for i in unique_list:
    sum += i
    prod *= i


print(f"uniques are {len(unique_list)}")
print(f"prod is {prod}")
print(f"sum is {sum}")