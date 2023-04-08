import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)

# use slicing to pull out the subarray consisting of the first 2 rows
b = a[:2, 1:3]  # row  first and second and column second to third
print(b)    # [[2 3]
         #    [6 7]]

# modifying an array
print(a[0,1])
b[0,0] = 77
print(a[0,1])

print("_________________________________________________________________________")

# Middle row accessing, mixing integer indexing with slices for lower rank
row1 = a [1, :]  # Rank 1 View
print(row1)
print(row1.shape)
row2 = a[1:2, :]   # Rank 2 view
print(row2)
print(row2.shape)

print("_________________________________________________________________________")

col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)  # Prints "[ 2  6 10] (3,)"
print(col_r2, col_r2.shape)

""" Problem Solving Time"""

"""

# Generate matrix:

###    1  2  3  4  5
###    6  7  8  9 10
###   11 12 13 14 15
###   16 17 18 19 20
###   21 22 23 24 25
###   26 27 28 29 30

# Acces 
        11 12
        16 17
    
# Acces  
         2
           8
            14
              20

# Acces        
                4  5



               24 25
               29 30
               
"""

matrix = np.arange(1,31).reshape(6,5)
print(matrix)

sub_matrix = matrix[2:4, 0:2]
print(sub_matrix)

# Access 2 8 14 20
sub_matrix2 = matrix[0::2, 1]
print(sub_matrix2)

# Access 4 5 24 25 29 30
sub_matrix3 = matrix[-2:, -2:]
print(sub_matrix3)

sub_matrix3 = matrix[[0, 3, 4], -2:]
print(sub_matrix3)


print("_________________________________________________________________________")

import numpy as np

a = np.array([[1,2], [3, 4], [5, 6]])
print(a)

bool_operation = (a > 2)
print(bool_operation)