from sympy import Limit, Symbol, S
n = Symbol('n')
print(Limit((1+1/n)**n, n, S.Infinity).doit())


from sympy import Symbol, Limit, S
p = Symbol('P', positive=True)
r = Symbol('r', positive=True)
t = Symbol('t', positive=True)
print(Limit(p*(1+r/n)**(n*t), n, S.Infinity).doit())  # continuous compound interest expression

# Instantaneous Rate of Change

from sympy import Symbol, Limit, Derivative
t = Symbol('t')
st = 5*t**2 + 2*t + 8

t1 = Symbol('t1')
delta_t = Symbol('delta_t')

st1 = st.subs({t: t1})
st1_delta = st.subs({t: t1 + delta_t})

print(Limit((st1_delta-st1)/delta_t, delta_t, 0).doit())

t2 = Symbol('t')
st2 = 5*t**2 + 2*t + 8
d2 = Derivative(st,t)
print(Derivative(st,t))
print(d2.doit().subs({t:t1}))
print(d2.doit().subs({t:1}))

from sympy import Derivative, Symbol
x = Symbol('x')
f = (x**3 + x**2 + x)*(x**2 + x)
print(Derivative(f,x).doit())













