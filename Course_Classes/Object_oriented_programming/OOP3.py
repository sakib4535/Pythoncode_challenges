# Object Method


class Person:

    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f"{self.firstname}{self.lastname}, is {self.age} year old. He lives in {self.city} in {self.country}"

p = Person('Sakib', 'Imtiaz', 45, 'USA', 'California')
print(p.person_info())

class Book:

    # Instance Attributes
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    def dance(self):
        return "{} is now dancing".format(self.name)

blue = Book("Haruki Murakami", 100)

print(blue.sing("Happy"))
print(blue.dance())

