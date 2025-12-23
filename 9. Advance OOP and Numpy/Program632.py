"""

Implement the following hierarchy . The Book function has name,
n (number of authors), authors (list of authors),
publisher, ISBN, and year as its data members and the derived
class has course as its data member. The derived class
method overrides (extends) the methods of the base
class.

⚠️ Book function is actually Book class

"""


class Book:

    def set_data(self, name, n, authors, publisher, ISBN, year):
        self.name = name
        self.n = n
        self.authors = authors
        self.publisher = publisher
        self.ISBN = ISBN
        self.year = year

    def print_data(self):
        print("\n\n")
        print(f"Name: {self.name}")
        print(f"Number of authors: {self.n}")
        print(f"Authors: {self.authors}")
        print(f"Publisher: {self.publisher}")
        print(f"ISBN: {self.ISBN}")
        print(f"Year: {self.year}")


class Course(Book):

    def set_data(self, name, n, authors, publisher, ISBN, year, course):
        super().set_data(name, n, authors, publisher, ISBN, year)
        self.course = course

    def print_data(self):
        super().print_data()
        print(f"Course: {self.course}")



book = Book()
book.set_data("Python Programming", 3, ["John Doe", "Jane Doe", "Jim Doe"], "Python Publishing", "1234567890", 2024)
book.print_data()

course = Course()
course.set_data("Python Programming", 3, ["John Doe", "Jane Doe", "Jim Doe"], "Python Publishing", "1234567890", 2024, "Python Programming")
course.print_data()


"""


Name: Python Programming
Number of authors: 3
Authors: ['John Doe', 'Jane Doe', 'Jim Doe']
Publisher: Python Publishing
ISBN: 1234567890
Year: 2024



Name: Python Programming
Number of authors: 3
Authors: ['John Doe', 'Jane Doe', 'Jim Doe']
Publisher: Python Publishing
ISBN: 1234567890
Year: 2024
Course: Python Programming

"""