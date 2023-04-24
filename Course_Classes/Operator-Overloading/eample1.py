""" Simulates a point in 2D coordinate System """

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(23,34)
p2 = Point(10,20)
p3 = p1 + p2
print(p3.x, p3.y)

# Example 2:

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(400)
b2 = Book(200)
print("Total Number of pages ", b1+b2)
    



