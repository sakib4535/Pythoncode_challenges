"""
A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers.
The number of dimensions is the rank of the array; the shape of an array is a tuple of integers giving the size
of the array along each dimension.

"""

import numpy as np

print(np.__version__)


"""
NumPy Basics
Operator	Description

np.array([1,2,3])	1d array
np.array([(1,2,3),(4,5,6)])	2d array
np.arange(start,stop,step)	range array
"""
"""
Placeholders
Operator	Description
np.linspace(0,2,9)	Add evenly spaced values btw interval to -array of length-
np.zeros((1,2))	Create and array filled with zeros
np.ones((1,2))	Creates an array filled with ones
np.random.random((5,5))	Creates random array
np.empty((2,2))	Creates an empty array
"""
"""
Array
Operator	Description

array.shape	Dimensions (Rows,Columns)
len(array)	Length of Array
array.ndim	Number of Array Dimensions
array.dtype	Data Type
array.astype(type)	Converts to Data Type
type(array)	Type of Array
"""

"""
Copying/Sorting
Operator	Description

np.copy(array)	Creates copy of array
other = array.copy()	Creates deep copy of array
array.sort()	Sorts an array
array.sort(axis=0)	Sorts axis of array
"""



print(np.array([1,2,3,4,5]))
print(np.array([(1,2,3),(4,5,6)]))
print(np.arange(1,20,2))
print('_______________________________________________________________________________________')

print(np.linspace(0,2,9))
print(np.zeros((1,3)))
print(np.ones((1,3)))
print(np.random.random((5,5)))
print(np.empty((2,2)))
print('_______________________________________________________________________________________')

matrix = np.array([[1,2,3,4,5],
          [6,7,8,9,10],
          [4,5,6,7,8]])
print(matrix.shape)  # Output: (3, 5)
print(matrix.size)   # Output: 15
print(len(matrix))   # Output: 3
print(matrix.dtype)  # Output: int64
print(matrix.ndim)
print(matrix.dtype)
print("astype Type: ", matrix.astype(float))
print(type(matrix))


print('_______________________________________________________________________________________')


""" 
Array Manipulation

Adding or Removing Elements

Operator	Description
np.append(a,b)	Append items to array
np.insert(array, 1, 2, axis)	Insert items into array at axis 0 or 1
np.resize((2,4))	Resize array to shape(2,4)
np.delete(array,1,axis)	Deletes items from array

Combining Arrays
Operator	Description

np.concatenate((a,b),axis=0)	Split an array into multiple sub-arrays.
np.vstack((a,b))	Split an array in sub-arrays of (nearly) identical size
np.hstack((a,b))	Split the array horizontally at 3rd index

More

Operator	Description

other = ndarray.flatten()	Flattens a 2d array to 1d
array = np.transpose(other)	Transpose array
array.T	Transpose array
inverse = np.linalg.inv(matrix)	Inverse of a given matrix
Slicing and Subsetting

Operator	Description

array[i]	1d array at index i
array[i,j]	2d array at index[i][j]
array[i<4]	Boolean Indexing, see Tricks
array[0:3]	Select items of index 0, 1 and 2
array[0:2,1]	Select items of rows 0 and 1 at column 1
array[:1]	Select items of row 0 (equals array[0:1, :])
array[1:2, :]	Select items of row 1
[comment]: <> (	array[1,...]
array[ : :-1]	Reverses array
"""


# Array Manipulation

a = np.array([[1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20],
                   [21, 22, 23, 24, 25]])

b = np.array([[2, 4, 6, 8, 10],
                   [3, 6, 9, 12, 15],
                   [4, 8, 12, 16, 20],
                   [5, 10, 15, 20, 25],
                   [6, 12, 18, 24, 30]])

print(np.append(a,b))

"""
The np.insert() method takes three parameters:

arr: the input array where you want to insert the values.
obj: the value or sequence of values to be inserted.
axis: the axis along which to insert the values.
"""

