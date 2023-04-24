"""
PROBLEM:

The code is performing a simulation to test the null hypothesis that the mean of a normally distributed population is equal to zero.
The simulation generates 10,000 samples of size 100 from a standard normal distribution, calculates the t-statistic and the p-value
for each sample, and then counts the fraction of p-values that are below a significance level of 0.05.
Finally, it plots the distribution of the p-values. If the null hypothesis is true, the distribution of the p-values should be
uniform, meaning that the fraction of p-values below the significance level should be close to 0.05. If the null hypothesis is false,
the distribution of the p-values will be skewed towards smaller values, indicating that the null hypothesis should be rejected.

"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# set seed for reproducibility
np.random.seed(123)

# define parameters
n_trials = 10000
n_samples = 100
alpha = 0.05

# Define a function to genrrate the data

def  generate_data(n_samples):
    return np.random.normal(0,1,size=n_samples)
# Define a function to calculate the t-statistics
def calculate_t_statistics(data):
    return np.sqrt(len(data)) * np.mean(data) / np.std(data)

# Define a function to calculate the p-value
def calculate_p_value(t_statistics, data):
    return 2 * (1 - stats.t.cdf(abs(t_statistics), df=len(data) - 1))

# Define a function to run the simulation
def run_simulation():
    data = generate_data(n_samples)

    t_statistic = calculate_t_statistics(data)  # calcualte t stat
    p_value = calculate_p_value(t_statistic, data)

    return p_value

# Run the simulation multiple times
p_values = [run_simulation() for _ in range(n_trials)]

# Calculate the fraction of p-values below the significance level
fraction_below_alpha = np.sum(np.array(p_values) < alpha) / n_trials

# Print the result
print('Fraction of p-values below alpha:', fraction_below_alpha)

# Plot the distribution of p-values
sns.histplot(p_values, kde=True)
plt.xlabel('p-value')
plt.ylabel('Count')
plt.title('Distribution of p-values')
plt.show()