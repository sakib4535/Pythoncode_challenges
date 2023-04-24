"""

asarray()
The asarray() function is used when you want to convert an input to an array. The input could be a lists, tuple, ndarray, etc.

Syntax:

numpy.asarray(data, dtype=None, order=None)[source]
data: Data that you want to convert to an array

dtype: This is an optional argument. If not specified, the data type is inferred from the input data

Order: Default is C which is an essential row style. Other option is F (Fortan-style)
"""

import numpy as np

a = np.matrix(np.ones((4,4)))
print(a)

np.array(a)[2] = 3
print(a)  # value won't change in result

"""
Matrix is immutable. You can use asarray if you want to add modification in the original array. 
Let's see if any change occurs when you want to change the value of the third rows with the value 2
"""

np.asarray(a)[2] = 2
print(a)


"""
### `arange()`

The **`arange()`** is an inbuilt numpy function that returns an ndarray object containing evenly spaced values within a defined interval. For instance, you want to create values from 1 to 10; you can use **`arange()`** function.

**Syntax:**
```python
numpy.arange(start, stop,step) 
```
* **`start`**: Start of interval
* **`stop`**: End of interval
* **`step`**: Spacing between values. Default step is 1
"""

# Example 2:

import numpy as np
a = np.arange(1, 14, 4)
print(a)