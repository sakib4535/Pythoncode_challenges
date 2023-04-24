class Person(object):

    @staticmethod
    def stat_meth():
        print("Look no self was Passed")

a = Person()
print(a.stat_meth())
print(type(Person.stat_meth))
print(type(a.stat_meth))

####################################################

class Point(object):

    def __new__(cls,*args,**kwargs):
        print("From new")
        print(cls)
        print(args)
        print(kwargs)

        # create our object and return it
        obj = super().__new__(cls)
        return obj

    def __init__(self,a = 0,b = 0):
        print("From init")
        self.a = a
        self.b = b

p2 = Point(6,9)
print(p2)
print(p2.__init__)
print(p2.__format__)
