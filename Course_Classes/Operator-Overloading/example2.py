class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Vector %d and %d" %(self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(22,33)
v2 = Vector(7,-9)
print(v1+v2)


#####################################

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "{0}, {1}".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

p1 = Point(45,34)
p2 = Point(425,90)

print(p1+p2)