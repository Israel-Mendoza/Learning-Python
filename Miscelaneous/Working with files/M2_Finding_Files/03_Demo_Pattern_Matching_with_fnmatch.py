import os
import fnmatch


"""Using the fnmatch to pattern matching. This allows us to use wildcards."""


def match(folder_path: str, search_criteria: str) -> None:
    for file in os.listdir(folder_path):
        if fnmatch.fnmatch(file, search_criteria):
            print(file)
    print()


print("All CSV files:")
match("../files", "*.csv")
# 02_file_test.csv
# 01_file_test.csv
# 02_test.csv
# 01_file.csv
# 01_test_file.csv
# 02_test_file.csv
# 01_test.csv
# 02_file.csv

print("CSV files, no tests:")
match("../files", "*_file.csv")
# CSV files, no tests:
# 01_file.csv
# 01_test_file.csv
# 02_test_file.csv
# 02_file.csv


print("CSV files, no tests, that contain the number 1:")
match("../files", "*1*_file.csv")
# CSV files, no tests, that contain the number 1:
# 01_file.csv
# 01_test_file.csv

print("CSV files, no tests, that contain the number 2:")
match("../files", "*2*_file.csv")
# CSV files, no tests, that contain the number 2:
# 02_test_file.csv
# 02_file.csv
