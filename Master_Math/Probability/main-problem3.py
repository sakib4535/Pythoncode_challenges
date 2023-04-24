"""
Problem:

One example of using a uniform distribution in real-life financial data could be to simulate stock price movement.
Suppose we want to simulate the stock price movement of a company over the next 100 days.
We can use a uniform distribution to generate random daily returns for the stock, assuming that the daily returns follow
a uniform distribution. We can then use these daily returns to simulate the stock price movement.

"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the seed for reproducibility
np.random.seed(123)

# Define the global parameters
INITIAL_PRICE = 100
N_DAYS = 100
DAILY_RETURN_MIN = -0.05
DAILY_RETURN_MAX = 0.05

# Define a function to generate the daily returns
def generate_daily_returns(min_return, max_return, n_days):
    return np.random.uniform(min_return, max_return, size=n_days)  # Uniform Function have Three Argmebts loc, scale, size

# Define a functon to calculate the cumulative function
def calculate_cumulative_returns(daily_returns):
    return np.cumprod(1 + daily_returns)

# Define a function to calculate the stock price
def calculate_stock_prices(initial_price, cumulative_returns):
    return initial_price * cumulative_returns

    # Define a function to plot the stock prices over time


def plot_stock_prices(stock_prices):
    sns.set_style('darkgrid')
    plt.plot(stock_prices)
    plt.xlabel('Day')
    plt.ylabel('Stock Price')
    plt.title('Stock Price Movement')
    plt.show()

# Define a function to plo the distribution of daily retunrs

def plot_daily_returns(daily_returns):
    sns.histplot(daily_returns, kde=True)
    plt.xlabel("Daily Return")
    plt.ylabel("Count")
    plt.title("Distribution of the Daily Returns")
    plt.show()

# Define a function to plot the distribution of stock prices

def plot_stock_price_distribution(stock_prices):
    sns.histplot(stock_prices, kde=True)
    plt.xlabel('Stock Price')
    plt.ylabel('Count')
    plt.title("Distribution of Stock Prices")
    plt.show()

# Define a main function to run the simulation

def main():
    daily_returns = generate_daily_returns(DAILY_RETURN_MIN, DAILY_RETURN_MAX, N_DAYS)  # generate Daily Returns with global parameters

    # Calculate the cumulative returns and stock prices
    cumulative_returns = calculate_cumulative_returns(daily_returns)
    stock_prices = calculate_stock_prices(INITIAL_PRICE, cumulative_returns)

    # Plot the Result
    plot_stock_prices(stock_prices)
    plot_daily_returns(daily_returns)
    plot_stock_price_distribution(stock_prices)

# Run the main Function
if __name__ == "__main__":
    main()