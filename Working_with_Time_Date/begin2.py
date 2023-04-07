""" We can also create date objects from a timestamp. """

from datetime import date
timestamp = date.fromtimestamp(2123453123)
print(timestamp)

from datetime import date

today = date.today()
print("Today Year: ", today.year)
print("Today Month", today.month)
print("Today Day: ", today.day)

""" A time object instantiated from the time class represents the local time. """

from datetime import time

a = time()
print(a)

b = time(12, 21, 56)
print(b)

c = time(hour=11, minute=12, second=56)
print(c)

# Example 7: Time object to represent time

from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)