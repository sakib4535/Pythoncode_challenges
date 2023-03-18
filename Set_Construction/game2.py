import random
import math
import matplotlib.pyplot as plt

def estimate_area(num_darts):

    """Estimates the area of a circle inscribe in a square using the dartboard
    method where num_darts is the number of darts to throw"""

    r = 1 #circle radius
    hits = 0 #number of darts hits inside the circle

    for i in range(num_darts):
        x = random.uniform(-r,r)
        y = random.uniform(-r,r)
        if x**2 + y**2 <= r**2:
            hits += 1

    f = hits / num_darts
    estimated_area = 4 * r**2 * f
    return estimated_area

num_darts = int(input("Enter the number of darts to throw: "))

#Estimate the area of the circle and print the result

#estimate_area = estimate_area(num_darts)
#actual_area = math.pi
#print(f"Estimate Area: {estimate_area}")
#print(f"Actual Area; {actual_area}")

# Initializing lists to hold the number of darts and the corresponding estimate area

num_darts_list = []
estimated_area_list = []

#Run Simulation with varying number of darts
for num_darts in range(10,20000,10):
    estimated_area = estimate_area(num_darts)
    num_darts_list.append(num_darts)
    estimated_area_list.append(estimated_area)

actual_area = math.pi * (1)**2
plt.plot(num_darts_list, estimated_area_list, label="Estimated Area")
plt.axhline(y=actual_area, color='r', linestyle='-', label="Actual Area")
plt.xlabel("Numbers of Darts")
plt.ylabel("Area")
plt.legend()
plt.show()