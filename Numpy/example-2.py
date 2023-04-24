#  complex example of broadcasting with array reorganizing:

import numpy as np

# Creating a 4x3x2 array of random integers between 0-9
a = np.random.randint(0,10, size=(4,3,2))
print("Random generated Number: ", a)
print("------------------------")
b = np.ones((3,2))
print("Using Ones: ", b)
print("------------------------")
# element wise multiplication

"""
reshape method to reshape b into a 3-dimensional array of shape (1, 3, 2), 
which allows us to perform broadcasting along the first dimension of a. The result is stored in the array c, which also has shape (4, 3, 2)
"""
c = a * b.reshape((1,3,2))
print("Reshape Format: ", c)

# Print the result for the first element of a
print("Result for the first element of a:")
print("a[0]:\n", a[0])
print("b:\n", b)
print("c[0]:\n", c[0])
