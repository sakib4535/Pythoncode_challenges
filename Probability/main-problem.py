"""implementation of generating random numbers from a uniform distribution in Python"""

import random

def uniform_distribution(a,b,n):

    """
    :param a: Lower Bond of the Uniform distribution
    :param b: Upper Bond of the Uniform distribution
    :param n: Number of random numbers to generate
    :return: A list of n random numbers from the uniform distribution
    """

    # Initializing an empty list to store the random numbers
    uniform_numbers = []

    # Generating n random numbers from the uniform distribution and append them

    for i in range(n):

        rand_num = random.random() # Generate a random number between 0 and 1
        uniform_num = a + rand_num * (b - a) # scale the random number to the desired range[a,b]
        uniform_numbers.append(uniform_num)

    return uniform_numbers


# Generate 10 random numbers from a uniform distribution with lower bound 0 and upper bound 1
result = uniform_distribution(0, 1, 10)

# Print the list of generated random numbers
print(result)


############################################################################################

# Alternative Usage Of The Code Using Visualizing Libraries

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def uniform_distribution2(x, y, j):
    """
    Generates n random numbers from a uniform distribution with lower bound a and upper bound b.

    Args:
    a (float): Lower bound of the uniform distribution.
    b (float): Upper bound of the uniform distribution.
    n (int): Number of random numbers to generate.

    Returns:
    list: A list of n random numbers from the uniform distribution.
    """
    # Generate n random numbers from the uniform distribution
    samples = np.random.uniform(x, y, j)

    # Create a histogram of the generated random numbers using seaborn
    sns.histplot(samples, kde=True)

    # Add plot title and labels
    plt.title('Uniform Distribution')
    plt.xlabel('Values')
    plt.ylabel('Frequency')

    # Show the plot
    plt.show()

    # Return the list of random numbers
    return samples

c = uniform_distribution2(10, 20, 5)
print(c)