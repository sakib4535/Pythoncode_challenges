"""
Problem:
The total duration of baseball games in the major league in the 2011 season is uniformly distributed between
447 hours and 521 hours inclusive.

Find a and b and describe what they represent.
Write the distribution.
Find the mean and the standard deviation.
What is the probability that the duration of games for a team for the 2011 season is between 480 and 500 hours?
What is the 65th percentile for the duration of games for a team for the 2011 season?
"""

"""
a) a = 447 and b = 521 represent the lower and upper bounds of the duration of baseball games in the 
major league in the 2011 season.

b) The distribution can be written as X ~ U(447, 521), which means that the duration of baseball games is uniformly 
distributed between 447 and 521 hours inclusive.

c) Mean (μ) = (a + b) / 2 = (447 + 521) / 2 = 484
Standard deviation (σ) = (b - a) / sqrt(12) = (521 - 447) / sqrt(12) = 11.32

d) To find the probability that the duration of games for a team for the 2011 season is between 480 and 500 hours, 
we need to find the area under the uniform distribution curve between these values. This can be calculated as:

P(480 < X < 500) = (500 - 480) / (b - a) = 20 / 74 = 0.2703

Therefore, the probability that the duration of games for a team for the 2011 season is between 480 and 500 hours 
is approximately 0.2703.

e) To find the 65th percentile for the duration of games for a team for the 2011 season, we need to find the value of
 X such that P(X < x) = 0.65. This can be calculated as:

0.65 = (x - a) / (b - a)
0.65(b - a) = x - a
x = a + 0.65(b - a)
x = 447 + 0.65(521 - 447)
x = 494.4

Therefore, the 65th percentile for the duration of games for a team for the 2011 season is approximately 494.4 hours.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

a = 447
b = 521

# Create an array of values for the distribution
x = np.linspace(a,b,100)

mean = (a+b) / 2
stdev = ((b-1) ** 2 / 12) ** 0.5

# Calculate the probability that the duration of games for a team is between 480 and 500 hours
prob = stats.uniform.cdf(500, loc=a, scale=b-a) - stats.uniform.cdf(480, loc=a, scale=b-a)

# Calculate the 65th percentile for the duration of games for a team
percentile = stats.uniform.ppf(0.65, loc=a, scale=b-a)

# Plot the distribution and shade the area between 480 adn 500 hours
plt.plot(x, stats.uniform.ppf(x, loc=a, scale=b-a), 'b-', label="PDF")
plt.fill_between(x, 0, stats.uniform.pdf(x, loc=a, scale=b-a), where=(x >= 480) & (x <= 500), color='green', alpha=0.5, label='Probability')
plt.axvline(x=mean, color='r', linestyle='--', label='Mean')
plt.axvline(x=percentile, color='blue', linestyle='--', label='65th Percentile')
plt.xlabel('Duration of Games (hours)')
plt.ylabel('Probability Density')
plt.title('Uniform Distribution of Baseball Game Durations')
plt.legend()
plt.show()


"""

stats.uniform.cdf() function from the SciPy library to calculate the probability that the duration of games for a 
team is between 480 and 500 hours, and the stats.uniform.ppf() function to calculate the 65th percentile for the duration 
of games for a team.

"""




