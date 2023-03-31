"""
Suppose we have a sample of 100 observations from a normal distribution with an unknown mean and standard deviation.
We want to estimate the population mean and standard deviation using this sample and compute a 95% confidence interval
for the population mean. To solve this problem, we can use the following steps:

1. Calculate the sample mean and standard deviation using the sample data.

2. Compute the standard error of the mean (SEM) using the formula
SEM = s / sqrt(n), where s is the sample standard deviation and n is the sample size.

3. Calculate the t-statistic using the formula t = (x_bar - mu) / SEM, where x_bar is the sample mean,
mu is the hypothesized population mean (which is unknown), and SEM is the standard error of the mean.
The t-statistic follows a t-distribution with n - 1 degrees of freedom.

4. Compute the 95% confidence interval for the population mean using the
formula CI = [x_bar - t_crit * SEM, x_bar + t_crit * SEM], where x_bar is the sample mean,
SEM is the standard error of the mean, and t_crit is the critical value of the
t-distribution with n - 1 degrees of freedom and a 95% confidence level.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t

np.random.seed(1234)
sample = np.random.normal(loc=10, scale=2, size=100)

# calculate sample mean and standard deviation
x_bar = np.mean(sample)
s = np.std(sample,ddof=1)

# Calculate the standard error of the mean (SEM)
n = len(sample)
SEM = s / np.sqrt(n)

# Calculate the t-statistic
mu = None           # We do not have a hypothetical population mean
df = n - 1
t_statistic = x_bar / SEM   # code without a hypothesized population mean

# Compute the critical value of the t-distribution
alpha = 0.05
t_crit = t.ppf(1-alpha/2, df)

# Compute the 95% Confidence interval for the population mean
CI = (x_bar - t_crit * SEM, x_bar + t_crit * SEM)

# Print the results
print("Sample mean: {:.3f}".format(x_bar))
print("Sample standard Deviation: {:.3f}".format(s))
print("Standard error of the Mean: {:.3f}".format(SEM))
print("T-statistics: {:.3f}".format(t_statistic))
print("Critical value of t: {:.3f}".format(t_crit))
print("95% confidence interval: ({:.3f}, {:.3f})".format(CI[0], CI[1]))


# Create a plot showing the sample distribution and confidence interval
fig, ax = plt.subplots()
ax.hist(sample, bins=20, density=True)
ax.set_xlabel("Sample Value")
ax.set_ylabel("Density")
ax.axvline(x_bar, color='r', linestyle='--', label='Sample Mean')
ax.axvline(CI[0], color='g', linestyle='--', label="95% CI")
ax.axvline(CI[1], color='b', linestyle='--')
ax.legend()

# Create a plot showing the t-distribution with the critical value and t-statistic
fig, ax = plt.subplots()
x = np.linspace(t.ppf(0.001, df), t.ppf(0.999, df), 100)
ax.plot(x, t.pdf(x, df), 'r-', lw=2, alpha=0.6, label='Critical Value')
ax.axvline(t_statistic, color='b', linestyle='--', label='t-Statistics')
ax.legend()

plt.show()

