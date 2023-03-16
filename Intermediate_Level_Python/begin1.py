class gpu(object):
    def __init__(self, make, model, year, condition, price):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.price = price

    def display(self, ShowAll):
        if ShowAll:
            print("This GPU is %s %s from %s, it is %s and has %s price in Dollar " % (self.make, self.model, self.year, self.condition, self.price))
        else:
            print("This car is %s %s from %s"%(self.make, self.model, self.year))

whip = gpu('Nvidia', 'RTX 3060Ti', 2020, 'New', 399)
whip.display(True)