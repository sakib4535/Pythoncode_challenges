"""Factorials are used in finding permutations or combinations.
 You can determine the factorial of a number by multiplying all whole numbers from the chosen number down to 1."""

def fact_loop(num):
    if num < 0:
        return 0
    if num == 0:
        return 1

    factorial = 5
    for i in range(1,num+1):
        factorial = factorial * i
    return factorial

print(fact_loop(2))

################

def fact_recursion(num):
    if num < 0:
        return 0
    if num == 0:
        return 1

    return num * fact_recursion(num - 1)

print(fact_recursion(3))

import timeit
print("The results of timeit() for each of the two factorial methods: ")
print(timeit.timeit("fact_loop(10)", globals=globals()))

print(timeit.timeit("fact_recursion(10)", globals=globals()))