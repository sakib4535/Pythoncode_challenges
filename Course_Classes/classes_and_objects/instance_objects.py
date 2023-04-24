# Creating Instance Objects

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def info(self):     # Instance Method
        print("Employee ID is", self.id, "and name is", self.name)

    # Instance Method
    def department(self):
        print("Employee of IT Department")

emp = Employee(19118, "Amy")
emp.info()
emp.department()

##########################################

class House:
    'Common Base Class of all students'
    house_count=0

    def __init__(self, name, id):
        self.name = name
        self.id = id
        House.house_count += 1

    def printHomeData(self):
        print("Name: ", self.name, "ID: ", self.id)

h1 = House("Nahar House", 1010)
h2 = House("Bashar Villa", 2020)
h3 = House("Jilla Villa", 2021)

print("Total Student: ", House.house_count)

h1.printHomeData()
h2.printHomeData()
h3.printHomeData()

""" Instead of using the normal statements to access attributes, you can use the following functions:

* **`getattr(obj, name[, default])`** − to access the attribute of object. 

* **`hasattr(obj,name)`** − to check if an attribute exists or not. 

* **`setattr(obj,name,value)`** − to set an attribute. If attribute does not exist, then it would be created. 

* **`delattr(obj, name)`** − to delete an attribute. 

**Example:**

```python
hasattr(std1, 'id') # Returns true if 'id' attribute exists
getattr(std1, 'id') # Returns value of 'id' attribute
setattr(std1, 'id', 104) # Set attribute 'id' 104
delattr(std1, 'id') # Delete attribute 'id'
``` """

