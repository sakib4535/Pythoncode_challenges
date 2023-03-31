# Normal Distribution Function

"""
Normal Distribution, also known as Gaussian distribution
A normal distribution has a bell-shaped density curve described by its mean $μ$ and standard deviation $σ$.
The density curve is symmetrical, centered about its mean, with its spread determined by its standard deviation showing that
data near the mean are more frequent in occurrence than data far from the mean. The probability distribution function of a normal
density curve with mean $μ$ and standard deviation $σ$ at a given point $x$ is given by:

You can generate a normally distributed random variable using scipy.stats module's norm.rvs() method.
The loc argument corresponds to the mean of the distribution. scale corresponds to standard deviation and size
to the number of random variates.
"""

from scipy.stats import norm
# generate random numbers from N(0,1)
data_normal = norm.rvs(size=10000,loc=0,scale=1)

from scipy.stats import norm
# generate random numbers from N(0,1)
data_normal = norm.rvs(size=10000,loc=0,scale=1)
