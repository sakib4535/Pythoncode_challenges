# Method to modify class default values

class Human:
    def __init__(self, name='Kuddus',age=90,country="Barmuda",city="Polando"):
        self.name = name
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def information(self):
        return f"{self.name} is { self.age} years old. He lives in {self.city}, {self.country}"
    def add_skill(self, skill):
        self.skills.append(skill)

h = Human()
print(h.information())
h.add_skill("Coding")
h.add_skill("Running")

h1 = Human("sakib", 40, "Australia", "Brisbane")
print(h1.information())

