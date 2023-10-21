from os import listdir, rename, getcwd, walk
from os.path import isfile, join
from toggler import CaseToggler as CT

file_path = getcwd()

directory = CT(file_path)

directory.asc_files_summary()

print(directory.asc_files)
print(directory.asc_files_lower)
print(directory.asc_files_upper)

if directory.polling_command_file in directory.onlyfiles:     #directory.find_file():
            print("\nThe text file containing the polling commands already exists!!!")
else:
    print("\nThe file does not exist.")