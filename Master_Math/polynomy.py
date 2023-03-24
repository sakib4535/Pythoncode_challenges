"""Polynomials: a0 +a1x+a2x^2+....anxn"""
"""nth degree polynomial, where coefficient can be any numbers."""
"""x3 mean three degree polynomial"""
"""Solution method: Look for the exact degrees while adding, subtracting, multiplying and division"""

import sympy as sym
from IPython.display import display, Math

from sympy.abc import x

p1 = 2*x**3 + x**2 - x
p2 = x**3 - x**4 - 4*x**2

display(Math(sym.latex(p1)))