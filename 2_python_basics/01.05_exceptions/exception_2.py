# Task 4

from datetime import datetime, timedelta
from dateutil import tz

def add_days_with_timezone(date, days, timezone_str):
    my_timezone = tz.gettz(timezone_str)
    if my_timezone == None:
        raise ValueError("Invalid timezone")
    
    date_with_timezone = date.astimezone(my_timezone)
    
    result_date = date_with_timezone + timedelta(days=days)
    
    return result_date

dt = datetime.now()
new_dt = add_days_with_timezone(dt, 12, "Europe/Berlin")
print(new_dt)