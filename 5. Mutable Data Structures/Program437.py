"""

Given a list of elements, write a python program to perform grouping
of similar elements, as different key-value list in
dictionary. Print the dictionary sorted in descending
order of frequency of the elements.
Note: To perform the sorting, use the sorted
function by converting the dictionary into a
list of tuples. After sorting,
convert the list of tuples back into a dictionary
and print it.

"""

lst = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]

dict = {}

for i in lst:

    if i not in dict.keys():
        dict[i] = []

    dict[i].append(i)

sorted_list = sorted(dict.items(), key = lambda x: len(x[1]), reverse = True)

sorted_dict = {}

for i in sorted_list:
    key = i[0]
    value = i[1]

    sorted_dict[key] = value

print(sorted_dict)
