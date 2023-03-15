from fractions import Fraction

f = Fraction(3,4) + 1 - Fraction(3,2)
print(f)

a = 2 + 3j
print(type(a))

b = complex(2,3)
print(b)

c1 = complex(3,4)
c2 = complex(4,6)

print(c1 + c2)

print(c1.real)
print(c1.imag)

print(c1.conjugate())
print(c2.conjugate())

print((c1.real ** 2 + c1.imag ** 2) ** 0.5)

print(abs(c1))
print(abs(c2))

try:
    a = Fraction(input("Enter a Fraction: "))
    print(a)
except ZeroDivisionError:
    print("Invalid Fraction")











































def is_factor(a,b):
    if b % a == 0:
        return True
    else:
        return False

print(is_factor(56,890))




def factors(b):

    for i in range(1, b+1):
        if b % i == 0:
            print(i)

if __name__ == "__main__":

    b = input("Your Number: ")
    b = float(b)

    if b > 0 and b.is_integer():
        factors(int(b))
    else:
        print("Invalid Number")

def factors(b):
    for i in range(1, b+1):
        if b % i == 0:
            print(i)

if __name__ == "__main__":
    b = input("Please Enter the Input: ")
    b = float(b)

    if b > 0 and b.is_integer():
        factors(int(b))
    else:
        print("Invalid Number")

