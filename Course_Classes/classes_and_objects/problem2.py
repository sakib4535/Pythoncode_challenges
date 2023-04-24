class Person:
    def __init__(self, name, height_m, weight_kg):
        self.name = name
        self.height_m = height_m
        self.weight_kg = weight_kg
    
    def bmi(self):
        bmi = self.weight_kg / (self.height_m ** 2)
        return bmi

    def status(self):
        bmi = self.bmi()
        if bmi > 25:
            return self.name + " is overweight"
        else:
            return self.name + " is not overweight"


person1 = Person("Sakib", 1.75, 80)
person2 = Person("Robin", 1.65, 55)
person3 = Person("Tawsif", 1.9, 100)

print(person1.status())
print(person2.status())
print(person3.status())