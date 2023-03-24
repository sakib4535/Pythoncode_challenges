
"""Constants of the math Module
The Python math module offers a variety of predefined constants.
Having access to these constants provides several advantages.
he module includes several famous mathematical constants and important values:

Pi
Tau (Tau (τ) is the ratio of a circle’s circumference to its radius.
This constant is equal to 2π, or roughly 6.28. Like pi, tau is an irrational number because it’s just pi times two.)
Euler’s number (Euler’s number (e) is a constant that is the base of the natural logarithm,
a mathematical function that is commonly used to calculate rates of growth or decay. )
Infinity
Not a number (NaN)
"""

# ceil(x)	Returns the smallest integer greater than or equal to x.
# factorial(x)	Returns the factorial of x
# floor(x)	Returns the largest integer less than or equal to x
# fsum(iterable)	Returns an accurate floating point sum of values in the iterable
# isfinite(x)	Returns True if x is neither an infinity nor a NaN (Not a Number)
# isinf(x)	Returns True if x is a positive or negative infinity
# isnan(x)	Returns True if x is a NaN
# log(x[, b])	Returns the logarithm of x to the base b (defaults to e)
# log1p(x)	Returns the natural logarithm of 1+x
# log2(x)	Returns the base-2 logarithm of x
# log10(x)	Returns the base-10 logarithm of x
# pow(x, y)	Returns x raised to the power y
# sqrt(x)	Returns the square root of x
# acos(x)	Returns the arc cosine of x
# asin(x)	Returns the arc sine of x


import math

print(math.pi)
print(math.e)
print(math.factorial(3))
print(math.exp(4))
print(math.log(math.e))
print(math.log10(1000))
print(math.pow(3,4))
print(math.sqrt(81))
print(math.sin(math.pi))
print(math.radians(180))
print(math.degrees(math.pi))

"""some examples"""

import math
print(math.pi)

def circle_area(r):
    return math.pi*r**2

radius = 5
print("The Area of circle = ", circle_area(radius))

######

deposit = 5000000
interest_rate = 7
years = 10

final_amount = deposit * math.pow(1 + interest_rate, years)
print(f"Our Final Amount is = {final_amount}")
print(type(final_amount))

############################
import math
# ** operator means raise to power i.e. ab for a ** b
res = math.e ** 3 + 5
print(res)

"""" Euler’s Number
Euler’s number (e) is a constant that is the base of the natural logarithm,
a mathematical function that is commonly used to calculate rates of growth or decay. """

"""The math.exp(x) method is equal to , where 
 is the Euler's number. 
 
 math.log()
The math.log() method accepts two arguments, x and base, where the default value of base is 
. So the method returns the natural logarithm of x 
 if we only pass one argument.
 
 math.pow()
The math.pow() method returns a floating-point value representing the value of x to the power of y 
. Let's try the math.pow() method by forecasting an investment
 """