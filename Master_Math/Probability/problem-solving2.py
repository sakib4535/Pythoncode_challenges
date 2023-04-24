"""
#2: Implement the Gradient Descent

The gradient descent method is used to find the minimum value of a function. Similar to the gradient ascent method, the gradient descent method is
an iterative method: we start with an initial value of the variable and gradually get closer to the variable value that corresponds to the minimum value
of the function. The step that gets us closer is the equation
xnew = xold − λ * df/dx ,
where λ is the step size and df/dx is the result of differentiating the function. Thus, the only difference
from the gradient ascent method is how we obtain the value of x_new from x_old.

Your challenge is to implement a generic program using the gradient descent algorithm to find the minimum value
of a single-variable function specified as input by the user. The program should also create a graph of the function
and show all the intermediate values it found before finding the minimum.
"""

import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(function, initial_x, learning_rate, num_iterations):  # gradient_descent that takes four arguments
    x = initial_x     # initialize the variable x with the initial_x value and x_history as an empty list.
    x_history = [x]
    for i in range(num_iterations):
        gradient = function_derivative(function, x) # This line calculates the gradient (i.e the slope) of the function at the current value of x.
        x -= learning_rate * gradient  # updates the value of x using the gradient descent formula.
        x_history.append(x) # updated value of x to the x_history list.
    return x, function(x), x_history

def function_derivative(function, x):
    h = 1e-6
    return(function(x+h) - function(x-h)) / (2*h)  # This line calculates the derivative of the function with respect to x using the finite difference method.

def plot_function(function, x_range):
    x_values = np.linspace(x_range[0], x_range[1], 100)  # This line creates an array of 100 equally spaced values between x_range[0] and x_range[1].
    y_values = function(x_values)
    plt.plot(x_values, y_values)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Function Plot")

def plot_history(x_history, function):
    y_history = [function(x) for x in x_history]
    plt.plot(x_history, y_history, 'ro-', markersize=3)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Gradient Descent")

# Example usage
def function(x):
    return 2*x**2 + 7*x + 15

plot_function(function, [-10, 5])
initial_x = -5
learning_rate = 0.1
num_iterations = 30
minimum, minimum_value, x_history = gradient_descent(function, initial_x, learning_rate, num_iterations)
plot_history(x_history, function)
plt.show()

