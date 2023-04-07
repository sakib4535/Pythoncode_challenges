""" A timedelta object represents the difference between two dates or times. """

from datetime import datetime, date

t1 = date(year=2022, month=9, day=13)
t2 = date(year=2019, month=7, day=20)
t3 = t1 - t2
print(t3)

t4 = datetime(year = 2019, month = 2, day = 22, hour = 10, minute = 19, second = 43)
t5 = datetime(year = 2021, month = 1, day = 12, hour = 22, minute = 21, second = 22)
t6 = t4 - t5
print(t6)

print("type of t3 =", type(t3))
print("type of t6 =", type(t6))

############################################################################################

# Example 12: Difference between two timedelta objects

from datetime import timedelta

t1 = timedelta(weeks = 3, days = 15, hours = 12, seconds = 53)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print("t3 =", t3)

# When you run the program, the output will be like below:


""" *You* can get the total number of seconds in a **`timedelta`** object using **`total_seconds()`** method. """
