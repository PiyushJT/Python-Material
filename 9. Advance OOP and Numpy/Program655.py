"""

Create a class called Matrix containing constructor that initialized 
the number of rows and number of columns of a new Matrix object.

"""

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

rows = 3
cols = 4
matrix = Matrix(rows, cols)
