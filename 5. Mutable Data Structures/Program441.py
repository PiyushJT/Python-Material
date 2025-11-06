"""

Given a list L of size N. You need to count the number of
special elements in the given list. An element is special if removal
of that element makes the list balanced. The list will be
balanced if sum of even index elements is equal to the sum of odd
elements. Also print the updated lists after removal of special elements.

"""

def is_balanced(lst):
    sum_even = 0
    sum_odd = 0

    for i in range(len(lst)):
        if i % 2 == 0:
            sum_even += lst[i]
        else:
            sum_odd += lst[i]

    return sum_even == sum_odd


lst = [5, 5, 2, 5, 8]

ind = 0
count = 0

for i in lst:

    new_list = lst[:ind] + lst[ind+1:]

    if is_balanced(new_list):
        count += 1
        
        print(f"Original List: {lst}")
        print(f"Index to be removed: {ind}")
        print(f"List after removing index: {new_list}")
        print()

    ind += 1

print(f"Total number of special elements: {count}")