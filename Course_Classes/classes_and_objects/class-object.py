# Creating Class and Object in Python
class GraduateStudent:
    species = "students"  # class attribute

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate The Class
sakib = GraduateStudent("Sakib", 20)
robin = GraduateStudent("Robin", 23)
lucy = GraduateStudent("lucy", 25)
roony = GraduateStudent("Roony", 30)

# Access the class attributes
print("Ismail is a {}".format(sakib.__class__.species))  # Ismail is a student
print("Ayon is also a {}".format(robin.__class__.species)) # Ayon is a student

#######################################################################

# Alternative Code

class Employee:
    
    employee_count=0  # class attribute

    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num
        Employee.employee_count += 1

    def printEmployeeData(self):
        print("Name: ", self.name, "ID: ", self.id_num)

e = Employee("John", 1001)
e.printEmployeeData()        # Name: John, ID: 1001






