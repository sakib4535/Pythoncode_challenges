"""
Area Between Two Curves
We learned that the integral expresses the area enclosed by the function f(x), with the x-axis between
x = a and x = b. The area between two curves is thus expressed as the integral,
where a and b are the points of intersection of the two curves with a < b.
The function f(x) is referred to as the upper function and g(x) as the lower
function. Figure 7-9 illustrates this, assuming f(x) = x and g(x) = x2, with a = 0 and b = 1.
Your challenge here is to write a program that will allow the user to
input any two single-variable functions of x and print the enclosed area between the two.
The program should make it clear that the first function entered should be the upper function, and it should also ask for the values
of x between which to find the area.

Solving Calculus Problems 207
Figure 7-9: The functions f(x) = x and g(x) = x2
 enclose an area between
x = 0 and x = 1.0.
Here's a Python program that calculates the area between two curves:

"""

import sympy as sp

# Ask user for the two functions

f = sp.sympify(input("Enter the upper function in terms of x: "))
g = sp.sympify(input("Enter the lower function in terms of x: "))

# Ask the user for the interval of integration
a = float(input("Enter the lower bound of integration: "))
b = float(input("Enter the upper bound of integration: "))

# Find the points of intersection of the two curves

points = sp.solve(f-g)

# Define the upper and lower functions

if points[0] < points[1]:
    upper = f
    lower = g
else:
    upper = g
    lower = f

area = sp.integrate(upper - lower, (sp.Symbol('x'), a,b))
print("The area between the two curves is: ", area)
