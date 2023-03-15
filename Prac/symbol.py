from sympy import Symbol, factor, pprint

x = Symbol('x')
y = Symbol('y')
a = x*x + x*y + x*y + y*y
pprint(factor(a))

expr = x*x + x*y + x*y + y*y
res = expr.subs({x:1, y:2})
print(res)
res1 = expr.subs({x:1-y}) #Express One Symbol in terms of another and substitute
print(res1)

######################################

from sympy import Symbol, pprint, init_printing
def printing_series(n, x_value):

    #Initialize printing system with reverse order

    init_printing(order='rev-lex')

    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x**i)/i

    pprint(series)

    # Evaluate the series at x_value

    series_value = series.subs({x: x_value})
    print("Value of the series at {0} : {1}".format(x_value, series_value))

if __name__ == "__main__":
    n = input("enter the number of terms:  ")
    x_value = input("enter the value of x at which you want:  ")

    printing_series(int(n), float(x_value))


#########################
"""Giving Error Message"""

from sympy import sympify
from sympy.core.sympify import SympifyError
expr = input("Enter a Mathematical Expression: ")
try:
    expr = sympify(expr)
except SympifyError:
    print("Invalid Output")

#################################

"""Product of Two Expressions"""

from sympy import expand, sympify, factor
from sympy.core.sympify import SympifyError

def product(expr1, expr2):
    prod = expand(expr1*expr2)
    pprint(prod)

if __name__ == "__main__":
    expr1 = input("Enter the First Expression: ")
    expr2 = input("Enter the Second Expression: ")

    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)

    except SympifyError:
        print("Invalid Input")
    else:
        product(expr1, expr2)

#######################################33

from sympy import solve, Symbol
x = Symbol('x')
expr = x - 5 - 7
print(solve(expr))

#########################################
from sympy import solve
x = Symbol('x')
expr = x**2 + 5*x + 4  # This x square has two solutions for x
print(solve(expr, dict=True))

####################################
x = Symbol('x')
expr = x**2 + x + 1 # This x square has two solutions for x
print(solve(expr, dict=True))

###########################################