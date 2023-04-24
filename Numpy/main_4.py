"""asarray() function is used when you want to convert an input to an array. The input could be a lists, tuple, ndarray, etc.
numpy.asarray(data, dtype=None, order=None)[source]

data: Data that you want to convert to an array

dtype: This is an optional argument. If not specified, the data type is inferred from the input data

Order: Default is C which is an essential row style. Other option is F (Fortan-style)
"""
import numpy as np

a = np.matrix(np.ones((3,4)))
print(a)

np.array(a)[2] = 3
print(a)

""" Matrix is immutable. You can use asarray if you want to add modification in the original array."""
print("__________________________")
np.asarray(a)[0:3]=2     # np.asarray(A): converts the matrix A to an array
print(a)

"""
The arange() is an inbuilt numpy function that returns an ndarray object containing evenly spaced values within a defined interval.
"""

"""
Reshape Data
In some occasions, you need to reshape the data from wide to long. You can use the reshape function for this.

Syntax:

numpy.reshape(a, newShape, order='C')

a: Array that you want to reshape
newShape: The new desires shape
order: Default is C which is an essential row style.
"""

x = np.arange(5)
print("x:", x)
print("x+1:", x+1, end='\n\n')

y = np.random.uniform(size=(2,5))
print('y:', y, sep='\n')
print('y+1: ', y+1, sep='\n')

# Since x is shaped (5,) and y is shaped (2,5) we can do operations between them.

print(x*y)

# Without broadcasting we'd have to manually reshape our arrays
print(x.reshape(1,-1).repeat(2, axis=0) * y)