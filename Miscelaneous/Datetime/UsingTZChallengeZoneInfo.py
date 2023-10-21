# Playing with date times and time zones

import zoneinfo
from datetime import datetime
from os import system, name

tz_codes = {
    0: "Exit",
    1: "America/Los_Angeles",
    2: "America/Mexico_City",
    3: "America/New_York",
    4: "Europe/Paris",
    5: "Europe/Moscow",
    6: "Asia/Calcutta",
    7: "Asia/Shanghai",
    8: "Asia/Seoul",
    9: "Asia/Tokyo"
}


def clear_terminal() -> None:
    """Clears the terminal for Linux/macOS and Windows systems"""
    if name == "nt":
        system("cls")
    else:
        system("clear")


def quit_app() -> None:
    print("\nGoodbye!\n")
    quit()


def timezone_to_place_name(timezone_name: str) -> str:
    """
    Returns the name of the place contained in a time zone code.
    Examples: 
        "America/Los_Angeles" -> "Los Angeles"
        "Europe/Moscow" -> "Moscow"
        "UTC" -> "UTC"
    """
    timezone_name = timezone_name.split("/")
    if len(timezone_name) > 1:
        return " ".join(timezone_name[1].split("_"))
    else:
        return timezone_name[0]


def display_options(setting_local: bool, options_dict: dict) -> None:
    """Prints the options in a dictionary"""
    message_specific = "LOCAL" if setting_local else "DESIRED"
    print(f"Available options for {message_specific} LOCATION:\n")
    for option, description in options_dict.items():
        print(f"{option}. {timezone_to_place_name(description)}")
    print()

def ask_for_option() -> int:
    """
    Ask the user for a valid option (from 0 to 9 or 'q').
    It'll continue asking the user until a valid option is entered.
    """
    message = "Please enter an option from 1 to 9 ('q' or 0 to quit): "
    while True:
        selected_option = input(message)
        if selected_option == "0" or selected_option.lower() == "q":
            return 0
        try:
            selected_option = int(selected_option)
            if 0 < selected_option < 10:
                return selected_option
            else:
                print("That was an invalid option. Please try again...\n")
        except ValueError:
            print("That was an invalid option. Please try again...\n")


def print_timesV2(local_timezone_code: str, preferred_timezone_code: str) -> None:
    """
    Prints three lines with the current times in:
    1. The UTC time
    2. The local time (time zone name passed as an argument)
    3. The selected time (time zone name passed as an argument)
    """
    current_utc_dt = datetime.now(tz=zoneinfo.ZoneInfo("UTC"))
    current_local_dt = current_utc_dt.astimezone(tz=zoneinfo.ZoneInfo(local_timezone_code))
    current_preferred_dt = current_utc_dt.astimezone(tz=zoneinfo.ZoneInfo(preferred_timezone_code))
    datetime_format = "%a %b %d, %Y %I:%M:%S %p"
    print("\nCURRENT TIME:")
    print(f"{current_utc_dt.strftime(datetime_format)} - UTC")
    print(f"{current_local_dt.strftime(datetime_format)} - {timezone_to_place_name(local_timezone_code)}")
    print(f"{current_preferred_dt.strftime(datetime_format)} - {timezone_to_place_name(preferred_timezone_code)}")
    print()

def main():
    """Starts the application's main loop"""
    clear_terminal()
    display_options(True, tz_codes)
    if local_code_num := ask_for_option():
        local_tz_code: str = tz_codes[local_code_num]
        clear_terminal()
        while True:
            display_options(False, tz_codes)
            if selected_option := ask_for_option():
                selected_tz_code: str = tz_codes[selected_option]
                print_timesV2(local_tz_code, selected_tz_code)
                input("Press ENTER to continue...")
                clear_terminal()
            else:
                quit_app()
    else:
        quit_app()


if __name__ == "__main__":
    main()
