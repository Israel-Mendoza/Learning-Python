import pytz
from datetime import datetime

"""The PYTZ module contains the time zone database in it's code."""

for tz in pytz.all_timezones:
    print(tz)

# Africa/Abidjan
# Africa/Accra
# Africa/Addis_Ababa
# Africa/Algiers
# Africa/Asmara
# Africa/Asmera
# Africa/Bamako
# Africa/Bangui
# Africa/Banjul
# .
# .
# .
# US/Mountain
# US/Pacific
# US/Samoa
# UTC
# Universal
# W-SU
# WET
# Zulu

for key in pytz.country_names:
    print(f"{key}: {pytz.country_names[key]}")
    if key in pytz.country_timezones:
        for time_zone in pytz.country_timezones[key]:
            tz_pytz = pytz.timezone(time_zone)
            local_time = datetime.now(tz=tz_pytz)
            print(f"\t{time_zone} ==> {local_time.strftime('%A %B %d, %Y -- %I:%M:%S %p')}")
# AD: Andorra
# 	Europe/Andorra ==> Friday September 03, 2021 -- 05:45:29 AM
# AE: United Arab Emirates
# 	Asia/Dubai ==> Friday September 03, 2021 -- 07:45:29 AM
# AF: Afghanistan
# 	Asia/Kabul ==> Friday September 03, 2021 -- 08:15:29 AM
# AG: Antigua & Barbuda
# 	America/Antigua ==> Thursday September 02, 2021 -- 11:45:29 PM
# AI: Anguilla
# 	America/Anguilla ==> Thursday September 02, 2021 -- 11:45:29 PM
# .
# .
# .
# UG: Uganda
# 	Africa/Kampala ==> Friday September 03, 2021 -- 06:45:29 AM
# US: United States
# 	America/New_York ==> Thursday September 02, 2021 -- 11:45:29 PM
# 	America/Detroit ==> Thursday September 02, 2021 -- 11:45:29 PM
# 	America/Kentucky/Louisville ==> Thursday September 02, 2021 -- 11:45:29 PM
# 	America/Kentucky/Monticello ==> Thursday September 02, 2021 -- 11:45:29 PM
# 	America/Indiana/Indianapolis ==> Thursday September 02, 2021 -- 11:45:29 PM
# 	America/Indiana/Vevay ==> Thursday September 02, 2021 -- 11:45:29 PM
# 	America/Chicago ==> Thursday September 02, 2021 -- 10:45:29 PM
# 	America/Indiana/Tell_City ==> Thursday September 02, 2021 -- 10:45:29 PM
# 	America/Indiana/Knox ==> Thursday September 02, 2021 -- 10:45:29 PM
# 	America/Menominee ==> Thursday September 02, 2021 -- 10:45:29 PM
# 	America/North_Dakota/Center ==> Thursday September 02, 2021 -- 10:45:29 PM
# 	America/Denver ==> Thursday September 02, 2021 -- 09:45:29 PM
# 	America/Boise ==> Thursday September 02, 2021 -- 09:45:29 PM
# 	America/Phoenix ==> Thursday September 02, 2021 -- 08:45:29 PM
# 	America/Los_Angeles ==> Thursday September 02, 2021 -- 08:45:29 PM
# 	America/Anchorage ==> Thursday September 02, 2021 -- 07:45:29 PM
# 	America/Juneau ==> Thursday September 02, 2021 -- 07:45:29 PM
# 	Pacific/Honolulu ==> Thursday September 02, 2021 -- 05:45:29 PM
# UY: Uruguay
# 	America/Montevideo ==> Friday September 03, 2021 -- 12:45:29 AM
# UZ: Uzbekistan
# 	Asia/Samarkand ==> Friday September 03, 2021 -- 08:45:29 AM
# 	Asia/Tashkent ==> Friday September 03, 2021 -- 08:45:29 AM
# VA: Vatican City
# 	Europe/Vatican ==> Friday September 03, 2021 -- 05:45:29 AM
# VC: St Vincent
# 	America/St_Vincent ==> Thursday September 02, 2021 -- 11:45:29 PM
# VE: Venezuela
# 	America/Caracas ==> Thursday September 02, 2021 -- 11:45:29 PM
# VG: Virgin Islands (UK)
# 	America/Tortola ==> Thursday September 02, 2021 -- 11:45:29 PM
# VI: Virgin Islands (US)
# 	America/St_Thomas ==> Thursday September 02, 2021 -- 11:45:29 PM
# VN: Vietnam
# 	Asia/Ho_Chi_Minh ==> Friday September 03, 2021 -- 10:45:29 AM
# VU: Vanuatu
# 	Pacific/Efate ==> Friday September 03, 2021 -- 02:45:29 PM
# WF: Wallis & Futuna
# 	Pacific/Wallis ==> Friday September 03, 2021 -- 03:45:29 PM
# WS: Samoa (western)
# 	Pacific/Apia ==> Friday September 03, 2021 -- 04:45:29 PM
# YE: Yemen
# 	Asia/Aden ==> Friday September 03, 2021 -- 06:45:29 AM
# YT: Mayotte
# 	Indian/Mayotte ==> Friday September 03, 2021 -- 06:45:29 AM
# ZA: South Africa
# 	Africa/Johannesburg ==> Friday September 03, 2021 -- 05:45:29 AM
# ZM: Zambia
# 	Africa/Lusaka ==> Friday September 03, 2021 -- 05:45:29 AM
# ZW: Zimbabwe
# 	Africa/Harare ==> Friday September 03, 2021 -- 05:45:29 AM
