""" Suppose you have a list of mathematical functions, each represented as a Python object with the following attributes:

name: The name of the function as a string.
args: A list of arguments for the function as floats.
result: The result of the function as a float.

You want to dynamically compute the value of a new mathematical function that is a linear combination of the functions
in the list, with coefficients given by another list. For example, if the list of functions is f1, f2, and f3, and the
coefficients are c1, c2, and c3, then the new function g is given by:  g(x) = c1*f1(x) + c2*f2(x) + c3*f3(x)

You can create a Python program to solve this problem using
the getattr, setattr, and delattr functions to dynamically create and set attributes of the new function object.
"""

import math

# Define a list of mathematical functions as objects

f1 = type("function",(), {'name':'sin', 'args':[0.5], 'result':None})
f2 = type("function",(), {'name':'cos', 'args':[1.5], 'result':None})
f3 = type("function",(), {'name':'sqrt', 'args':[2.5], 'result':None})
functions = [f1,f2,f3]

coefficients = [1.0, 2.0, 3.0]

# Define the new function object
g = type("function",(), {'name':'g', 'args':[None], 'result':None})

x = 0.1
sum = 0
for i, func in enumerate(functions):
    if hasattr(math, func.name):  # Check if the math module has an attribute with the same name as the current function.
        func_obj = getattr(math, func.name)  # Get the actual function object from the math module using the name of the function.
        output = func_obj(*func.args)
        setattr(func, "result", output)    # Set the result attribute of the current function object to the value of output.
    sum += coefficients[i] * func.result   # Multiply the current function's result by its corresponding coefficient, then add it to the sum variable.

# Set input value attributes of the new function object
setattr(g, "args", [x])
# Set the result attribute of the new function object
setattr(g, "result", sum)
print("value of g(0.1): ", g.result)
