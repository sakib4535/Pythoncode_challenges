"""How many tosses before you un out of Money"""

import random

def coin_toss():
    """Return H for heads and T for tails"""
    return random.choice(['H', 'T'])

def play_game(starting_amount):

    """Simulates the Coin toss game and returns the numbebr of tosses required to reach 50"""

    balance = starting_amount
    num_tosses = 0

    while balance > 0:
        toss_result = coin_toss()
        if toss_result == 'H':
            balance += 1
        else:
            balance -= 1.5
        num_tosses += 1
    return num_tosses

# Get user input from starting amount
starting_amount = float(input("Enter the Number: "))

num_tosses = play_game(starting_amount)
print(f"Game Over after {num_tosses}")