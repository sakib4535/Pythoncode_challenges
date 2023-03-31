# Probability distributions in machine learning literature.

"""
1. Discrete probability distributions are Bernoulli distribution, Binomial distribution, Poisson distribution etc...
2. continuous probability distributions are normal distribution, exponential distribution, beta distribution, etc.

A curve meeting these requirements is often known as a density curve. These Are:

1: The curve has no negative values (p(x) > 0 for all x)

2: The total area under the curve is equal to $1$.

cumulative distribution function. All random variables (discrete and continuous) have a cumulative distribution function.
It is a function giving the probability that the random variable $X$ is less than or equal to $x$, for every value $x$.
For a discrete random variable, the cumulative distribution function is found by summing up the probabilities.

https://openstax.org/books/introductory-statistics/pages/5-2-the-uniform-distribution
https://www.datacamp.com/tutorial/probability-distributions-python
"""

# Essential Libraries

for inline plots in jupyter
%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
for latex equations
from IPython.display import Math, Latex
for displaying images
from IPython.core.display import Image

# import seaborn
import seaborn as sns
# settings for seaborn plotting style
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(5,5)})

# Uniform Distribution Function

"""
https://openstax.org/books/introductory-statistics/pages/5-2-the-uniform-distribution

The probability distribution function of the continuous uniform distribution is:

The uniform function generates a uniform continuous variable between the specified interval via its loc and scale arguments. 
This distribution is constant between loc and loc + scale. The size arguments describe the number of random variates. 
If you want to maintain reproducibility, include a random_state argument assigned to a number.
"""

# import uniform distribution
from scipy.stats import uniform

