"""
The data that follow record the total weight, to the nearest pound, of fish caught by passengers on 35 different charter
fishing boats on one summer day. The sample mean = 7.9 and the sample standard deviation = 4.33.
The data follow a uniform distribution where all values between and including zero and 14 are equally likely.
State the values of a and b. Write the distribution in proper notation, and calculate the theoretical mean and standard deviation.

1	12	4	10	4	14	11
7	11	4	13	2	4	6
3	10	0	12	6	9	10
5	13	4	10	14	12	11
6	10	11	0	11	13	2
Table 5.2

"""


import statistics
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

data = [1, 12, 4, 10, 4, 14, 11, 7, 11, 4, 13, 2, 4, 6, 3, 10, 0, 12, 6, 9, 10, 5, 13, 4, 10, 14, 12, 11, 6, 10, 11, 0, 11, 13, 2]

# calculate mean and standard deviation of the sample
# mean = statistics.mean(data)
mean = np.mean(data)
# stdev = statistics.stdev(data)
stdev = np.std(data, ddof=1)

# Calculate a and b for uniform distribution
a = min(data)
b = max(data)

# Calculate theoreticla mean and standard deviation of the uniform distribution
# uni_mean = (a+b) / 2
# uni_stdev = (b-a) / ((12)**0.5)

uni_mean = (a + b) / 2
uni_stdev = (b - a) / (np.sqrt(12))

# Print the results
# print("Mean of the sample:", mean)
# print("Standard deviation of the sample:", stdev)
# print("a:", a)
# print("b:", b)
# print("Theoretical mean of the uniform distribution:", uni_mean)
# print("Theoretical standard deviation of the uniform distribution:", uni_stdev)

# Create histogram of the data
plt.hist(data, bins=20, density=True, alpha=0.5, color='blue')
plt.axvline(mean, color='red', linestyle='dashed', linewidth=1, label='Sample Mean')
plt.axvline(mean + stdev, color='green', linestyle='dashed', linewidth=1, label='Sample Standard Deviation (Spread)')
plt.axvline(mean - stdev, color='green', linestyle='dashed', linewidth=1)
plt.title('Histogram of the Sample Data')
plt.xlabel('Total weight of fish caught')
plt.ylabel('Density')
plt.legend()
plt.show()

# Create probability density function plot of the theoretical uniform distribution
x = np.linspace(a-1, b+1, 1000)
y = np.ones(len(x)) / (b - a)
plt.plot(x, y, linewidth=2, color='red')
plt.axvline(uni_mean, color='green', linestyle='dashed', linewidth=1, label='Theoretical Mean')
plt.axvline(uni_mean + uni_stdev, color='blue', linestyle='dashed', linewidth=1, label='Theoretical SD')
plt.axvline(uni_mean - uni_stdev, color='blue', linestyle='dashed', linewidth=1)
plt.title('Probability Density Function of the Uniform Distribution')
plt.xlabel('Total weight of fish caught')
plt.ylabel('Density')
plt.legend()
plt.show()

# Create normal probability plot to assess normality assumption of the data
res = (np.sort(data) - mean) / stdev
norm_plot = norm.ppf(np.arange(0.5, len(res)+0.5) / len(res))
plt.scatter(norm_plot, res, color='blue')
plt.plot(norm_plot, norm_plot, color='red', linestyle='dashed')
plt.title('Normal Probability Plot')
plt.xlabel('Theoretical Normal Quantiles')
plt.ylabel('Sample Data Standardized Values')
plt.show()

"""
Since the data follows a uniform distribution, where all values between and including zero and 14 are equally likely, 
the probability density function is:

f(x) = 1/15, for x ∈ [0,14]

Where a=0 and b=14 are the lower and upper bounds of the uniform distribution.

The theoretical mean and standard deviation of a uniform distribution are calculated as:

Mean = (a + b) / 2 = (0 + 14) / 2 = 7

Standard deviation = (b - a) / √12 = (14 - 0) / √12 ≈ 4.04

Therefore, the distribution can be denoted as: X ~ U(0,14), Where X represents the total weight of fish caught by 
passengers on 35 different charter fishing boats on one summer day.
"""