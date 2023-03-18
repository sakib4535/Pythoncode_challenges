from sympy import FiniteSet, pi
"""For different Gravity and Locations"""

def time_period(length, g):

    T = 2*pi*(length/g)**0.5
    return T

if __name__ == "__main__":

    L = FiniteSet(15,18,21,22.5,26)
    g_values = FiniteSet(9.8, 9.78, 9.83)
    print("{0:^15}{1:^15}{2:^15}".format('Length(cm)', 'Gravity(m/s^2)', 'Time Period(s)'))
    for ele in L*g_values:
        l = ele[0] # From tuple we extracted first value
        g = ele[1] # From tuple we extracted second value associated with gravity
        t = time_period(l/100, g)

        print('{0:^15}{1:^15}{2:^15.3f}'.format(float(l), float(g), float(t)))
