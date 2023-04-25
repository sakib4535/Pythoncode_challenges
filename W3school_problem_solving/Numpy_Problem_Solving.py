#!/usr/bin/env python
# coding: utf-8

# # W3Resources: Using Numpy Library 

# # *** Level: Basic
# 

# 1. Write a Numpy program to get the Numpy version and show the Numpy build configuration.

# In[2]:


import numpy as np

print("Numpy Version:", np.__version__)
print("Numpy Build Configuration:")
print(np.show_config())


# 2. Write a NumPy program to get help with the add function.

# In[9]:


import numpy as np

# Use the help() function to get information about the add() function
help(np.add)
help(np.subtract)
help(np.multiply)
help(np.divide)


# 3. Write a NumPy program to test whether none of the elements of a given array are zero.

# In[6]:


import numpy as np

arr = np.array([[1,2,3,4,5],
              [6,7,8,9,10]])

result = np.all(arr != 0)

if result:
    print("None of them are zero")
else:
    print("At least One element is Zero")


# 4. Write a NumPy program to test if any of the elements of a given array are non-zero.

# In[ ]:





# 5. Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a number).

# In[7]:


import numpy as np

arr = np.array([1.0, np.inf, np.nan, 2.0, -np.inf])
result = np.isfinite(arr)
print(result)


# 6. Write a NumPy program to test elements-wise for positive or negative infinity.

# In[8]:


import numpy as np

arr = np.array([1.0, np.inf, np.nan, 2.0, -np.inf])

result = np.isinf(arr)
result_pos = np.isposinf(arr)
result_neg = np.isneginf(arr)

# Print the results
print("Is infinite?", result)
print("Is positive infinite?", result_pos)
print("Is negative infinite?", result_neg)


# 7. Write a NumPy program to test element-wise for NaN of a given array. 

# In[11]:


import numpy as np

arr = np.array([1.0, np.inf, np.nan, 2.0, -np.inf])
result = np.isnan(arr)
print(result)


# 8. Write a NumPy program to test element-wise for complex numbers, real numbers in a given array. Also test if a given number is of a scalar type or not.

# In[12]:


import numpy as np

# Define the input array
arr = np.array([1+2j, 3+4j, 5+0j, 7, 8.5])

result_complex = np.iscomplex(arr)
result_real = np.isreal(arr)
num = 19
result_scalar = np.isscalar(num)

# Print the results
print("Is complex?", result_complex)
print("Is real?", result_real)
print("Is scalar?", result_scalar)


# 9. Write a NumPy program to test whether two arrays are element-wise equal within a tolerance.

# In[17]:


import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([1.0, 2.0, 3.01])

# Test whether the arrays are element-wise equal within a tolerance
tolerance = 0.1
result = np.allclose(a, b, rtol=tolerance)

if result:
    print("The arrays are equal within a tolerance of", tolerance)
else:
    print("The arrays are not equal within a tolerance of", tolerance)


# 10. Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.

# In[18]:


import numpy as np

a = np.array([1,2,3,4])
b = np.array([3,2,5,1])

greater = np.greater(a,b)
greater_equal = np.greater_equal(a,b)
less = np.less(a,b)
less_equal = np.less_equal(a,b)


# print the results
print("Array a:", a)
print("Array b:", b)
print("a > b:", greater)
print("a >= b:", greater_equal)
print("a < b:", less)
print("a <= b:", less_equal)


# 11. Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.

# In[ ]:





# 12. Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array.

# In[19]:


import numpy as np

# create an array with the given values
arr = np.array([1, 7, 13, 105])
size = arr.nbytes

print("Array:", arr)
print("Size of array in bytes:", size)


# 13. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives. 

# In[22]:


import numpy as np

zeros_arr = np.zeros(10)
ones_arr = np.ones(10)
fives_arr = np.full(10,5)

print("Array of 10 zeros:", zeros_arr)
print("Array of 10 ones:", ones_arr)
print("Array of 10 fives:", fives_arr)


# 14. Write a NumPy program to create an array of integers from 30 to 70. 

# In[23]:


import numpy as np

# create an array of integers from 30 to 70
arr = np.arange(30, 71)

# print the array
print("Array of integers from 30 to 70:", arr)


# 15.Write a NumPy program to create an array of all even integers from 30 to 70. 

# In[25]:


import numpy as np

# create an array of integers from 30 to 70
arr = np.arange(30, 71, 2)

# print the array
print("Array of integers with even numbers from 30 to 70:", arr)


# 16. Write a NumPy program to create a 3x3 identity matrix. 

# In[27]:


matrix = np.identity(3)
print(matrix)


# 17. Write a NumPy program to generate a random number between 0 and 1.

# In[28]:


import numpy as np
# Rnadom number between 0 and 1
random_num = np.random.rand()
print("Random number between 0 and 1: ", random_num)


# 18. Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution. 

# In[29]:


arr = np.random.randn(15)
print(arr)


