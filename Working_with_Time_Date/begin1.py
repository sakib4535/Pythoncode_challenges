# get Current Date Time

import datetime
datetime_object = datetime.datetime.now()
"""
 classes defined in the datetime module is datetime class. 
 We then used now() method to create a datetime object containing the current local date and time.
"""
print(datetime_object)


# Getting the Current Date

date_object = datetime.date.today()
print(f"get Current Date : {date_object}")

"""
Commonly used classes in the datetime module are:

date Class
time Class
datetime Class
timedelta Class
"""

import datetime

d = datetime.date(2023, 1, 18)  # here d is a date object
print(d)

"""
date() in the above example is a constructor of the date class. The constructor takes three arguments: year, month and day.
"""

""" We can only import date class from the datetime module """

from datetime import date

d = date(2023, 4, 5)
print(d)

from datetime import date
today = date.today()
print(today)
