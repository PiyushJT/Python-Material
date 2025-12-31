"""

Print max from axis 0 and min from axis 1 from the following 2-D array.
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])

"""

import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

arrX = sampleArray[:, 0]
arrY = sampleArray[0, :]

print(sampleArray)

print("Max from axis 0:", np.max(arrX))
print("Min from axis 1:", np.min(arrY))

"""

[[34 43 73]
 [82 22 12]
 [53 94 66]]
Max from axis 0: 82
Min from axis 1: 34

"""