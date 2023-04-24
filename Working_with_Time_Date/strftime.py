""" In this class, you will learn to convert date, time and datetime objects to its equivalent string """

# Example 1
""" datetime object containing current date and time to different string formats. """

from datetime import datetime

now = datetime.now()  # current date and time
print(now)

year = now.strftime("%Y")
print(year)

day = now.strftime("%d")
print(day)

time = now.strftime("%H:%M:%Y")
print(day)
time = now.strftime("%H:%M:%S")
print("time:", time)

date_time1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time1)

date_time2 = now.strftime("%d/%m/%Y, %H:%M:%S")
print("date and time:",date_time2)



"""  
In the above program, %Y, %m, %d etc. are format codes. The strftime() method takes one or more format codes as an 
argument and returns a formatted string based on it.

object of datetime class can access strftime() method.

"""

# Example 2:

from datetime import datetime

timestamp = 1592019301
date_time = datetime.fromtimestamp(timestamp)

print(date_time)

d = date_time.strftime("%d %b, %Y") # %b: abbreviate month name, %d: day of the month as a zero padded decimal
print("Output: ", d)

d = date_time.strftime("%d %B, %Y")  # %B: Full month name
print("Output: ", d)

d = date_time.strftime("%I%p")  # %I: Hour (12-hour clock) as a decimal number.
print("Output: ", d)

""" The strftime() class method takes two arguments:

- string (that be converted to datetime)
- format code
"""

"""
%a	Abbreviated weekday name.	Sun, Mon, ...
%A	Full weekday name.	Sunday, Monday, ...
%w	Weekday as a decimal number.	0, 1, ..., 6
%d	Day of the month as a zero-padded decimal.	01, 02, ..., 31
%-d	Day of the month as a decimal number.	1, 2, ..., 30
%b	Abbreviated month name.	Jan, Feb, ..., Dec
%B	Full month name.	January, February, ...
%m	Month as a zero-padded decimal number.	01, 02, ..., 12
%-m	Month as a decimal number.	1, 2, ..., 12
%y	Year without century as a zero-padded decimal number.	00, 01, ..., 99
%-y	Year without century as a decimal number.	0, 1, ..., 99
%Y	Year with century as a decimal number.	2013, 2019 etc.
%H	Hour (24-hour clock) as a zero-padded decimal number.	00, 01, ..., 23
%-H	Hour (24-hour clock) as a decimal number.	0, 1, ..., 23
%I	Hour (12-hour clock) as a zero-padded decimal number.	01, 02, ..., 12
%-I	Hour (12-hour clock) as a decimal number.	1, 2, ... 12
%p	Locale’s AM or PM.	AM, PM
%M	Minute as a zero-padded decimal number.	00, 01, ..., 59
%-M	Minute as a decimal number.	0, 1, ..., 59
%S	Second as a zero-padded decimal number.	00, 01, ..., 59
%-S	Second as a decimal number.	0, 1, ..., 59
%f	Microsecond as a decimal number, zero-padded on the left.	000000 - 999999
%z	UTC offset in the form +HHMM or -HHMM.	
%Z	Time zone name.	
%j	Day of the year as a zero-padded decimal number.	001, 002, ..., 366
%-j	Day of the year as a decimal number.	1, 2, ..., 366
%U	Week number of the year (Sunday as the first day of the week). All days in a new year preceding the first Sunday are considered to be in week 0.	00, 01, ..., 53
%U	Week number of the year (Monday as the first day of the week). All days in a new year preceding the first Monday are considered to be in week 0.	00, 01, ..., 53
%c	Locale’s appropriate date and time representation.	Mon Sep 30 07:06:05 2013
%x	Locale’s appropriate date representation.	09/30/13
%X	Locale’s appropriate time representation.	07:06:05
%%	A literal '%' character.	%


"""