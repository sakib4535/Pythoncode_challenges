"""The numeric functions in the math module take real numbers/integers as arguments and
after doing the specified mathematical calculations
, it returns a number or a boolean value.

url = https://www.scaler.com/topics/math-module-in-python/ """

"""Lagrange Interpolation"""

x = [0,20,40,60,80,100]
y = [26.3, 48.5, 61.4, 71.54, 79.65, 85.43]

m = len(x)
n = m - 1

xp = float(input("Enter Number: "))
yp = 0
for i in range(n+1):
    p = 1
    for j in range(n+1):
        if j != i:
            p *= (xp - x[j])/(x[i] - x[j])
    yp += y[i]*p

print("For x = %s.2f, y=%f"%(xp,yp))


# Alternative Method

#import numpy as np

#x1 = np.array([0,20,40,60,80,100], float)
#y1 = np.array([26.3, 48.5, 61.4, 71.54, 79.65, 85.43], float)

#xp1 = float(input("Enter x: "))
#yp1 = 0

#for xi in x1:
#    p *= (xp1 - x1[j])/(x1[i] - x1[j])
#    yp1 += y1[i]*p
# print("for x = %.2f, y = %f"%(xp1,yp1))


##########################################

import numpy as np

x1 = np.array([0, 20, 40, 60, 80, 100], float)
y1 = np.array([26.3, 48.5, 61.4, 71.54, 79.65, 85.43], float)

xp1 = float(input("Enter x: "))
yp1 = 0
p = 1

for j, xi in enumerate(x1):
    if j == 0:
        p = 1
    else:
        for i in range(j):
            p *= (xp1 - x1[i])/(x1[j] - x1[i])
    yp1 += y1[j] * p

print("for x = %.2f, y = %f"%(xp1, yp1))




