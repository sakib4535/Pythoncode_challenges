class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"The name of the Cat is {self.name} and he is {self.age} years old")

    def make_sound(self):
        print("Mewww!")

cat1 = Cat('Amelia', 3)
cat2 = Cat('Bella', 6)
print(cat1.info())
print(cat2.info())

###################################

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self):
        """Find distance from origin"""
        return (self.x**2 + self.y**2) ** 0.5

p1 = Point(6,9)
print(f"Distance From the Origin: {p1.distance()}")
print(type(Point.distance))
print(type(p1.distance))

""" p1.distance() is technically equivalent to Point.distance(p1)"""

""" 

Generally, when we call a method with some arguments, the corresponding class function is called by placing the method's 
object before the first argument. So, anything like obj.meth(args) becomes Class.meth(obj, args). The calling process is 
automatic while the receiving process is not (its explicit).

This is the reason the first parameter of a function in class must be the object itself. Writing this parameter as self is 
merely a convention. It is not a keyword and has no special meaning in Python. We could use other names (like this) but it 
is highly discouraged. Using names other than self is frowned upon by most developers and degrades the readability of the 
code (Readability counts).

"""

