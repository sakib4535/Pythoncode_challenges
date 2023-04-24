from sympy import Limit, Symbol, S
x = Symbol('x')
print(Limit(1/x, x, S.Infinity))

##############

l = Limit(1/x, x, S.Infinity)
print(l.doit())

print(Limit(1/x, x, 0, dir='+').doit())
print(Limit(1/x, x, 0, dir='-').doit()) # using four parameters where 1/x, where the value of x is 0 and direction is negative infinity.

from sympy import Symbol, sin
print(Limit(sin(x)/x, x, 0).doit())

