class ComplexNumber:
    def __init__(self,r=0,i=1):
        self.real = r
        self.imaginary = i

    def get_data(self):
        print("{0}+{1}j".format(self.real, self.imaginary))

c1 = ComplexNumber(5,6)
c1.get_data()

##################################

