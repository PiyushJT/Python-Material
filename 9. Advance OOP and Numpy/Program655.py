"""
Create a class called Matrix containing constructor that initialized the number of rows and number of columns of a new
Matrix object.
"""

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # Initialize a zero matrix
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def display(self):
        for row in self.data:
            print(row)

if __name__ == "__main__":
    rows = 3
    cols = 4
    matrix = Matrix(rows, cols)
    print(f"Created a matrix with {rows} rows and {cols} columns:")
    matrix.display()
