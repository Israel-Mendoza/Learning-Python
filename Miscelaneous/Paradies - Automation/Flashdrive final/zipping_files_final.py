from os import path, getcwd, remove
from shutil import make_archive, move
from polling_flashdrive import Flashdrive

print("*****POLLING REGISTER USING A FLASHDRIVE***** \n\nAuthor: Israel Mendoza\n\n\n\n")

if path.exists("C:\\Program Files (x86)\\SAP\\Retail Systems\\Xpress Server\\upload"):
    reg_path = "C:\\Program Files (x86)\\SAP\\Retail Systems\\Xpress Server\\upload"
elif path.exists("C:\\Program Files\\SAP\\Retail Systems\\Xpress Server\\upload"):
    reg_path = "C:\\Program Files\\SAP\\Retail Systems\\Xpress Server\\upload"
else:
    reg_path = ""

if reg_path:
    polling = Flashdrive()
    if polling.flashdrive and not path.exists(polling.end_zip_file):
        print("Creating the zip file containing the polling files...\n")
        polling.create_zip()
        if polling.check_creation():
            print("The zip file was successfully created.\n")
            print(f"Moving the zip file to the '{polling.flashdrive}' drive...\n\n\n")
            polling.move_zip_file()
        else:
            print("The zip file could not be created either because the \"upload\" folder was not found, "
                "or because there was an error during the file creation.\n")
            print("Contact the IT Service Center for further assistance.")
    elif polling.flashdrive and path.exists(polling.end_zip_file):
        print(f"There is already a '{polling.zip_filename}' in the '{polling.flashdrive}' drive.")
        print("Deleting the file to avoid duplicates...\n")
        remove(polling.end_zip_file)
        print("Creating the zip file containing the polling files...\n")
        polling.create_zip()
        if polling.check_creation():
            print(f"Moving the zip file to the '{polling.flashdrive}' drive...\n\n\n")
            polling.move_zip_file()
        else:
            print("The zip file could not be created either because the \"upload\" folder was not found, "
                "or because there was an error during the file creation.\n")
            print("Contact the IT Service Center for further assistance.")
    elif not polling.flashdrive:
        print("No flashdrive was recognized by the Operating System. \n"
            "\nInsert a flashdrive and try again.")
else:
    print("The program was unable to find the following paths: ")
    print("--->>> Program Files (x86)\\SAP\\Retail Systems\\Xpress Server\\upload")
    print("--->>> Program Files\\SAP\\Retail Systems\\Xpress Server\\upload")
    print("\nPlease contact the IT Service Center for further assistance.")
    
input()
