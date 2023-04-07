from datetime import date

today = date.today()
print(today)


# Another version

today = date.today()

d1 = today.strftime("%d/%m/%Y")
d2 = today.strftime("%B %d, %Y")
print("d2 = ", d2)
# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

# Example 3: Get the current date and time

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
