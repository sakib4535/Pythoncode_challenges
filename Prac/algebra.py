from sympy import Symbol
x = Symbol('x')
print(x + x + 1)

x = Symbol('x')
print(x.name)

from sympy import factor, expand, pprint
x = Symbol('x')
y = Symbol('y')

expr = x**2 - y**2
print(factor(expr))
print(expand(expr))

####################################

expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
factors = factor(expr)
print(factors)

##################################
"""Pretty Print"""

expr1 = x**2 + y**2 + 2*x*y
pprint(expr1)

############################

"""Printing Series"""

from sympy import Symbol, pprint, init_printing
def print_series(n):

    init_printing(order='rev-lex')

    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x**i)/i
    pprint(series)

if __name__ == "__main__":
    n = input("Enter the terms: ")
    print_series(int(n))


####################################

"""Substituting"""



