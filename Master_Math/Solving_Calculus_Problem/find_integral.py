from sympy import Integral, Symbol
x = Symbol('x')
k = Symbol('k')
print(Integral(k*x, x))
print(Integral(k*x, x).doit())
print(Integral(k*x, (x,0,2)).doit()) # using lower and upper limit as a tuple into the integral object

print(Integral(x, (x,2,4)).doit())


