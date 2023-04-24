import numpy as np


class Vector(object):
    def __init__(self, vec):
        super(Vector, self).__init__()
        self.vec = vec
        print("vector: {}".format(self.vec))

    def perform_operation(self, vec2):
        pass


class Addition(Vector):
    def __init__(self, vec):
        super(Addition, self).__init__(vec)
        print("Adding vector {}...".format(vec))

    def perform_operation(self, vec2):
        return self.vec + vec2


class Subtraction(Vector):
    def __init__(self, vec):
        super(Subtraction, self).__init__(vec)
        print("Subtracting vector {}....".format(vec))

    def perform_operation(self, vec2):
        return self.vec - vec2


class ScalarMultiplication(Vector):
    def __init__(self, vec, scalar):
        super(ScalarMultiplication, self).__init__(vec)
        self.scalar = scalar
        print("Multiplying vector {} by scaler {}..".format(vec, scalar))

    def perform_operation(self, vec2=None):
        return self.scalar * self.vec


class DotProduct(Vector):
    def __init__(self, vec):
        super(DotProduct, self).__init__(vec)
        print("calculating dot product with vector {}...".format(vec))

    def perform_operation(self, vec2):
        return np.dot(self.vec, vec2)


class VectorOperations(Addition, Subtraction, ScalarMultiplication, DotProduct):
    def __init__(self, vec1, vec2=None, scalar=None):
        super(VectorOperations, self).__init__(vec1)

        self.vec1 = vec1
        self.vec2 = vec2

        self.addition = None
        self.subtraction = None
        self.scalar_multiplication = None
        self.dot_product = None

        if vec2 is not None:
            self.addition = Addition(vec1)
            self.subtraction = Subtraction(vec1)
        if scalar is not None:
            self.scalar_multiplication = ScalarMultiplication(vec1, scalar)
        if vec2 is not None:
            self.dot_product = DotProduct(vec1)

    def perform_operation(self, vec2=None):
        if self.addition is not None and vec2 is not None:
            return self.addition.perform_operation(vec2)
        if self.subtraction is not None and vec2 is not None:
            return self.subtraction.perform_operation(vec2)
        if self.scalar_multiplication is not None and vec2 is None:
            return self.scalar_multiplication.perform_operation()
        if self.dot_product is not None and vec2 is not None:
            return self.dot_product.perform_operation(vec2)


# create a vector object
vec1 = Vector([1, 2, 3])

# create a vector operations object for vector addition
vec_addition = VectorOperations([4, 5, 6], vec2=vec1)
result = vec_addition.perform_operation(vec1)
print(result)  # prints [5 7 9]

# create a vector operations object for scalar multiplication
vec_scalar_mult = VectorOperations([4, 5, 6], scalar=2)
result = vec_scalar_mult.perform_operation()
print(result)  # prints [ 8 10 12]

# create a vector operations object for dot product
vec_dot_product = VectorOperations([1, 2, 3], vec2=[4, 5, 6])
result = vec_dot_product.perform_operation([4, 5, 6])
print(result)  # prints 32