print("Inserting item a: ", np.insert(a, 1, 2, axis=1))  # last 1 means columns and first 1 mean index position, '2' is item
print("Resizing the matrix:", np.resize(4,2))
print("Deleting Numbers: ", np.delete(a, 10))  # Its working like indexing delete inside the a array
print("Concatenating: ", np.concatenate((a,b), axis=0))
print("Vertically Stack: ", np.vstack((a,b)))
print("Horizontally Stack: ", np.hstack((a,b)))

print("______________________________________________________________________________________________________")


print("Flatten a 2D Array to 1D: ", )






print("______________________________________________________________________________________________________")

"""

Slicing and Subsetting
Operator	Description
array[i]	1d array at index i
array[i,j]	2d array at index[i][j]
array[i<4]	Boolean Indexing, see Tricks
array[0:3]	Select items of index 0, 1 and 2
array[0:2,1]	Select items of rows 0 and 1 at column 1
array[:1]	Select items of row 0 (equals array[0:1, :])
array[1:2, :]	Select items of row 1
[comment]: <> (	array[1,...]
array[ : :-1]	Reverses array

"""


"""
Operations
Operator	Description

np.add(x,y)	Addition
np.substract(x,y)	Subtraction
np.divide(x,y)	Division
np.multiply(x,y)	Multiplication
np.sqrt(x)	Square Root
np.sin(x)	Element-wise sine
np.cos(x)	Element-wise cosine
np.log(x)	Element-wise natural log
np.dot(x,y)	Dot product
np.roots([1,0,-4])	Roots of a given polynomial coefficients
Comparison
Operator	Description
==	Equal
!=	Not equal
<	Smaller than
>	Greater than
<=	Smaller than or equal
>=	Greater than or equal
np.array_equal(x,y)	Array-wise comparison
Basic Statistics
Operator	Description
np.mean(array)	Mean
np.median(array)	Median
array.corrcoef()	Correlation Coefficient
np.std(array)	Standard Deviation
More
Operator	Description
array.sum()	Array-wise sum
array.min()	Array-wise minimum value
array.max(axis=0)	Maximum value of specified axis
array.cumsum(axis=0)	Cumulative sum of specified axis
"""
print("______________________________________________________________________________________________________")

import numpy as np

# Example arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([[1, 2], [3, 4]])
d = np.array([[5, 6], [7, 8]])

# Addition
print(np.add(a, b))         # Output: [5 7 9]

# Subtraction
print(np.subtract(a, b))    # Output: [-3 -3 -3]

# Division
print(np.divide(a, b))      # Output: [0.25 0.4  0.5 ]

# Multiplication
print(np.multiply(a, b))    # Output: [ 4 10 18]

# Square Root
print(np.sqrt(a))           # Output: [1.         1.41421356 1.73205081]

# Element-wise sine
print(np.sin(a))            # Output: [0.84147098 0.90929743 0.14112001]

# Dot product
print(np.dot(c, d))         # Output: [[19 22]
                            #          [43 50]]

# Roots of a given polynomial coefficients
print(np.roots([1, 0, -4])) # Output: [ 2. -2.]

# Equal
print(a == b)               # Output: [False False False]

# Array-wise comparison
print(np.array_equal(a, b)) # Output: False

# Mean
print(np.mean(a))           # Output: 2.0

# Median
print(np.median(a))         # Output: 2.0

# Correlation Coefficient
print(np.corrcoef(a, b))    # Output: [[1. 1.]
                            #          [1. 1.]]

# Standard Deviation
print(np.std(a))            # Output: 0.816496580927726

# Array-wise sum
print(a.sum())              # Output: 6

# Array-wise minimum value
print(a.min())              # Output: 1

# Maximum value of specified axis
print(c.max(axis=0))        # Output: [3 4]

# Cumulative sum of specified axis
print(c.cumsum(axis=0))     # Output: [[1 2]
                            #          [4 6]]
