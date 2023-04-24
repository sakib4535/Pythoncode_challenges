class Fraction(object):
    def __init__(self, n=0, d=1):
        self.numerator = n
        self.denominator = d

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def set_numerator(self, n):
        self.numerator = n

    def set_denominator(self, d):
        self.denominator = d

    def print_fraction(self):
        print(f"{self.numerator}/{self.denominator}")


if __name__ == "__main__":
    f = Fraction()
    f.set_numerator(2)
    f.set_denominator(5)
    f.print_fraction()


