
"""A good approximation for the root of a real-valued function
f ( x ) = 0 f(x) = 0 f(x)=0 """

""" 
x = 20
for i in range(100):
    xnew = x - (2*x**3 - 9.5*x + 7.5)/(6*x**2 - 9.5)
    if abs(xnew - x) < 0.001: break
    x = xnew
print("The root is %.3f at %d iterations."%(xnew, i))

"""

# Alternative Method
def nraphson(fn, dfn, x, tol, maxiter):
    for i in range(maxiter):
        xnew = x - fn(x)/dfn(x)
        if abs(xnew - x) < tol:
            break
        x = xnew
    return x

y = lambda x: 2*x**3 - 9.5*x + 7.5
dy = lambda x: 6*x**2 - 9

print(nraphson(y, dy, 5, 0.0001, 100))



