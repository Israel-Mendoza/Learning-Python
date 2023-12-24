import zipfile
from typing import Literal

files_to_add: list[str] = ["../files/01_file.csv", "../files/01_file.txt"]
zip_file: str = "./files.zip"


def add_to_zip(zip_file_name: str, files: list[str], opt: Literal["r", "w", "a"]) -> None:
    with zipfile.ZipFile(zip_file_name, opt) as archive:
        for file in files:
            archive_list = archive.namelist()
            if file not in archive_list:
                archive.write(file)
            else:
                print(f"File '{file}' is already in the zip file")


add_to_zip(zip_file, files_to_add, 'a')
