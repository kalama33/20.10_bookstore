
# calendar.isleap() method

import calendar

calendar.isleap(2024)

my_year = 2024

if calendar.isleap(my_year):
    print(f'Year {my_year} is a leap year')
else:
    print(f"Year {my_year} is not a leap year")
    
print("yes" if calendar.isleap(my_year) else "No")

### calendar.month() Method

# It is used to generate a string representation of a calendar.
# It takes two integer:
# 1. the year 
# 2 . month

import calendar
print(calendar.month(2022,12))

# It can be customized
# 1. setfirstweekday (weekday)
# 2. firstweekday

calendar.setfirstweekday(1)
print(calendar.month(2033, 12))
print(calendar.firstweekday())

calendar.SUNDAY

# Arithmetics with Datetime

from datetime import datetime
halloween2019 = datetime(2019, 10, 31)
halloween2019

# != < >

from dateutil import tz