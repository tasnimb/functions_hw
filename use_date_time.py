# example file for working with date information
from datetime import date
from datetime import time
from datetime import datetime


# date objects
today = date.today()

# today's date from the simple today() method from the date class
print("Today's date is:", today)

# print out the date's individual components
print("Date components: ", today.day, today.month, today.year)

# retrieve today's weekday (0 = Monday, 6 = Sunday)
print("Today's weekday number is: ", today.weekday())
days = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]
print("Which is a: ", days[today.weekday()])

## Date time objects
# Get today's date from datetime class
today = datetime.now()
print("The current day and time is:", today)

# Get the current time
t = datetime.time(datetime.now())
print(t)

print("The current time is:", today.ctime())
