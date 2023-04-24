# Define the Rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def description(self):
        return "This is a rectangle with width {} and height {}".format(self.width, self.height)

# Create an object of the Rectangle class
rect = Rectangle(5, 10)

# Use the built-in class attributes to access the class name, module name, and base classes
class_name = Rectangle.__name__
module_name = Rectangle.__module__
base_classes = Rectangle.__bases__

# Print the results
print("Class name:", class_name)
print("Module name:", module_name)
print("Base classes:", base_classes)

# Call the description() method to get a string describing the rectangle
description = rect.description()

# Print the description
print(description)
