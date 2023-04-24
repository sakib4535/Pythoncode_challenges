"""
Flatten Data
When you deal with some neural network like convnet, you need to flatten the array. You can use flatten().

numpy.flatten(order='C')
a: Array that you want to reshape
newShape: The new desires shape
order: Default is C which is an essential row style.

What is vstack?
With vstack you can appened data vertically.

What is hstack?
With hstack you can appened data horizontally. This is a very convinient function in Numpy.

Generate Random Numbers----
To generate random numbers for Gaussian distribution use:

Syntax:

numpy.random.normal(loc, scale, size)
loc: the mean. The center of distribution
scale: standard deviation.
size: number of returns
"""

import numpy as np

# set the mean and standard deviation
mu = 10
sigma = 2

# generate 10 random numbers from a normal distribution with mean=mu and std=sigma
random_numbers = np.random.normal(mu, sigma, 10)  # loc, scale, size parameters as arguments

# print the generated random numbers
print(random_numbers)


"""
Linspace
Linspace gives evenly spaced samples.

Syntax:

numpy.linspace(start, stop, num, endpoint)
start: Start of sequence
stop: End of sequence
num: Number of samples to generate. Default is 50
endpoint: If True (default), stop is the last value. If False, stop value is not included.
"""
print("_________________________________________________________________")
import numpy as np

# generate 10 equally spaced samples between 0 and 1
samples = np.linspace(0, 1, num=10, endpoint=True)
samples2 = np.linspace(0,10,6)   # (10-0) / (6-1) = 2, 2 difference
"""
Here's what each of the parameters passed to np.linspace() means:

The first parameter, 0, is the start of the sequence.
The second parameter, 10, is the end of the sequence.
The third parameter, 3, is the number of samples to generate between the start and end of the sequence.
"""
# print the generated samples
print(samples)
print(samples2)


"""
LogSpace
LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.

Syntax:

numpy.logspace(start, stop, num, endpoint)
start: Start of sequence
stop: End of sequence
num: Number of samples to generate. Default is 50
endpoint: If True (default), stop is the last value. If False, stop value is not included.

"""

lang = np.logspace(3.0, 4.0, num=4)
x = np.array([1,2,3], dtype=np.complex128)
print(x)
print(x.itemsize)