import matplotlib.pyplot as plt

def draw_graph(x,y):
    plt.plot(x,y, marker='o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitational force in newtons')
    plt.title('Gravitational force and distance')
    plt.show()

def generate_F_r():
    r = range(100,1001,50)
    F = []
    G = 6.674*(10**-11)
    m1 = 0.5
    m2 = 1.5

    for dist in r:
        force = G*(m1*m2)/(dist**2)
        F.append(force)

    draw_graph(r,F)

if __name__ == "__main__":
    generate_F_r()

from matplotlib import pyplot as plt
import math
def draw_graph(x,y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distance in meters')

    plt.ylabel('Gravitational force in newtons')
    plt.title('Gravitational force and distance')
    plt.show()

def frange(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval
    return numbers

def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8

    t_flight = 2*u*math.sin(theta)/g
    intervals = frange(0, t_flight, 0.001)
    x = []
    y = []

    for t in intervals:
        x.append(u * math.cos(theta) * t)
        y.append(u * math.sin(theta) * t - 0.5 * g * t * t)
        draw_graph(x, y)

if __name__ == '__main__':
    try:
        u = float(input('Enter the initial velocity (m/s): '))
        theta = float(input('Enter the angle of projection (degrees): '))
    except ValueError:
        print('You entered an invalid input')
    else:
        draw_trajectory(u, theta)
        plt.show()



