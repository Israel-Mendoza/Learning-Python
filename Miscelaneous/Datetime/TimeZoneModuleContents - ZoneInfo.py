import zoneinfo
from datetime import datetime

"""
The zoneinfo module does not directly provide time zone data, 
and instead pulls time zone information from the system time zone database or the first-party PyPI package tzdata, if available. 
Some systems, including notably Windows systems, do not have an IANA database available, 
and so for projects targeting cross-platform compatibility that require time zone data, 
it is recommended to declare a dependency on tzdata. If neither system data nor tzdata are available, 
all calls to ZoneInfo will raise ZoneInfoNotFoundError.
"""

# The time zones available to the zoneinfo module are stored in a
# set of strings returned by the zoneinfo.available_timezones() function:
print(type(zoneinfo.available_timezones()))  # <class 'set'>
print(len(zoneinfo.available_timezones()))  # 594

for timezone in zoneinfo.available_timezones():
    print(timezone)
# Asia/Qostanay
# Atlantic/St_Helena
# America/Argentina/Catamarca
# Europe/Paris
# America/Merida
# Asia/Beirut
# .
# .
# .
# Asia/Jerusalem
# America/Indiana/Indianapolis
# Asia/Yangon
# America/Dominica
# Africa/Maseru
# Chile/EasterIsland
# Etc/GMT0


# Using a zoneinfo.ZoneInfo object to create an aware datetime object:
my_aware_dt = datetime.now(tz=zoneinfo.ZoneInfo("America/Mexico_City"))

print(my_aware_dt)
# 2021-09-03 00:06:54.340648-05:00
