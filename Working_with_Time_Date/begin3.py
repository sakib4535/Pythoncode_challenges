""" The datetime module has a class named dateclass that can contain information from both date and time objects."""

from datetime import datetime

a = datetime(2021, 11, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)  # The first three arguments year, month and day in the datetime() constructor are mandatory
print(b)

#  Print year, month, hour, minute and timestamp

from datetime import datetime

a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("Year",a.year)
print("Month",a.month)
print("Day",a.day)
print("Hour",a.hour)
print("Minute: ",a.minute)
print("Time Stamp: ",a.timestamp())





