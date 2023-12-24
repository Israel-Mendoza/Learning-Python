import os


"""Using the os.walk() method to traverse directories"""


def traverse(folder_path: str) -> None:
    for path, dirs, files in os.walk(folder_path):  # Returns an iterator of tuple[str, list[str], list[str]]
        print(f"Path: {path}")
        if dirs:
            for directory in dirs:
                print(f"\tDirectory: {directory}")
        else:
            print("\tNo directories found in the current directory")
        if files:
            for file in files:
                print(f"\tFile: '{file}'")
        else:
            print("\tNo files found in the current directory")


traverse("../files")
# Path: ../files
# 	Directory: subfolder
# 	Directory: empty
# 	File: '02_file_test.csv'
# 	File: '01_test.txt'
# 	File: '01_file_test.csv'
# 	File: '02_test.csv'
# 	File: '01_file.csv'
# 	File: '01_test_file.csv'
# 	File: '02_test_file.csv'
# 	File: '02_file.txt'
# 	File: '01_test.csv'
# 	File: '02_file_test.txt'
# 	File: '01_file_test.txt'
# 	File: '02_test.txt'
# 	File: 'text.txt'
# 	File: '01_test_file.txt'
# 	File: '01_file.txt'
# 	File: '02_test_file.txt'
# 	File: '02_file.csv'
# Path: ../files/subfolder
# 	No directories found in the current directory
# 	File: '01_file_test.csv'
# 	File: '01_test_file.csv'
# 	File: '01_file_test.txt'
# 	File: '01_test_file copy.txt'
# 	File: '01_test_file.txt'
# Path: ../files/empty
# 	No directories found in the current directory
# 	No files found in the current directory
