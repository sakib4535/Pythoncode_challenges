import math, sympy
print(math.sin(math.pi/2))
print(sympy.sin(math.pi/2))

from sympy import sin,solve,Symbol
u = Symbol('u')
t = Symbol('t')
g = Symbol('g')
theta = Symbol('theta')
print(solve(u*sin(theta)-g*t, t))

x = Symbol('x', positive=True, complex=True) # we can use 'real', 'integer', 'complex', 'imaginary'
if (x+5) > 0:
    print("Do Something")
else:
    print("Do Something Else")
