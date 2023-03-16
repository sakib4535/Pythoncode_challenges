import collections
from collections import deque

d = deque("hello")
d.append('4')
print(d.appendleft(5))

###
print(d.pop())
print(d.popleft())

print(d.clear())
print(d.extend('345'))
print(d.extend('Banga'))

#####

c = deque('hello', maxlen=5)
c.maxlen = 5
print(c)
print(c.extend([1,2,3]))
print(c)


