from os import listdir, rename, getcwd, walk
from os.path import isfile, join
from toggler import CaseToggler as CT

print("============================================================================================================")
print("\n\n\n\tWelcome to CASE TOGGLER!!!\t\t\t\t\t\tAuthor: Israel Mendoza\n\n\n")
print("============================================================================================================\n\n")


file_path = getcwd()

directory = CT(file_path)

directory.asc_files_summary()
print("\nEnter 'q' at anytime to quit.\n")

while True:
    if directory.asc_files_lower and directory.asc_files_upper:
        response = input("\nEnter '1' to convert the remaining files to uppercases and '2' for lowercases: ")
        if response == 'q':
            break
        elif response == "1":
            directory.case_toggler_upper()
            directory.asc_files_conversion_summary()
            break
        elif response == "2":
            directory.case_toggler_lower()
            directory.asc_files_conversion_summary()
            break
        else:
            continue
    elif directory.asc_files_upper:
        response = input("\nEnter 'y' to convert these files to lowercase. Otherwise, hit 'q' to quit. ")
        if response == "q":
            break
        elif response == "y":
            directory.case_toggler_lower()
            directory.asc_files_conversion_summary()
            break
        else:
            continue
    elif directory.asc_files_lower:
        directory.case_toggler_upper()
        directory.asc_files_conversion_summary()
        break

print("============================================================================================================")
print("============================================================================================================")

if directory.asc_files_upper:
    while True:
        if directory.find_file():
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

print("============================================================================================================")
print("\n\n\t\t\t\tThank you for using Case Toggler for polling!!!\n")
print("============================================================================================================")

input()