"""
time.struct_time(tm_year=2018, tm_mon=12, tm_mday=27,
                    tm_hour=6, tm_min=35, tm_sec=17,
                    tm_wday=3, tm_yday=361, tm_isdst=0)

                    """

import time

# get the current time in seconds since the Epoch
current_time = time.time()

# convert the current time to a struct_time object in local time
local_time = time.localtime(current_time)

# print the current time and local time as struct_time objects
print("Current time as seconds since Epoch:", current_time)
print("Local time as struct_time object:", local_time)

# access the different fields of the struct_time object
print("Year:", local_time.tm_year)
print("Month:", local_time.tm_mon)
print("Day:", local_time.tm_mday)
print("Hour:", local_time.tm_hour)
print("Minute:", local_time.tm_min)
print("Second:", local_time.tm_sec)
print("Weekday (Monday is 0):", local_time.tm_wday)
print("Day of year:", local_time.tm_yday)
print("Is daylight saving time?", local_time.tm_isdst)

##############################################################################################
print("____________________________________________________________________________")
import time

# create a struct_time object representing January 1, 2022, 00:00:00 UTC
my_time = time.struct_time((2022, 1, 1, 0, 0, 0, 4, 1, -1))

# access the different fields of the struct_time object
print("Year:", my_time.tm_year)
print("Month:", my_time.tm_mon)
print("Day:", my_time.tm_mday)
print("Hour:", my_time.tm_hour)
print("Minute:", my_time.tm_min)
print("Second:", my_time.tm_sec)
print("Weekday (Monday is 0):", my_time.tm_wday)
print("Day of year:", my_time.tm_yday)
print("Is daylight saving time?", my_time.tm_isdst)

print("____________________________________________________________________________")


import time

# create a string representing January 1, 2022, 00:00:00 UTC
time_string = "2022-01-01 00:00:00"

# convert the string to a struct_time object
my_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")

# access the different fields of the struct_time object
print("Year:", my_time.tm_year)
print("Month:", my_time.tm_mon)
print("Day:", my_time.tm_mday)
print("Hour:", my_time.tm_hour)
print("Minute:", my_time.tm_min)
print("Second:", my_time.tm_sec)
print("Weekday (Monday is 0):", my_time.tm_wday)
print("Day of year:", my_time.tm_yday)
print("Is daylight saving time?", my_time.tm_isdst)
