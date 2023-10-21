from zoneinfo import ZoneInfo
from datetime import datetime

# Creating a naive datetime object
birthday = datetime(1992, 4, 9, 9, 54, 0) 
print(f"Naive birthday: {birthday}")
# Naive birthday: 1992-04-09 09:54:00

# Creating an aware datetime object out of a naive one using the datetime object's replace method:
birthday = birthday.replace(tzinfo=ZoneInfo("America/Mexico_City"))
print(f"Aware birthday {birthday}")
# Aware birthday 1992-04-09 09:54:00-06:00

# Creating an aware datetime object with a different time zone 
# to the original using the datetime object's astimezone method:
birthdate_utc = birthday.astimezone(tz=ZoneInfo("UTC"))
print(f"Aware birthday in UTC: {birthdate_utc}")
# Aware birthday in UTC: 1992-04-09 15:54:00+00:00

########################################################################################
########################################################################################

# Creating an aware datetime object with a given time (March 1st, 2020, at midnight):
aware_dt = datetime(2020, 3, 1, 0, 0, 0, tzinfo=ZoneInfo("UTC"))
print(f"Random aware UTC time: {aware_dt}")
# Random aware UTC time: 2020-03-01 00:00:00+00:00

# Creating an aware datetime object with the current UTC time:
aware_dt_utc_now = datetime.now(tz=ZoneInfo("UTC"))
print(f"Current aware UTC time: {aware_dt_utc_now}")
# Current aware UTC time: 2021-09-03 05:33:24.940399+00:00

# Converting our first datetime object from UTC to our the Mexico City time zone:
aware_dt_mx = aware_dt_utc_now.astimezone(ZoneInfo("America/Mexico_City"))
print(f"Current aware time: {aware_dt_mx}")
# Current aware local time: 2021-09-03 00:33:24.940399-05:00
