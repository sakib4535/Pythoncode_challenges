# For One Variable

from sympy import *
from sympy.parsing.sympy_parser import parse_expr

# Accept user inputs
function_str = input("Enter a function is one variable: ")
variable_str = input("Enter the Variable: ")
point_str = input("Enter the point to check the continuity at: ")

# Parse the Function and variable strings into Sympy objects
function = parse_expr(function_str)
variable = symbols(variable_str)

# Compute the left-hand and right-hand limits
lhs_limit = limit(function, variable, float(point_str), dir='-')
rhs_limit = limit(function, variable, float(point_str), dir='+')

# Check if the function is continuous at the point
if lhs_limit == rhs_limit:
    print(f"{function_str} is continuous at {point_str}")
else:
    print(f"{function_str} is not continuous at {point_str}")


# ALTERNATIVE: For Two variable at a point


from sympy import *
from sympy.parsing.sympy_parser import parse_expr

# Accept user inputs
function_str1 = input("Enter a function in two variables: ")
variables_str1 = input("Enter the two variables separated by a comma: ")
point_str1 = input("Enter the point to check the continuity at separated by a comma: ")

# Parse the function and variable strings into SymPy objects
function1 = parse_expr(function_str1)
variables = symbols(variables_str1)
var1, var2 = variables[0], variables[1]

# Convert the point to a tuple of floats
point = tuple(map(float, point_str1.split(',')))

# Unpack the point tuple into two variables
p1, p2 = point

# Compute the left-hand and right-hand limits for each variable
lhs_limit_var1 = limit(function1, var1, p1, dir='-')
rhs_limit_var1 = limit(function1, var1, p1, dir='+')
lhs_limit_var2 = limit(function1, var2, p2, dir='-')
rhs_limit_var2 = limit(function1, var2, p2, dir='+')

# Check if the function is continuous at the point
if lhs_limit_var1 == rhs_limit_var1 and lhs_limit_var2 == rhs_limit_var2:
    print(f"{function_str1} is continuous at {point_str1}")
else:
    print(f"{function_str1} is not continuous at {point_str1}")
