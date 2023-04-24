"""Use gradient ascent to find the maximum value of a single-variable function.
This also checks the existence of a solution for the equation"""

from sympy import Derivative, Symbol, sympify, solve, SympifyError

def grad_ascent(x0, f1x, x):
    # check if f1x=0 has solution
    if not solve(f1x):
        print("cannot continue, solution for {0}=0 does not exist".format(f1x))
        return
    epsilon = 1e-6
    step_size = 1e-4
    x_old = x0
    x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
    while abs(x_old - x_new) > epsilon:
        x_old = x_new
        x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
    return x_new

if __name__ == "__main__":

    f = input("Enter a function in one variable: ")
    var = input("Enter the variable to differentiate with respect to: ")
    var0 = float(input('Enter the initial Value of the variable: '))
    try:
        f = sympify(f)
    except SympifyError:
        print("Invalid Function entered")
    else:
        var = Symbol('var')
        d = Derivative(f, var).doit()
        var_max = grad_ascent(var0, d, var)
        if var_max:
            print("{0}:{1}".format(var.name, var_max))
