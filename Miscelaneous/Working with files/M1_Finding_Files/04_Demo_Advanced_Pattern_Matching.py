import os
import fnmatch


def match(folder_path: str, search_criteria: str) -> None:
    for file in os.listdir(folder_path):
        if fnmatch.fnmatch(file, search_criteria):
            print(file)
    print()


print("Any type of files containing the substring '_file'")
match('../files', '*_file*.*')
# Any type of files containing the substring '_file'
# 02_file_test.csv
# 01_file_test.csv
# 01_file.csv
# 01_test_file.csv
# 02_test_file.csv
# 02_file.txt
# 02_file_test.txt
# 01_file_test.txt
# 01_test_file.txt
# 01_file.txt
# 02_test_file.txt
# 02_file.csv

print("Any type of files containing the substring '_file_'")
match('../files', '*_file_*.*')
# Any type of files containing the substring '_file_'
# 02_file_test.csv
# 01_file_test.csv
# 02_file_test.txt
# 01_file_test.txt

print("More complicated matching:")
match('../files', '*2_*_*.*')
# More complicated matching:
# 02_file_test.csv
# 02_test_file.csv
# 02_file_test.txt
# 02_test_file.txt
