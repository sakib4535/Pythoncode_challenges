class ComplexLinearEquation:
    def __init__(self, re=0, im=0):
        self.re = re
        self. im = im
    def __add__(self, other):
        return ComplexLinearEquation(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + self.im * other.re
        return ComplexLinearEquation(re, im)

    def __sub__(self, other):
        return ComplexLinearEquation(self.re - other.re, self.im - other.im)

    def __abs__(self):
        return (self.re ** 2 + self.im ** 2) ** 0.5

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __lt__(self, other):
        return abs(self) <  abs(other)

    def __str__(self):
        sign = "+" if self.im >= 0 else "-"
        return f"{self.re}{sign} {abs(self.im)}i"

eq1 = ComplexLinearEquation(2, 3)
eq2 = ComplexLinearEquation(1, -2)

# Addition
result = eq1 + eq2
print(f"{eq1} + {eq2} = {result}")

# Multiplication
result = eq1 * eq2
print(f"{eq1} * {eq2} = {result}")

# Subtraction
result = eq1 - eq2
print(f"{eq1} - {eq2} = {result}")

# Modulus
result = abs(eq1)
print(f"|{eq1}| = {result}")

# Greater than
print(f"{eq1} > {eq2} = {eq1 > eq2}")

# Less than
print(f"{eq1} < {eq2} = {eq1 < eq2}")