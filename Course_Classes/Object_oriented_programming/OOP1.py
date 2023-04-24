class Person:
    """This is a person class"""
    def __init__(self, name, education, reflection):
        self.name = name
        self.education = education
        self.reflection = reflection

    def __str__(self):
        return f"My self Mr. {self.name} and came from {self.education}. I am looking for {self.reflection }."

class Student(Person):
    """This is a student class that inherits from Person"""
    def learn(self):
        print("Welcome to my home Dear Friend")

# Create an instance of Student class and call the learn method
s = Student("Robin", "University of Dhaka", "a Machine to kill")
s.learn()
print(s.name, s.reflection, s.education)
print(s)
