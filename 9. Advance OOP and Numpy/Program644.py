"""

Create a 5X2 integer array from a range between 100 to 200 such that
the difference between each element is 10

"""

import numpy as np

lst = []

for i in range(100, 200, 10):
    lst.append(i)

arr = np.array(lst)
arr = arr.reshape(5, 2)

print(arr)

"""

[[100 110]
 [120 130]
 [140 150]
 [160 170]
 [180 190]]

"""