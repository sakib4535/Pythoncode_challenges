# Use Collections library

import collections
from collections import Counter

#Containers:
#list
#set
#dict
#tuple - immutable

#Types
#1. counter <- this video
#2. deque
#3. namedTuple()
#4. orderedDict
#5. defaultdict

c = Counter("sakib Imtiaz")
print(c)
c = Counter(['a', 's', 'k', 'i', 'b'])
print(c)
c = Counter({'a':1, 'b':2})
print(c)
c = Counter(cats=4, dogs=9)
print(c)
print(list(c.elements()))

##########################
c = Counter(a=4, b=2, c=0, d=-2)
d = ['a', 'b', 'c', 'c']
c.subtract(d)
print(c)
c.update(d)

###########################

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(['a', 'b', 'c', 'c'])
print(c+d)
print(c-d)
print(c | d)