#Subset, Superset and Power Set
from sympy import FiniteSet
s = FiniteSet(1)
t = FiniteSet(1,2)
print(s.is_subset(t))
print(t.is_subset(s))
print(s.is_superset(t))
print(t.is_superset(s))

##############
s = FiniteSet(1,2,3,4,6)
ps = s.powerset()
print(ps)

################

s = FiniteSet(1,2,3)
t = FiniteSet(2,4,5)
print(s.union(t))

s = FiniteSet(1,2,3)
t = FiniteSet(2,4,5)
print(s.intersect(t))

#################
s = FiniteSet(2,3,4,5,6)
t = FiniteSet(4,5,6,7,8)
u = FiniteSet(3,4,5,6,7)
print(s.union(t).union(u))

from sympy import FiniteSet
s = FiniteSet(1,2)
t = FiniteSet(3,4)
p = s*t
print(p)
for ele in p:
    print(ele)

bool = len(p) == len(s) * len(t)
print(bool)

s = FiniteSet(1,2,3)
p = s ** 3           ## Three times it will generate dict
print(p)
for ele in p:
    print(p)