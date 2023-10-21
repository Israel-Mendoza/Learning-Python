import pytz
import zoneinfo
from datetime import datetime

"""
Using time zone objects - Starting with LOCAL time.
In the end, we will be using the pytz and zoneinfo only to make our datetime objects timezone aware.
"""

country_timezone = "America/Mexico_City"

tz_zoneinfo = zoneinfo.ZoneInfo(country_timezone)
tz_pytz = pytz.timezone(country_timezone)

# Printing the returned objects:
print(f"Time zone object created using pytz: {type(tz_pytz)} - {tz_pytz}")
print(f"Time zone object created using ZoneInfo: {type(tz_zoneinfo)} - {tz_zoneinfo}")
# Time zone object created using pytz: <class 'pytz.tzfile.America/Mexico_City'> - America/Mexico_City
# Time zone object created using ZoneInfo: <class 'zoneinfo.ZoneInfo'> - America/Mexico_City

# To reate timezone aware datetime objects we must use a time zone object 
# like the ones we just created, passing it to the tx parameter:
local_time_using_pytz = datetime.now(tz=tz_pytz)
local_time_using_zoneinfo = datetime.now(tz=tz_zoneinfo)

# Printing the returned datetime objects:
print(f"Using the 'pytz.tzfile.America/Mexico_City' time zone object: {type(local_time_using_pytz)} - {local_time_using_pytz}")
print(f"Using the 'zoneinfo.ZoneInfo' time zone object: {type(local_time_using_zoneinfo)} - {local_time_using_zoneinfo}")
# Using the 'pytz.tzfile.America/Mexico_City' time zone object: <class 'datetime.datetime'> - 2021-09-02 23:02:37.355436-05:00
# Using the 'zoneinfo.ZoneInfo' time zone object: <class 'datetime.datetime'> - 2021-09-02 23:02:37.355516-05:00

# Printing the local time using the datetime objects. Using the "string from time" method.
print(f"The time in '{country_timezone}' is {local_time_using_pytz.strftime('%A %B %d, %Y -- %I:%M:%S %p')}")
print(f"The time in '{country_timezone}' is {local_time_using_zoneinfo.strftime('%A %B %d, %Y -- %I:%M:%S %p')}")
# The time in 'America/Mexico_City' is Thursday September 02, 2021 -- 11:02:37 PM
# The time in 'America/Mexico_City' is Thursday September 02, 2021 -- 11:02:37 PM

# Using the local datetime object to print the current UTC time:
print(f"{type(local_time_using_pytz)} - {local_time_using_pytz.utcnow().strftime('%A %B %d, %Y -- %I:%M:%S %p')}")
print(f"{type(local_time_using_zoneinfo)} - {local_time_using_zoneinfo.utcnow().strftime('%A %B %d, %Y -- %I:%M:%S %p')}")
# <class 'datetime.datetime'> - Friday September 03, 2021 -- 04:02:37 AM
# <class 'datetime.datetime'> - Friday September 03, 2021 -- 04:02:37 AM
