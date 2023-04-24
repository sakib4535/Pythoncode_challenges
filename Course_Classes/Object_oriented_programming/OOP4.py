# Object Default Methods
class Car:

    def __init__(self, make="Toyota", model=" Corolla", year="2015", color="Dark Maroon"):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def car_info(self):
        return f"This is a {self.color}{self.model} from {self.year}"

p = Car()
print(p.car_info())
car2 = Car('Ford', " Mustang", 1969, 'Red')
print(car2.car_info())

