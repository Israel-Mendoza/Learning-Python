import pytz
import zoneinfo
from datetime import datetime

mx_city_tz_obj = pytz.timezone("America/Mexico_City")
print(f"'mx_city_tz_obj': {type(mx_city_tz_obj)} {mx_city_tz_obj}")
# 'mx_city_tz_obj': <class 'pytz.tzfile.America/Mexico_City'> America/Mexico_City

# Using the 'pytz.tzfile.America/Mexico_City' object to create an aware datetime.datetime object 
# using the localize method, which takes a naive datetime.datetime object
aware_local_time = mx_city_tz_obj.localize(datetime.now())
# Print the aware datetime.datetime object returned by the localize method
print(f"'aware_local_time': {aware_local_time}")
# 'aware_local_time': 2021-09-02 23:40:35.949442-05:00
print(f"'aware_local_time' tz_info property: {aware_local_time.tzinfo}")
# 'aware_local_time' tz_info propperty: America/Mexico_City
print()

# Naive comparison

naive_local_time = datetime.now()

print(f"'naive_local_time': {naive_local_time}")
# 'naive_local_time': 2021-09-02 23:40:35.949641
print(f"'naive_local_time' tz_info: {naive_local_time.tzinfo}")
# 'naive_local_time' tz_info: None
