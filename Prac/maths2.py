def multi_table(a):
    for i in range(1,11):
        print("{0} x {1} = {2}".format(a, i, a*i))

if __name__ == "__main__":

    while True:
        a = input("Enter a Number: ")
        multi_table(float(a))

        answer = input("Do you wanna Exit? (y) or (n)")
        if answer == 'y':
            break


l = [1,2,3,4,5,6]

for item in l:
    print(item)

for index, item in enumerate(l):
    print(index, item)

x  = [23, 34, 56, 67, 78, 45, 34, 23, 12]
y = [23, 41, 34, 63, 34, 76, 56, 88, 90]

from pylab import plot, show, legend, title, xlabel, ylabel, axis
import matplotlib.pyplot as plt

plot(x, y, marker= 'o')
plt.xlabel("Numbers From Aliens")
plt.ylabel("Higher Authority Members")
show()

nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3, 55.6, 57.4, 51.2, 55.2, 51.2]
years = range(2000, 2018)
plot(years, nyc_temp, marker='*')
show()

nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]

months = range(1,13)
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
title("Average monthly Temperature in Newyork")
xlabel("Month")
ylabel("Temperature")
legend([2000, 2006, 2012])
show()

nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
axis(ymin=0)
plot(nyc_temp, marker='o')


