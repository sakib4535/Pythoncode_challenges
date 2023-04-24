names = input("Enter Your Name: ")
class Person:
    """This is a person class"""
    def __init__(self, name):
        self.name = name

# Ask for input
name = input("Enter programming language name: ")
ide = input("Enter IDE: ")
year = input("Enter year of creation: ")

class language:
    language1 = "Low-level Versatile programming language"
    language2 = "High Level Dynamic Object Oriented Programming"
    language3 = "Intelligent and Cutting Edge Query Tool"                        # Class attributes

    def __init__(self, name, ide, year): # Instance attribute
        self.name = name
        self.ide = ide
        self.year = year

# Instantiate the language class
lang = language(name, ide, year)

# Instantiate the person class
p = Person(names)

# Access the attributes
print(f"{p.name} using {lang.name} which was developed in {lang.year} with using {lang.ide} as the IDE.")
print(f"{lang.name} is a {lang.__class__.language2}.")

# Instantiate the language class
lan1 = language("C", "VSCODE", 1985)
lan2 = language("Python", "Pycharm", 2000)
lan3 = language("SQL", "Azure", 2010)

print("C is a {}".format(lan1.__class__.language1))
print("Python is a {}".format(lan2.__class__.language2))
print("SQL is a {}".format(lan3.__class__.language3))
