# First Degree Equation Solving

def plug():
    x= -100
    while x < 100:
        if 2*x + 5 == 13:
            print("x = ",x)
        x += 1 # make x go up by 1 to test the next number

print(plug())


###########################################

# Formula for first degree of equations

def equation(a,b,c,d):
    """Solve Equations of the form ax + b = cx + d (Single Degree Equation format/expresison)"""
    return (d-b)/(a-c)

# Solving Higher Degree of Equation (ax**2 + bx + c = 0)
# Quadratic Equation

#from math import sqrt

#def quad(a,b,c):
#   """Returns the solutions of an equation of the form
#  ax**2 + b*x + c = 0"""

#    x1 = (-b + sqrt(b**2-4*a*c))/(2*a)
#   x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
#    return x1,x2

# a =  5
# b = -3
# c = 7
# print(quad(a,b,c))

