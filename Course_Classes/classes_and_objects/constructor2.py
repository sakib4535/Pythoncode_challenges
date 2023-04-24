# Constructor without parameters (Non-parameterized operation)

"""In this class, the __init__ method is a non-parameterized constructor that initializes the x and y coordinates of the point to 0.
The distance_from_origin method calculates the distance between the point and the origin (0, 0) using the Pythagorean theorem.

Now suppose you want to find the distance between two points, p1 and p2, on the x-y plane.
You can create two Point objects and set their x and y coordinates: """

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
    def distance_from_origin(self):
        return (self.x**2 + self.y**2)**0.5

p1 = Point()
p1.x = 3
p1.y = 4

p2 = Point()
p2.x = -1
p2.y = 2

distance = ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5
print(distance)


########################################################

# Another Example

class Factorial:
    def __init__(self):
        self.n = 0
        self.result = 1

    def calculate_factorial(self):
        if self.n < 0:
            return "Error: Factorial of negative numbers is undefined"
        elif self.n == 0:
            return 1
        else:
            for i in range(1, self.n+1):
                self.result *= i
            return self.result



fact = Factorial()
fact.n = 5
print(fact.calculate_factorial())