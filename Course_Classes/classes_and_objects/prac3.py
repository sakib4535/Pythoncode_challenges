from sympy import Symbol, sympify

class FarePrice:
    def __init__(self, x, y, point):
        self.x = Symbol(x)
        self.y = Symbol(y)
        self.point = point

    def Point(self):
        return sympify(self.x**2 + self.y**2)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        sum_xy = x + y
        prod_xy = x * y
        return FarePrice(x, y, f"{self.point} + {other.point}"), sum_xy, prod_xy

obj1 = FarePrice('78', '98', "Point 1")
obj2 = FarePrice(23, 11, "Point 2")
obj3, sum_xy, prod_xy = obj1 + obj2

print(obj3.point)
print(obj3.Point())
print(f"Sum of x and y: {sum_xy}")
print(f"Product of x and y: {prod_xy}")
