# Overriding parent Method

# Creating a class named Element
class Element:
    # Defining a constructor method that initializes the class attributes
    def __init__(self, name, symbol):
        self.name = name  # Initializing the name attribute
        self.symbol = symbol  # Initializing the symbol attribute

    # Defining a method that returns the name and symbol of the element
    def element_info(self):
        return f"{self.name} ({self.symbol})"

# Creating a class named Food that inherits from the Element class
class Food(Element):
    # Defining a constructor method that initializes the class attributes, including those inherited from the parent class
    def __init__(self, name='Burger', symbol="salad", quantity=1, city='Dhaka', country='Bangladesh', gender='male'):
        super().__init__(name, symbol)  # Calling the constructor of the parent class to initialize name and symbol attributes
        self.quantity = quantity  # Initializing the quantity attribute
        self.city = city  # Initializing the city attribute
        self.country = country  # Initializing the country attribute
        self.gender = gender  # Initializing the gender attribute

    # Defining a method that returns the food information, including the gender of the person eating, name, symbol, quantity, city, and country
    def food_info(self):
        e = 'heavy Weight Food' if self.gender == 'male' else 'She'  # Conditional statement to check the gender and assign a string value
        return f"{e} is having {self.name} with {self.symbol}, where the quantity is {self.quantity}.Location: {self.city}, {self.country}"

# Creating instances of the Food class
s1 = Food('Pizza', 'Saussage', 4,"Dhaka", "Bangladesh", "female")  # Initializing attributes with specific values
s2 = Food('pasta', 'cheese', 2, "California", "USA", "male")  # Initializing attributes with specific values

# Printing the food information of both instances
print(s1.food_info())
print(s2.food_info())