# 19. Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.

# In[31]:


import numpy as np

vector = np.arange(15,56)
print(vector[1:-1])


# 20. Write a NumPy program to create a 3X4 array and iterate over it.

# In[36]:


import numpy as np

arr = np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]])
print(arr.shape)
print(arr.size)
print(arr.nbytes)

for i in range(arr.shape[0]): # accessing row
    for j in range(arr.shape[1]): # accessing column
        print(arr[i][j])
        


# # **** Array

# 2. Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

# In[38]:


import numpy as np
values_list = [1,2,3,4,5]
value_arr = np.array(values_list)
print(value_arr)


# 3.Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10. Go to the editor
# Expected Output:
# [[ 2 3 4]
# [ 5 6 7]
# [ 8 9 10]]

# In[39]:


arr = np.arange(2,11)
matrix = arr.reshape(3,3)
print(matrix)


# 4. Write a NumPy program to create a null vector of size 10 and update the sixth value to 11. Go to the editor
# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# Update sixth value to 11
# [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]

# In[41]:


vec = np.zeros(10)
vec[5] = 11
print(vec)


# 5. Write a NumPy program to create an array with values ranging from 12 to 38. Go to the editor
# Expected Output:
# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

# In[42]:


import numpy as np

# create an array with values ranging from 12 to 38
arr = np.arange(12, 38)

# print the array
print(arr)


# 6. Write a NumPy program to reverse an array (the first element becomes the last). Go to the editor
# Original array:
# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
# Reverse array:
# [37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12]

# In[44]:


arr = np.arange(12,38)
reverse =  np.flip(arr)
print(arr)
print(reverse)


# 7. Write a NumPy program to convert an array to a floating type. Go to the editor
# Sample output:
# Original array
# [1, 2, 3, 4]
# Array converted to a float type:
# [ 1. 2. 3. 4.]

# In[45]:


arr = np.arange(1,5)
arr_float = arr.astype('float')
print(arr)
print(arr_float)


# 8. Write a NumPy program to create a 2D array with 1 on the border and 0 inside.Go to the editor
# Expected Output:
# Original array:
# [[ 1. 1. 1. 1. 1.]
# ...................
# [ 1. 1. 1. 1. 1.]]
# 1 on the border and 0 inside in the array
# [[ 1. 1. 1. 1. 1.]
# ...................
# [ 1. 1. 1. 1. 1.]]

# In[47]:


# creating 5x5 array
arr = np.ones((5,5))
arr[1:-1, 1:-1] = 0
print(arr)
print(arr)


# 9. Write a NumPy program to add a border (filled with 0's) around an existing array. Go to the editor
# Expected Output:
# Original array:
# [[ 1. 1. 1.]
# [ 1. 1. 1.]
# [ 1. 1. 1.]]
# 1 on the border and 0 inside in the array
# [[ 0. 0. 0. 0. 0.]
# ...........
# [ 0. 0. 0. 0. 0.]]

# In[52]:


import numpy as np

# Create the original array
original_array = np.ones((3,3))

# Add a border of zeros to the original array
bordered_array = np.pad(original_array, 1, mode='constant')

# Print the original and bordered arrays
print("Original array:\n", original_array)
print("\nArray with a border of zeros:\n", bordered_array)

# ALternative MEthod

arr = np.ones((5,5))
print(arr)

arr[: , [0,-1]] = 0
arr[[0,-1], :] = 0
print("Array with border:")
print(arr)


# 10. Write a NumPy program to create an 8x8 matrix and fill it with a checkerboard pattern. Go to the editor
# Checkerboard pattern:
# [[0 1 0 1 0 1 0 1]
# ..........
# [0 1 0 1 0 1 0 1]
# [1 0 1 0 1 0 1 0]]

# In[54]:


"""
arr[1::2,1::2] = 0 sets every other element in every other row to 0, but starting from the second row and column, effectively setting the odd 
columns in odd rows to 0.
"""

matrix = np.zeros((8,8), dtype=int)
"""even columns in even rows to 0."""
matrix[::2, ::2] = 1  # arr[::2] means take every second element in arr starting from the first element
""" odd columns in odd rows to 0."""
matrix[1::2, 1::2] = 1 # arr[1::2,1::2] = 0 sets every other element in every other row to 0, but starting from the second row and column, effectively setting the odd columns in odd rows to 0.
print(matrix)


# 11. Write a NumPy program to convert a list and tuple into arrays. Go to the editor
# List to array:
# [1 2 3 4 5 6 7 8]
# Tuple to array:
# [[8 4 6]
# [1 2 3]]

# In[ ]:





# 12. Write a NumPy program to append values to the end of an array. Go to the editor
# Expected Output:
# Original array:
# [10, 20, 30]
# After append values to the end of the array:
# [10 20 30 40 50 60 70 80 90]

# In[55]:


import numpy as np

