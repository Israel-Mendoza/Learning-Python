import pytz
import zoneinfo
from datetime import datetime

# Staring with naive datetime objects
local_time = datetime.now()
utc_time = datetime.utcnow()

# Printing the naive objects. Notice how there's no TZ info:
print(f"Naive local time: {local_time}")
print(f"Naive UTC time: {utc_time}")
# Naive local time: 2021-09-02 23:32:57.661888 <-- No TZ info
# Naive UTC time: 2021-09-03 04:32:57.661893 <-- No TZ info

# Converting naive datetime objects to aware ones using pytz's timezone function.
# Notice how the "replace" method returns a NEW datetime object.
aware_local_time_pytz = local_time.replace(tzinfo=pytz.timezone("America/Mexico_City"))
aware_utc_time_pytz = utc_time.replace(tzinfo=pytz.timezone("UTC"))

# Converting naive datetime objects to aware ones using zoneinfo's ZoneInfo class.
# Again, notice how the "replace" method returns a NEW datetime object.
aware_local_time = local_time.replace(tzinfo=zoneinfo.ZoneInfo("America/Mexico_City"))
aware_utc_time = utc_time.replace(tzinfo=zoneinfo.ZoneInfo("UTC"))

# Printing the aware objects. Notice how there is TZ info now.
print(f"Aware local time (PYTZ): {aware_local_time_pytz}")
print(f"Aware local time (ZoneInfo): {aware_local_time}")
# Aware local time (PYTZ): 2021-09-02 23:32:57.661888-06:37 <-- TZ info
# Aware local time (ZoneInfo): 2021-09-02 23:32:57.661888-05:00 <-- TZ info
print(f"Aware UTC time (ZoneInfo): {aware_utc_time}")
print(f"Aware UTC time (PYTZ): {aware_utc_time_pytz}")
# Aware UTC time (ZoneInfo): 2021-09-03 04:32:57.661893+00:00 <-- TZ info
# Aware UTC time (PYTZ): 2021-09-03 04:32:57.661893+00:00 <-- TZ info
