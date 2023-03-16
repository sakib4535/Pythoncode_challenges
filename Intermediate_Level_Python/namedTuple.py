from collections import namedtuple
import collections

Point = namedtuple('Point', 'x y z')
newP = Point(3,4,5)
print(newP)

######
Point = namedtuple('Point', ['x', 'y', 'z'])
newP = Point(13,24,55)
print(newP)

########
Point = namedtuple('Point', {'x':0, 'y':0, 'z':0})
newP = Point(13.21,24.21,55.31)
print(newP)

######
Point = namedtuple('Point', {'x':0, 'y':0, 'z':0})
newP = Point(13.21,24.21,55.31)
print(newP.x, newP.y, newP.z)
print(newP[0])
print(newP._asdict())

#####
Point = namedtuple('Point', {'x':0, 'y':0, 'z':0})
newP = Point(13.21,24.21,55.31)
print(newP._fields)
print(newP._replace(y=4))

p2 = Point._make(['a', 'b', 'c'])
print(p2)