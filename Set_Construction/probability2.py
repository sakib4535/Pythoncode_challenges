from sympy import FiniteSet
s = FiniteSet(1,2,3,4,5,6)
a = FiniteSet(2,3,5) # Prime Numbers
b = FiniteSet(1,3,5) # Odd numbers
e = a.intersect(b)
print(len(e)/len(s))

# Simulating Die Roll (six_sided)
import random
print(random.randint(1,6))

"""Roll the dice until the total score is 20"""

import matplotlib.pyplot as plt
import random

target_score = 20

def roll():
    return random.randint(1,6)

if __name__ == "__main__":
    score = 0
    number_of_rolls = 0
    while score < target_score:
        die_roll = roll()
        number_of_rolls += 1
        print("Rolled: {0}".format(die_roll))
        score += die_roll
    print('Score of {0} reached in {1} rolls'.format(score, num_rolls))




