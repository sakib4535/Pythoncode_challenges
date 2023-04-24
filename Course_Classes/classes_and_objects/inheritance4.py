class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed
        print("Cat created.")

    def speak(self):
        return "Meow"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof"


class CatDog(Cat, Dog):
    def __init__(self, cat_name, dog_name, breed):
        super().__init__(cat_name, "white", breed)
        Dog.__init__(self, dog_name, breed)
        print("CatDog created.")

    def speak(self):
        return "MeowWoof"


cd = CatDog("Ramba", "Lala", "Poodle")
print(cd.speak())  # Output: MeowWoof

#################################################################
"""
This code defines two classes Gender and Male. Gender is a base class and Male is a derived class of Gender.
The Gender class has an __init__ method that initializes the name of the person using the name parameter passed to it 
and saves it as an instance variable self.name. The class also has a speak method that prints "Persons speaks" when called.

The Male class is derived from the Gender class and overrides the __init__ method by calling the parent class's __init__ method 
using the super() function. The Male class also overrides the speak method and calls the speak method of the parent class using 
super().speak() and then prints "Male Guy Talking" after that.

Finally, an instance of the Male class is created with the name "Rafsan" and stored in the variable d. 
The speak method of this instance is called using d.speak() which first calls the speak method of the Gender class 
and then prints "Male Guy Talking" afterwards. The output will be:
"""
class Gender:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Persons speaks")

class Male(Gender):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        super().speak()
        print("Male Guy Talking")

d = Male("Rafsan")
d.speak()

#############################################################################

# Example 3:

class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')


class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')


d1 = Dog()
