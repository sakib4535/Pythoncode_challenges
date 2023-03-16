# Static and Class Method

class person(object):
    total = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getPopulation(cls):
        return cls.total
    def isAdult(age):
        return age >= 18
    def display(self):
        print(self.name, 'is', self.age, 'years old')

newcomer = person('sakib', 12)
print(person.isAdult(12))
