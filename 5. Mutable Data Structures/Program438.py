"""

A digital image in a computer is represented by a pixels matrix.
Each image processing operation in a computer may be
observed as an operation on the image matrix. Suppose
you are given an N x N 2D matrix A (in the form of a list)
representing an image. Write a Python program to
rotate this image by 90 degrees (clockwise) by
rotating the matrix 90 degree clockwise.
Write proper code to take input
of N from the user and then to take input of an
N x N matrix from the
user. Rotate the matrix by 90 degree clockwise and
then print the rotated matrix.

Note: You are not allowed to use an extra iterable like list,
tuple, etc. to do this. You need to make changes in the given
list A itself. Your program should be able to handle any N x N
matrix from N = 1 to N = 20.

"""

def rotate_matrix(matrix):
    n = len(matrix)
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            # Swap elements across diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        left = 0
        right = n - 1
        while left < right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1

# Input matrix size
n = int(input("Enter N: "))

# Input matrix elements
matrix = []
print(f"\nEnter {n}x{n} matrix elements:")
for i in range(n):
    row = []
    for j in range(n):
        val = int(input(f"Enter element at position [{i}][{j}]: "))
        row.append(val)
    matrix.append(row)

# Print original matrix
print("\nOriginal Matrix:")
for row in matrix:
    print(row)

# Rotate the matrix
rotate_matrix(matrix)

# Print rotated matrix
print("\nMatrix after 90° clockwise rotation:")
for row in matrix:
    print(row)