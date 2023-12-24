import os


"""Using Python to list the files contained in a given path."""


def list_dir(folder_path: str):
    for file in os.listdir(folder_path):
        print(file)


list_dir("../files")
# 02_file_test.csv
# subfolder
# 01_test.txt
# 01_file_test.csv
# 02_test.csv
# 01_file.csv
# 01_test_file.csv
# 02_test_file.csv
# 02_file.txt
# 01_test.csv
# 02_file_test.txt
# 01_file_test.txt
# 02_test.txt
# text.txt
# 01_test_file.txt
# 01_file.txt
# 02_test_file.txt
# 02_file.csv
