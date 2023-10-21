from os import listdir, rename, getcwd, walk
from os.path import isfile, join

class CaseToggler:
    """It toggles the file name's cases and creates a text file,
    ready to be used for Micros registers polling."""

    def __init__(self, file_path):
        """Initializes the file_path."""
        self.file_path = file_path
        # Makes a list with all the file names in the directory.
        self.onlyfiles = [file for file in listdir(file_path) if isfile(join(file_path, file))]
        # Makes a list with the names of the *.asc files
        self.asc_files = [file for file in self.onlyfiles if "O.asc" in file or "O.ASC" in file]
        self.asc_files_lower = [file for file in self.asc_files if "str" in file]
        self.asc_files_upper = [file for file in self.asc_files if "STR" in file]
        self.polling_command_file = "polling_commands.txt"

    def asc_files_summary(self):
        """Prints messages summarizing the amount of files that can be converted."""
        if not self.asc_files_lower and not self.asc_files_upper:
            print("There are no Action Script Communication (ASC) files in the given folder.\n")
            print("Please make sure the files are available and run this program again.")
        elif self.asc_files_lower and self.asc_files_upper:
            print(f"There are both lowercased and uppercased Action Script Communication (ASC) "
                "files in this directory.")
        elif self.asc_files_upper:
            print("All of the Action Script Communication (ASC) files in this directory "
                "are already uppercased. \nThey are ready for polling.")
        elif self.asc_files_lower:
            print("All of the Action Script Communication (ASC) files in this directory "
                "are lowercased and ready to be converted.")

    def asc_files_conversion_summary(self):
        """Prints messages summarizing the amount of files that can be converted."""
        onlyfiles = [file for file in listdir(self.file_path) if isfile(join(self.file_path, file))]
        asc_files_lower = [file for file in onlyfiles if "O.asc" in file]
        asc_files_upper = [file for file in onlyfiles if "O.ASC" in file]

        if not asc_files_lower and not asc_files_upper:
            print("\nThere are no Action Script Communication (ASC) files in the given folder.\n")
            print("Please contact your system administrator.\n")
        elif asc_files_upper and not asc_files_lower:
            print("\nAll of the Action Script Communication (ASC) files in this directory "
                "are now uppercased. All files are ready for polling.\n")
        elif asc_files_lower and not asc_files_upper:
            print("\nAll of the Action Script Communication (ASC) files in this directory "
                "are lowercased. They will need to be uppercased for polling.\n")


    def case_toggler_upper(self):
        """
        Looks for all the files in the given directory, and renames the *.asc files to uppercases.
        """
        converted_files = []
        # Renames the *.asc files to uppercases.
        for file in self.asc_files_lower:
            src = file
            dst = file.upper()
            print(f"Renaming {src} to {dst}...")
            rename(src, dst)
            converted_files.append(dst)
        print("\n\nConverted files: \n")
        for file in converted_files:
            print(f"--->  {file}")

    def case_toggler_lower(self):
        """
        Looks for all the files in the given directory, and renames the *.ASC files to lowercases.
        Returns True if it converted the files, and False if there are only lower *.asc files.
        """
        converted_files = []
        # Renames the *.asc files to lowercases.
        for file in self.asc_files_upper:
            src = file
            dst = file[0:7].lower() + "O" + file[-4:].lower()
            print(f"Renaming {src} to {dst}...")
            rename(src, dst)
            converted_files.append(dst)
        print("\n\nConverted files: \n")
        for file in converted_files:
            print(f"--->  {file}")

    def polling_command_generator(self):
        """
        Accepts a list containing filenames and generates a text file 
        containing the psales.ksh command for each file.
        """
        commands = ""
        for file in self.asc_files_upper:
            commands += f"psales.ksh {file[3:7]} O\n"
        with open(self.polling_command_file, "w") as file_contents:
            file_contents.write(commands)

    def directory_status_update(self):
        """Updates the attributes containing the files in lower or uppercases."""
        self.onlyfiles = [file for file in listdir(self.file_path) if isfile(join(self.file_path, file))]
        self.asc_files_lower = [file for file in self.onlyfiles if "O.asc" in file]
        self.asc_files_upper = [file for file in self.onlyfiles if "O.ASC" in file]
