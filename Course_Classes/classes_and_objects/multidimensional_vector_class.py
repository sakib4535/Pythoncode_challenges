class Vector:

    def __init__(self, d):
        """ Creating a d-dimensional vectors of zeroes """
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):   # relying on __len__ mehtod
            raise ValueError("Dimensions Must Agree to each other")
        result = Vector(len(self))  # starting with vector of zeroes
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return self._coords != other._coords

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

# create two vectors
v1 = Vector(4)
v2 = Vector(4)

# set values of the vectors
v1[0] = 5
v1[1] = -2
v1[2] = 0
v1[3] = 8

v2[0] = 1
v2[1] = 6
v2[2] = -9
v2[3] = 3
# add the vectors together
v3 = v1 + v2

# print the result
print(v3)
