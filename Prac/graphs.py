import matplotlib.pyplot
from pylab import plot, savefig
def create_graph():
    x = [21,32,43,21,42]
    y = [34,25,67,77,89]

    matplotlib.pyplot.plot(x, y)
    matplotlib.pyplot.show()

if __name__ == "__main__":
    create_graph()

from pylab import plot, savefig
x = [1, 2, 3]
y = [2, 4, 6]
plot(x, y)
savefig('mygraph.png')