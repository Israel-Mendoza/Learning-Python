import pytz
from datetime import datetime

naive_dt = datetime.now()
print(f"Naive dt: {naive_dt}")

# Localizing a naive dt
my_tz = pytz.timezone("America/Mexico_City")
aware_dt = my_tz.localize(naive_dt)
print(f"Aware dt: {aware_dt}")

# Calculating time from aware dt
istambul_tz = pytz.timezone("Asia/Istanbul")
print(f"Local tz as timezone for Istambul: {aware_dt.astimezone(istambul_tz)}")
print()

##############################

naive = datetime.now()
print(f"Naive dt: {naive}")

my_tz = pytz.timezone("America/Mexico_City")

aware = my_tz.localize(naive)
print(f"Aware dt: {aware}")

istambul_tz = pytz.timezone("Asia/Istanbul")
print(f"Local tz as timezone for Istambul: {aware_dt.astimezone(istambul_tz)}")
print()
