""" Python has a module named time to handle time-related tasks.
To use functions defined in the module, we need to import the module first.

The time() function returns the number of seconds passed since epoch.

"""

import time
seconds = time.time()
print(seconds)


""" The time.ctime() function takes seconds passed since epoch as an argument and returns a string representing local time. """

seconds = 2365225768.4618235
local_time = time.ctime(seconds)
print("Local time: ", local_time)

""" The sleep() function suspends (delays) execution of the current thread for the given number of seconds. """

import time
print("Printed Immediately")
time.sleep(3)
print("Print after 3 second")

