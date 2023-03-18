from sympy import FiniteSet
from fractions import Fraction
s = FiniteSet(1,1.3, Fraction(1,5))
print(s)
print(2 in s)


# Creating Empty set, sets from lists or tuples

a = FiniteSet()
print(a)

mem = [21,4,1,3,12,312,313,12,45,5]
s = FiniteSet(*mem)
print(s)

mem2 = [21,43,1,43,21,654,76,98]
print(FiniteSet(*mem2))

#Iteration
s1 = FiniteSet(21,34,12,42,51)
for mem3 in s1:
    print(mem3)

s2 = FiniteSet(2,3,4)
s3 = FiniteSet(4,5,6)
print(s2 == s3)

