# Playing with date times and time zones

import pytz
from datetime import datetime
from os import system, name

tz_codes = {
    1: "America/Los_Angeles",
    2: "America/Mexico_City",
    3: "America/New_York",
    4: "Europe/Paris",
    5: "Europe/Istanbul",
    6: "Europe/Moscow",
    7: "Asia/Kolkata",
    8: "Asia/Seoul",
    9: "Asia/Tokyo"
}

places = {
    0: "Exit",
    1: "Los Angeles",
    2: "Mexico City",
    3: "New York",
    4: "Paris",
    5: "Istambul",
    6: "Moscow",
    7: "Kolkata",
    8: "Seoul",
    9: "Tokyo"
}


def display_options(places_dict: dict):
    """Prints the key and value of the passed dict"""
    print("Available options: ")
    for option, place in places_dict.items():
        if option == 0:
            continue
        print(f"\t{option}. {place}")


def display_time(tz_dict: dict, desired_location: int, local_tz_name: str ):
    """
    Given a desired location, displays:
        1. The current UTC time
        2. The current local time
        3. The current time for the desired location

    Args:
        tz_dict [dict]: A dictionary containing the tz names in pytz
        desired_location [int]: A valid int key in the tz_codes dict
        local_tz_name [str]: The name of the local tz in pytz
    """
    tz_code = tz_dict[desired_location]
    current_utc = datetime.now(tz=pytz.utc)
    local_time = current_utc.astimezone(pytz.timezone(local_tz_name))
    desired_time = current_utc.astimezone(pytz.timezone(tz_code))
    print(f"\nCurrent UTC time:\t\t{current_utc.strftime('%A %B %d, %Y  %I:%M:%S %p')}")
    print(f"Current local time:\t\t{local_time.strftime('%A %B %d, %Y  %I:%M:%S %p')}")
    print(f"Current time in {places[desired_location]}: {desired_time.strftime('%A %B %d, %Y  %I:%M:%S %p')}\n")


def clear_terminal():
    """Clears the terminal for Linux/macOS and Windows systems"""
    if name == "nt":
        system("cls")
    else:
        system("clear")


# Main app loop:
while True:
    clear_terminal()
    display_options(places)
    message = "Enter desired location ('q' or 0 to quit): "
    location = input(message)
    if location == "0" or location == "q":
        print("\nGoodbye!\n")
        break
    for index, city in places.items():
        if location.lower() in city.lower():
            location = index
            break
    else:
        try:
            location = int(location)
        except ValueError:
            print("\nThat was not a valid option! Try again...\n")
            continue
    display_time(tz_codes, location, "America/Mexico_City")
    input("Press ENTER to continue...")
