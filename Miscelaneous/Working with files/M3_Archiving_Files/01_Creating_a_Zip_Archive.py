import zipfile
import time
import os
from typing import Literal


to_zip: list[str] = [
    "../files/subfolder/01_file_test.csv",
    "../files/subfolder/01_file_test.txt",
    "../files/subfolder/01_test_file.csv",
    "../files/subfolder/01_test_file.txt",
    "../files/01_file_test.csv",
    "../files/01_file_test.txt"
]


def create_zip(zip_file_name: str, files: list[str], opt: Literal["r", "w"]) -> None:
    with zipfile.ZipFile(zip_file_name, opt, allowZip64=True) as archive:
        for file in files:
            archive.write(file)


file_name: str = "./files.zip"
create_zip(file_name, to_zip, "w")

time.sleep(1)  # Waiting one second before

zip_file_exists: bool = os.path.isfile(file_name)

print(f"The {file_name} exists: {zip_file_exists}.")
# The ./files.zip exists: True.

# if zip_file_exists:
#     # Un chistorete:
#     print(f"Deleting file", end="")
#     for _ in range(5):
#         print(". ", end="")
#         time.sleep(0.5)
#     print()
#     # Let's delete the file:
#     try:
#         os.remove(file_name)
#         print(f"File '{file_name}' successfully removed!")
#     except OSError as err:
#         print(f"{err.__class__}: {err}")
# File './files.zip' successfully removed!
