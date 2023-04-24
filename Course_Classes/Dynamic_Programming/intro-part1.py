def count_down(n):

    """
    A Recursive function countdown from n to 0.
    :param n:
    :return:
    """

    if n == 0:
        return
    else:
        print(n)
        count_down(n-1)

count_down(5)

# example of Python code that uses a stack and a recursive function with a base condition

"""
Basic Syntax of the Recursion techniques that was used in previous problems
def recursive_function(parameter):
    if base_condition:
        return base_case_output
    else:
        recursive_output = recursive_function(recursive_parameter)
        return final_output(recursive_parameter)
"""

# calculates the sum of integers from 1 to n using functional recursion in Python

""" 
base case n == 1, which returns the sum of 1 (i.e., 1). For all other positive integers n, the function calls itself 
with the argument n-1 and adds n to the result. This recursive process continues until the base case is reached, at 
which point the function returns the final result.
"""

def sum_to_n(n):
    if n==1:
        return 1
    else:
        return n + sum_to_n(n-1)

print(sum_to_n(5))


