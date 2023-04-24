# Single Inheritance

class Flag:  # Base Class
    def flag_info(self):
        print("Inside Flag class")

# Derive Class
class Color(Flag):
    def color_info(self):
        print("Inside Color Class")

# create object of flag
flag = Flag()

# Access the Flag info using color object
flag.flag_info()

color = Color()
color.color_info()

