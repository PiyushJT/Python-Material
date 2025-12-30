"""

645.
Following is the provided numPy array. Return array of items by taking
the third column from all rows
sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])

646.
Return array of odd rows and even columns from below numpy array
sampleArray = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

"""

import numpy as np


print("645")
sampleArray = np.array(
    [
        [11 ,22, 33],
        [44, 55, 66],
        [77, 88, 99]
    ]
)

print(sampleArray[:, 2])




print("\n646")
sampleArray = np.array(
    [
        [3, 6, 9, 12],
        [15 ,18, 21, 24],
        [27 ,30, 33, 36],
        [39 ,42, 45, 48],
        [51 ,54, 57, 60]
    ]
)

print(sampleArray[::2, 1::2])


"""

645
[33 66 99]

646
[[ 6 12]
 [30 36]
 [54 60]]

"""