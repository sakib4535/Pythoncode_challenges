class MyClass():
    def __init__(self):
        print("OKKWW")

def my_def(var=1, class_=MyClass):
    print(var)
    print(class_)

my_def()

class Prefix:
    def __init___(self):
        self.public = 10
        self._private = 40

test = Prefix()

print(test.public)
print(test._private)


class MyClass():
    def __init__(self):
        self.__variable = 10

import testFile
obj = testFile.MyClass()
obj.__variable
