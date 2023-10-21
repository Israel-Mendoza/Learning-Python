import time

print(f"The Epoch on this system starts at {time.strftime('%A %B %d, %Y - %I:%M:%S %p', time.gmtime(0))}")
# The Epoch on this system starts at Thursday January 01, 1970 - 12:00:00 AM

print(f"The current timezone is {time.tzname[0]} with an offset of {time.timezone}")
# The current timezone is CST with an offset of 21600


# if time.daylight != 0:
#     print("\tDaylight saving time is in effect for this location")
# else:
#     print("\tDaylight saving time is not in effect for this location.")
# # Daylight saving time is in effect for this location

msg = "" if time.daylight != 0 else "NOT "
print(f"Daylight saving time is {msg}in effect for this location")
# Daylight saving time is in effect for this location

print(f"Local time is {time.strftime('%A %B %d, %Y - %I:%M:%S %p', time.localtime())}")
# Local time is Sunday September 05, 2021 - 08:22:46 PM
print(f"UTC time is {time.strftime('%A %B %d, %Y - %I:%M:%S %p', time.gmtime())}")
# UTC time is Monday September 06, 2021 - 01:22:46 AM