original_array = np.array([10, 20, 30])
values_to_append = np.array([40, 50, 60, 70, 80, 90])

appended_array = np.append(original_array, values_to_append)

print("Original array:")
print(original_array)

print("After appending values to the end of the array:")
print(appended_array)


# 13. Write a NumPy program to create an empty and full array. Go to the editor
# Expected Output:
# [ 6.93270651e-310 1.59262180e-316 6.93270559e-310 6.93270665e-310]
# [ 6.93270667e-310 6.93270671e-310 6.93270668e-310 6.93270483e-310]
# [ 6.93270668e-310 6.93270671e-310 6.93270370e-310 6.93270488e-310]]
# [[6 6 6]
# [6 6 6]
# [6 6 6]]

# In[59]:


empty_arr = np.empty((3,4))
print(empty_arr)

# fully array with value 6
full_arr = np.full((3,3), 6)
print(full_arr)


# 14. Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array. Go to the editor
# Sample Array [0, 12, 45.21, 34, 99.91]
# [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]
# Expected Output:
# Values in Fahrenheit degrees:
# [ 0. 12. 45.21 34. 99.91 32. ]
# Values in Centigrade degrees:
# [-17.78 -11.11 7.34 1.11 37.73 0. ]
# 
# Values in Centigrade degrees:
# [-17.78 -11.11 7.34 1.11 37.73 0. ]
# Values in Fahrenheit degrees:
# [-0. 12. 45.21 34. 99.91 32. ]

# In[61]:


celcius = np.array([0,12,45,21,34,99,91,0])
fahrenheit = celcius * 9 / 5 + 32
print(fahrenheit)
print(celcius)


# 15. Write a NumPy program to find the real and imaginary parts of an array of complex numbers. Go to the editor
# Expected Output:
# Original array [ 1.00000000+0.j 0.70710678+0.70710678j]
# Real part of the array:
# [ 1. 0.70710678]
# Imaginary part of the array:
# [ 0. 0.70710678]

# In[62]:


import numpy as np

# Create a complex array
arr = np.array([1+0j, 0.70710678+0.70710678j])

real_part = arr.real
imag_part = arr.imag

print(arr)
print(real_part)
print(imag_part)


# 16. Write a NumPy program to find the number of elements in an array. It also finds the length of one array element in bytes and the total bytes consumed by the elements. Go to the editor
# Expected Output:
# Size of the array: 3
# Length of one array element in bytes: 8
# Total bytes consumed by the elements of the array: 24

# In[63]:


import numpy as np

arr = np.array([20,40,21,3,2,1,23,41])
print("Size of the array:", arr.size)
print("Length of one array element in bytes:", arr.itemsize)
print("Total bytes consumed by the elements of the array:", arr.nbytes)


# 17. Write a NumPy program to test whether each element of a 1-D array is also present in a second array. Go to the editor
# Expected Output:
# Array1: [ 0 10 20 40 60]
# Array2: [0, 40]
# Compare each element of array1 and array2
# [ True False False True False]

# In[66]:


array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([0, 40])

result = np.in1d(array1, array2) 

print("Array1:", array1)
print("Array2:", array2)
print("Compare each element of array1 and array2")
print(result)


# 18. Write a NumPy program to find common values between two arrays. Go to the editor
# Expected Output:
# Array1: [ 0 10 20 40 60]
# Array2: [10, 30, 40]
# Common values between two arrays:
# [10 40]

# In[68]:


array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([10, 30, 40])

common = np.intersect1d(array1, array2)

print("Array1:", array1)
print("Array2:", array2)
print("Common values between two arrays:")
print(common)


# 19. Write a NumPy program to get the unique elements of an array. Go to the editor
# Expected Output:
# Original array:
# [10 10 20 20 30 30]
# Unique elements of the above array:
# [10 20 30]
# Original array:
# [[1 1]
# [2 3]]
# Unique elements of the above array:
# [1 2 3]

# In[69]:


import numpy as np

arr1 = np.array([10, 10, 20, 20, 30, 30])
arr2 = np.array([[1, 1], [2, 3]])

print("Original array:")
print(arr1)
print("Unique elements of the above array:")
print(np.unique(arr1))

print("Original array:")
print(arr2)
print("Unique elements of the above array:")
print(np.unique(arr2))


# 20. Write a NumPy program to find the set difference between two arrays. The set difference will return sorted, distinct values in array1 that are not in array2. Go to the editor
# Expected Output:
# Array1: [ 0 10 20 40 60 80]
# Array2: [10, 30, 40, 50, 70, 90]
# Set difference between two arrays:
# [ 0 20 60 80]

# In[70]:


import numpy as np

array1 = np.array([0, 10, 20, 40, 60, 80])
array2 = np.array([10, 30, 40, 50, 70, 90])

result = np.setdiff1d(array1, array2)

print("Array1:", array1)
print("Array2:", array2)
print("Set difference between two arrays:")
print(result)


# In[ ]:




