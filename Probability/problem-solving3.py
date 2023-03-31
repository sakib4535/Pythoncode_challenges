"""
#1: Verify the Continuity of a Function at a Point

A necessary, but not sufficient, condition for a function to be differentiable at a point is that
it must be continuous at that point. That is, the function must be defined at that point and its left-hand limit and righthand
limit must exist and be equal to the value of the function at that point. If f(x) is the function and x = a is the point
we are interested in evaluating, this is mathematically stated as
.
Your challenge here is to write a program that will (1) accept a single variable function and a value of that variable as inputs and (2) check
whether the input function is continuous at the point where the variable
assumes the value input.
"""

""" Solution Document:

This is a problem statement for a program that verifies the continuity of a function at a given point. 
The program accepts two inputs: a single-variable function and a value of that variable. 
The program checks whether the input function is continuous at the point where the variable assumes the given value. 
If the function is continuous at that point, the program will output a message saying so. 
If the function is not continuous at that point, the program will output a message indicating the point of discontinuity. 
"""

import sympy
import numpy as np
import matplotlib.pyplot as plt

# Accept input function and value
function = input("Enter a function in one variable: ")
variable = input("Enter the variable: ")
point = float(input("Enter the point to check the continuity at: "))

# crate symbolic expression from input function
expr = sympy.sympify(function)

# Define function for plotiing
f = sympy.lambdify(variable, expr, 'numpy')

# Plot Function
x = np.linspace(point, -1, int(point) + 1, 100)
y = f(x)
plt.plot(x,y)

# Check left-hand and right-hnad limits
left_limit = sympy.limit(expr, variable, point, dir='-')
right_limit = sympy.limit(expr, variable, point, dir='+')

# Check continuity at point
if left_limit == right_limit:
    print(f"{function} is continuous at {point:.1f}")
else:
    print(f"{function} is not continuous at {point:.1f}")
    plt.plot(point, f(point), 'ro')

plt.xlabel(variable)
plt.ylabel(function)
plt.title("Function plot")
plt.show()