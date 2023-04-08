import numpy as np

x = np.arange(24).reshape(4,3,2)
print(x)

my_list = np.array(range(1,10))
print(my_list)

a = np.array([1,2,3,4,5])
print(a)
print(type(a))

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
my = np.array(my_matrix)
print(my)
print(my.dtype)
print(my.size)
print(my.shape)
print(my.ndim)
print(my.itemsize)
print(my.nbytes)


a = np.array([1, 2, 3])   # Create a 1d array
print(a)
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Indexing with 3 elements. Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # Create a 2d array
print(b)
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # matrix position intersection with row and column axis



x = np.array([[1, 2, 3,4,5], [5,6,7,8,9]], dtype=np.int64)   # Force a particular datatype
print(x.dtype)

print("_______________________________________________________________________________________")

import numpy as np

a = np.zeros((5,5))
print(a)

b = np.ones((2,4))
print(b)

c = np.full((2,2), 7)
print(c)

d = np.eye(2)
print(d)

e = np.random.random((5,3))
print(e)
