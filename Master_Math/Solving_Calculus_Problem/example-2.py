from sympy import Symbol, Derivative

t = Symbol('t')
st = 5*t**2 + 2*t + 8

d = Derivative(st, t)
print(d.doit())  # Compute and print the derivative of st with respect to t

t1 = 2  # Define a value for t1
print(d.doit().subs({t: t1}))  # Substitute t with t1 and evaluate the derivative
print(d.doit().subs({t: 1}))  # Substitute t with 1 and evaluate the derivative


###############################

x = Symbol('x')
f = (x**3 + x**2 +x)*(x**2+x)
print(Derivative(f,x).doit())