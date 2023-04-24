import numpy as np

class Vector(object): # Base class for vectors
    def __init__(self, vec):
        """
        Constructor for Vector class
        :param vec: numpy array, vector
        """
        super(Vector, self).__init__()
        self.vec = vec
        print("vector: {}".format(self.vec))

    def perform_operation(self, vec2):
        """
        Abstract method for performing vector operations.
        :param vec2:  numpy array, result of the vector operation
        :return: numpy array, result of the victor operation
        """
        pass

class Addition(Vector): # Base class for vector addition
    def __init__(self, vec):
        """
        Constructor for addition class
        :param vec: numpy array, vector to be added
        """
        super(Addition, self).__init__(vec)
        print("Adding vector {}...".format(vec))

    def perform_operation(self, vec2):
        """
        Method to perform vector addition operation.
        :param vec2: numpy array, second vector to be added
        :return: numpy array, sum of the two vectors
        """
        return self.vec + vec2

class Subtraction(Vector): # Base Class for vector substraction
    def __init__(self, vec):
        """
        Constructor for Substraction class.
        :param vec: numpy array, vector to be subtracted
        """
        super(Subtraction, self).__init__(vec)
        print("Subtracting vector {}....".format(vec))

    def perform_operation(self, vec2):
        """
        Method to perform vector substraction operation.
        :param vec2: numpy array, second vector to be subtracted
        :return: numpy array, difference of the two vectors
        """
        return self.vec - vec2

class ScalarMultiplication(Vector):  # Base class for scalar multiplication
    def __init__(self, vec, scalar):
        """
        Constructor for ScalarMultiplication Class.
        :param vec: numpy array, vector to be multiplied
        :param scalar: float, scalar to multiply the vector
        """
        super(ScalarMultiplication, self).__init__(vec)
        self.scalar = scalar
        print("Multiplying vector {} by scaler {}..".format(vec, scalar))

    def perform_operation(self, vec2=None):
        """
        Method to perform scalar multiplication operation.
        :param vec2: None, not used in scaler multiplication
        :return: nympu array, result of scalar multiplication
        """
        return self.scalar * self.vec

class DotProduct(Vector):
    def __init__(self, vec):
        """
        Constructor for dot PRoduct class.
        :param vec: numpy array, vector to be dotted with
        """
        super(DotProduct, self).__init__(vec)
        print("calculating dot product with vector {}...".format(vec))

    def perform_operation(self, vec2):
        """
        Method to perform dot product operation.
        :param vec2: numpy array, second vector to be dotted with
        :return: float, dot product of the two vectors
        """
        return np.dot(self.vec, vec2)

class VectorOperations(Addition, Subtraction, ScalarMultiplication, DotProduct):
    def __init__(self, vec1, vec2=None, scalar=None):
        """
        Constructor for VectorOperation
        :param vec1: numpy array, first vector
        :param vec2: numpy array, second vector ()optional, required for additon
        :param scalar: float, scalar(optional, for multiplicaiton)
        """
        super(VectorOperations, self).__init__(vec1)
        if vec2 is not None:
            super(Addition, self).__init__(vec2)
            super(Subtraction, self).__init__(vec2, scalar)
        if scalar is not None:
            super(ScalarMultiplication, self).__init__(vec1)
        super(DotProduct, self).__init__(vec1)

        self.vec1 = vec1
        self.vec2 = vec2

        if vec2 is not None:
            self.addition = Addition(vec1)
            self.subtraction = Subtraction(vec1)
        if scalar is not None:
            self.scalar_multiplication = ScalarMultiplication(vec1, scalar)
        self.dot_product = DotProduct(vec1)

    # def __init__(self, vec1, vec2=None, scalar=None):

        """
        Constructor for VectorOperation
        :param vec1: numpy array, first vector
        :param vec2: numpy array, second vector ()optional, required for additon
        :param scalar: float, scalar(optional, for multiplicaiton)
        """
       # self.vec1 = vec1
       # self.vec2 = vec2
       # if vec2 is not None:
        #    self.addition = Addition(vec1)
         #   self.subtraction = Subtraction(vec1)
        # if scalar is not None:
          #  self.scalar_multiplication = ScalarMultiplication(vec1, scalar)
        # self.dot_product = DotProduct(vec1)

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