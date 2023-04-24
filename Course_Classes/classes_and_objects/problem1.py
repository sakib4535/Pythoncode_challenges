"""Problem: Implement a class that represents a polynomial function of degree n.
The class should have methods for evaluating the polynomial function at a given point,
finding the derivative of the function, and finding the roots of the function."""


class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

# This method takes a single argument x and returns the value of the polynomial function evaluated at x.
    def evaluate(self, x):
        result = 0
        for i in range(len(self.coefficients)):
            result += self.coefficients[i] * (x ** i)
        return result

# This method takes a single argument x and returns the value of the polynomial function evaluated at x.
    def derivative(self):
        derivatives = []
        for i in range(1,len(self.coefficients)):
            derivatives.append(i * self.coefficients[i])
        return Polynomial(derivatives)

# This method finds and returns the roots (i.e. zeros) of the polynomial function. It first checks if the polynomial is of degree 1 or 2, and then uses the quadratic formula to compute the roots if the polynomial is of degree 2 and the discriminant is non-negative.
    def roots(self):
        if self.degree() == 1:
            return [-self.coefficients[0] / self.coefficients[1]]
        elif self.degree() == 2:
            a,b,c = self.coefficients
            discriminant = b **2 - 4 * a * c
            if discriminant >= 0:
                root1 = (-b + discriminant ** 0.5) / (2*a)
                root2 = (-b - discriminant ** 0.5)/ (2*a)
                return [root1,root2]
            else:
                return []
        else:
            return []

    def degree(self):
        return len(self.coefficients) - 1

p = Polynomial([-1,3,5,6])
result = p.evaluate(2)
print(result)
# This computes the derivative of the polynomial function represented by the p object, creates a new Polynomial object to represent it, evaluates the derivative at x = 2, and prints the result.
dp = p.derivative()
result = dp.evaluate(2)
print(result)

roots = p.roots()
print(roots)
