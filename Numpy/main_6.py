import numpy as np

normal_array = np.random.normal(4.5, 3, 20)
print(normal_array)

### Min
print(np.min(normal_array))

### Max
print(np.max(normal_array))

### Mean
print(np.mean(normal_array))

### Median
print(np.median(normal_array))

### Sd
print(np.std(normal_array))


"""

Broadcasting with array reorganizing
It's super cool and super useful. The one-line explanation is that when doing elementwise operations, things expand to 
the "correct" shape.

"""

# Example:

a = np.linspace(1, 9, 9).reshape(3, 3)
print(a)

# Calculate the determinant of the matrix
det = np.linalg.det(a)

# Check if the determinant satisfies the equation a1A2 + b1B2 + c1C2 = 0
A2 = a[0, 2] * a[1, 1] - a[0, 1] * a[1, 2]
B2 = -a[0, 2] * a[1, 0] + a[0, 0] * a[1, 2]
C2 = a[0, 1] * a[1, 0] - a[0, 0] * a[1, 1]

if a[0, 0] * A2 + a[0, 1] * B2 + a[0, 2] * C2 == 0:
    print("The determinant satisfies the equation a1A2 + b1B2 + c1C2 = 0")
else:
    print("The determinant does not satisfy the equation a1A2 + b1B2 + c1C2 = 0")


import matplotlib.pyplot as plt

normal_array = np.random.normal(6, 2.6, 15) # mean is 6, std is 2.6 and size is 15
plt.hist(normal_array, bins=10)
plt.show()


