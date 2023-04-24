import numpy as np
import scipy.stats as stats

# Define the mean and covariance matrix for the complex normal distribution
mean = np.array([[1 + 2j], [3 - 4j]])
cov = np.array([[2 + 1j, 1 - 2j], [1 + 2j, 3 - 1j]])

# Generate a complex normal distribution with the specified mean and covariance matrix
samples = stats.multivariate_normal(mean.flatten(), cov).reshape(-1, 1)

# Print the generated samples
print(samples)
