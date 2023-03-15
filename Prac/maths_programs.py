def factors(b):
    for i in range(1, b+1):
        if b % i == 0:
            print(i)

if __name__ == "__main__":
    b = input(" Please Enter The Number: ")
    b = float(b)

    if b > 0 and b.is_integer():
        factors(int(b))
    else:
        print("Wrong Bro")

def multi_table(a):

    for i in range(1,11):
        print('{0} x {1} = {2}'.format(a, i, a*i))

if __name__ == "__main__":
    a = input('Enter a number: ')
    multi_table(float(a))


"""Quadratic Equation"""

def roots(a,b,c):

    D = (b*b - 4*a*c)**0.5
    x_1 = (-b + D)/(2*a)
    x_2 = (-b - D)/(2*a)

    print('x1: {0}'.format(x_1))
    print('x2: {0}'.format(x_2))

if __name__ == "__main__":
    a = input("Enter a: ")
    b = input("Enter b: ")
    c = input("Enter c: ")
    roots(float(a), float(b), float(c))

def roots(a,b,c):

    D = (b*b - 4*a*c) ** 0.5
    x1 = (-b + D)/(2*a)
    x2 = (-b - D)/(2*a)

    print("x1: {0}".format(x1))
    print("x2: {0}".format(x2))

if __name__ == "__main__":
    a = input("Enter a: ")
    b = input("Enter b: ")
    c = input("Enter c; ")
    roots(float(a),float(b),float(c))

"""Fraction Operation"""

from fractions import Fraction

def add(a,b):
    print("result of Addition: {0}".format(a+b))
def subtract(a,b):
    print("Result of Subtract: {0}".format(a-b))
def multiply(a,b):
    print("Result of Multiply: {0}".format(a*b))
def division(a,b):
    print("Result of Division: {0}".format(a/b))

if __name__ == "__main__":
    a = Fraction(input("Enter first fraction: "))
    b = Fraction(input("Enter second fraction: "))
    op = input("Operation to perform - Add, Subtract, Divide, Multiply")
    if op == 'Add':
        add(a,b)
    if op == 'Subtract':
        subtract(a,b)
    if op == 'Divide':
        division(a,b)
    if op == 'Multiply':
        multiply(a,b)

