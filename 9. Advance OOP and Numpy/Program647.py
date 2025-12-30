"""

Sort following NumPy array
Case 1: Sort array by the second row
Case 2: Sort the array by the second column
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])

➡️ argsort() gives indices of sorted elements in ascending order

"""

import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

print("original")
print(sampleArray)


print("Case 1: Sort array by the second row")
sorted_indices = sampleArray[1, :].argsort()
print(sorted_indices)
print(sampleArray[:, sorted_indices])

print("Case 2: Sort the array by the second column")
sorted_indices = sampleArray[:, 1].argsort()
print(sorted_indices)
print(sampleArray[sorted_indices, :])


"""

original
[[34 43 73]
 [82 22 12]
 [53 94 66]]
Case 1: Sort array by the second row
[2 1 0]
[[73 43 34]
 [12 22 82]
 [66 94 53]]
Case 2: Sort the array by the second column
[1 0 2]
[[82 22 12]
 [34 43 73]
 [53 94 66]]

"""