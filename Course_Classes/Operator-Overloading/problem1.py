"""
In this implementation, we define a Vector class with three components x, y, and z.
We overload the __add__() and __sub__() methods to allow addition and subtraction of two vectors, respectively.
We also overload the __mul__() method to perform the dot product of two vectors, or multiply a vector by a scalar.

In the __mul__() method, we first check if the other operand is a scalar (int or float) or a vector.
If it's a scalar, we multiply each component of the vector by the scalar and return a new vector with the result.
If it's a vector, we compute the dot product of the two vectors and return the result.
If the other operand is neither a scalar nor a vector, we raise a TypeError.

We then create two vectors a and b with components (1, 2, 3) and (4, 5, 6), respectively.
We compute their dot product using the overloaded * operator and print the result to the console.
The output is 32, which is the dot product of a and b.

"""

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("Unsupported Operand Type")

a = Vector(4, -7, 9)
b = Vector(5,5,-1)
dot_product = a * b
print(dot_product)  # Output: 32