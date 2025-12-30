"""

Write a NumPy array program to convert the values of Fahrenheit
degrees into Celsius degrees. The numpy array to be
considered is [0, 12, 45.21, 34, 99.91, 32] for Fahrenheit values.
Values are stored into a NumPy array. After converting the
following numpy array into Celsius, then sort the array and
find the position of 0.0 (means where 0.0 value is located i.e. it’s index)
Formula to convert value of Fahrenheit to Celsius is:
C=5*F/9 - 5*32/9

"""

import numpy as np

fahrenheit = np.array([0, 12, 45.21, 34, 99.91, 32])

celsius = (5/9) * (fahrenheit - 32)

print("Celsius:", celsius)
print("Sorted Celsius:", np.sort(celsius))

at = np.where(np.sort(celsius) == 0.0)

print("Index of 0.0 in sorted Celsius:", at)


"""

Celsius: [-17.77777778 -11.11111111   7.33888889   1.11111111  37.72777778
   0.        ]
Sorted Celsius: [-17.77777778 -11.11111111   0.           1.11111111   7.33888889
  37.72777778]
Index of 0.0 in sorted Celsius: (array([2]),)

"""