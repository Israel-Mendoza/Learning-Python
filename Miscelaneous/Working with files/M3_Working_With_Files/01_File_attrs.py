import os
from datetime import datetime

"""Getting file attributes with the os module"""


def get_date(time_stamp: float) -> str:
    return datetime.utcfromtimestamp(time_stamp).strftime("%d %b %Y")


def get_file_attrs(folder_path: str) -> None:
    with os.scandir(folder_path) as directory:
        for file in directory:  # This is an iterator of ScanDir[str]
            if file.is_file():  # This is a DirEntry[str]
                file_info: os.stat_result = file.stat()
                print(f"Modified {get_date(file_info.st_mtime)} - {file.name}")


get_file_attrs("../files/subfolder")

