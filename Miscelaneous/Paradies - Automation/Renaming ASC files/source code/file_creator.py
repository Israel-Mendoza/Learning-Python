from os import listdir, rename, getcwd, walk
from os.path import isfile, join
from toggler import CaseToggler as CT

file_path = getcwd()

directory = CT(file_path)

print(directory.asc_files_upper)
print(directory.polling_command_file)
print(directory.onlyfiles)
print(directory.polling_command_file in directory.onlyfiles)

if directory.asc_files_upper:
    while True:
        if directory.polling_command_file in directory.onlyfiles:
            print("\nThe text file containing the polling commands already exists!!!")
            response = input("\nEnter 'y' to overwrite it. Otherwise hit 'q' to quit. ")
            if response == "q":
                break
            elif response == "y":
                directory.polling_command_generator()
                print("\nThe polling commands file has been overwritten!!!")
                break
            else:
                continue
        else:
            directory.polling_command_generator()
            print("\nThe polling commands file has been successfully created!!!")
            break
else:
    print("\nThere are no uppercased files. No need to create a file with polling commands.\n")

input()