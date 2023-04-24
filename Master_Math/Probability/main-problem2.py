"""One example of a computational mathematical problem using a Uniform distribution could be simulating the probability
of rolling a certain value on a fair dice. For example, suppose we want to simulate the probability of rolling a 6 on a
fair six-sided dice. We can use a Uniform distribution to simulate the dice rolls and estimate the probability of rolling a 6."""

import random
import seaborn as sns
import matplotlib.pyplot as plt

def dice_roll_probability(n):

    """
    Simulates n dice rolls and estimates the probability of rolling a 6.
    :param n: Number of dice rolls to simulate
    :return: Estimated probability of rolling a 6

    """

    # initialize the count of rolls that result in a 6 to 0
    roll_count = 0

    # simulate n dice rolls
    for i in range(n):
        roll = random.uniform(1,6) # Generate a random number from a Uniform distribution wiht range [1,6]
        if roll == 6: # If the roll is a 6, increment the roll count
            roll_count += 1

    probability = roll_count / n
    return probability

# Simulate dice rolls for different sample sizes
# sample_sizes = [10,100,1000,10000]
# probabilities = [dice_roll_probability(n) for n in sample_sizes]


# Simulate 10,000 dice rolls
n = 10000
results = []
for i in range(n):
    result = dice_roll_probability(10)
    results.append(result)

# Create a histogram with seaborn
sns.set_style('whitegrid')
sns.displot(results, kde=False, color='blue')

# Add a vertical line at the expected value of 1/6
plt.axvline(x=1/6, linestyle='--', color='red')

# Add labels and a title
plt.xlabel('Probability of rolling a 6')
plt.ylabel('Frequency')
plt.title('Histogram of dice roll probabilities')

# Display the plot
plt.show()


# Plotting the result using seaborn and matplotlib

# sns.set_style("whitegrid")
# plt.plot(sample_sizes, probabilities, marker='o')
# plt.title("Estimated Probability of rolling a 6")
# plt.xlabel("Number of Dice Rolls")
# plt.ylabel("Probability")
# plt.ylim(0,1)
# plt.show()


