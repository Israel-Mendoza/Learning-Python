import os

"""Using Python to list the files contained in a given path and which names end (or start) with a given string"""


def ends_with(folder_path: str, search_criteria: str) -> None:
    for file in os.listdir(folder_path):
        if file.endswith(search_criteria):
            print(file)
    print()


def starts_with(folder_path: str, search_criteria: str) -> None:
    for file in os.listdir(folder_path):
        if file.startswith(search_criteria):
            print(file)
    print()


print("CSV Files")
ends_with("../files", ".csv")
# CSV Files
# 02_file_test.csv
# 01_file_test.csv
# 02_test.csv
# 01_file.csv
# 01_test_file.csv
# 02_test_file.csv
# 01_test.csv
# 02_file.csv

print("Files starting with \"01\"")
starts_with("../files", "01")
# Files starting with "01"
# 01_test.txt
# 01_file_test.csv
# 01_file.csv
# 01_test_file.csv
# 01_test.csv
# 01_file_test.txt
# 01_test_file.txt
# 01_file.txt
