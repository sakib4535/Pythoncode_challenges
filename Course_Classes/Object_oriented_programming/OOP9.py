# Polymorphism

class Circle:
    pi = 3.1416

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        print("Area of circle: ", self.pi * self.radius * self.radius)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        print('Area of Rectangle is: ', self.length * self.width)

cir = Circle(8)
rect = Rectangle(9,6)
print(cir.calculate_area())
print(rect.calculate_area())



############################################################

# Another Example:
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

def animal_sounds(animal):
    print(animal.make_sound())


dog = Dog("Fido")
cat = Cat("Whiskers")

animal_sounds(dog)  # Output: Woof!
animal_sounds(cat)  # Output: Meow!
