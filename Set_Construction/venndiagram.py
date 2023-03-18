import matplotlib.pyplot as plt
from matplotlib_venn import venn2
from sympy import FiniteSet
import matplotlib.pyplot as plt

def draw_venn(sets):

    venn2(subsets=sets)
    plt.show()

if __name__ == "__main__":

    s1 = FiniteSet(1,3,5,7,9,11,13,15,17,19)
    s2 = FiniteSet(2,3,5,7,11,13,17)

    draw_venn([s1,s2])