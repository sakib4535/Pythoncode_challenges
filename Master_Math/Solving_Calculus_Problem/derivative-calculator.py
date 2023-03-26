from sympy import Symbol, Derivative, sympify, pprint
from sympy.core.sympify import SympifyError

def derivative(f, var):
    var = Symbol(var)
    d = Derivative(f,var).doit()
    pprint(d)

if __name__ == "__main__":

    f = input("Enter a Function: ")
    var = input('Enter the variable to differentiate with respect to: ')
    try:
        f = sympify(f)
    except SympifyError:
        print("Invalid Input")
    else:
        derivative(f,var)

from sympy import Symbol, solve, Derivative
x = Symbol('x')
f1 = x**5 - 30*x**3 + 50*x
d1 = Derivative(f1,x).doit()
print(d1)

critical_points = solve(d1)
print(critical_points)
A = critical_points[2]
B = critical_points[0]
C = critical_points[1]
D = critical_points[3]

# Calculating second order  derivative for the f(x) function where we entered third argument(3rd).
d2 = Derivative(f, x, 2).doit()
print(d2.subs({x:B}).evalf())
print(d2.subs({x:C}).evalf())
print(d2.subs({x:A}).evalf())
print(d2.subs({x:D}).evalf())

# Creating Domain Boundaries with two labels: x_min and x_max to evaluate the function at the points A,C, x_min, x_max.

x_min = -5
x_max = 5

print(f.subs({x:A}).evalf())
print(f.subs({x:C}).evalf())
print(f.subs({x:x_min}).evalf())
print(f.subs({x:x_max}).evalf())

# Now we will determine the global minimum where we must compute the values of f(x) at the points B and D, (-5 to +5)

print(f.subs({x:B}).evalf())
print(f.subs({x:D}).evalf())
print(f.subs({x:x_min}).evalf())
print(f.subs({x:x_max}).evalf())



