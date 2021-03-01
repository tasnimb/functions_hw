# example file for formatting time and date output

from datetime import datetime



# time and dates can be formatted using a set of predefined string control codes
now = datetime.now()
#print(now.strftime())
#### Date formatting ####
# %y/%y - Year, %a/%A - weekday, %b/%B = month, %d - day of month

print(now.strftime("The current year is: %Y"))
print(now.strftime(("%a, %d %B, %y")))

# %c = locale's date and time, %x - locale's date, %X - locale's time
print(now.strftime("locale date and time: %c"))
print(now.strftime("locale date: %x"))
print(now.strftime("locale time: %X"))

#### Time formatting ####
# %I/%H - 12/24 Hour, %M - minute, %s - second, %p - locale's AM/PM
print(now.strftime("Current time: %I:%M:%S %p"))
print(now.strftime("24-hour time: %H:%M"))
