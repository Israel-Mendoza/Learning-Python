from os import path, getcwd
from shutil import make_archive, move
from glob import glob

class Flashdrive():
    """
    A class that helps us manually getting the polling files
    from a register.
    """
    def __init__(self):
        """Initializes the working directory."""
        self.current_path = getcwd()
        """Initializes the flashdrive path."""
        if "C:" in getcwd():
            for possible_drive in ["d", "e", "f", "g", "h", "i", "j"]:
                if path.exists(f"{possible_drive.upper()}:\\"):
                    self.flashdrive = f"{possible_drive.upper()}:\\"
                    break
                else:
                    continue
            else:
                self.flashdrive = ""
        else:
            self.flashdrive = getcwd()
        """Initializes the register directory path."""
        if path.exists("C:\\Program Files (x86)\\SAP\\Retail Systems\\Xpress Server\\upload"):
            self.reg_path = "C:\\Program Files (x86)\\SAP\\Retail Systems\\Xpress Server\\upload"
        elif path.exists("C:\\Program Files\\SAP\\Retail Systems\\Xpress Server\\upload"):
            self.reg_path = "C:\\Program Files\\SAP\\Retail Systems\\Xpress Server\\upload"
        else:
            self.reg_path = ""
        self.journal_path = f"{self.reg_path}\\keep1"
        self.journal_files = glob(f"{self.journal_path}/*.jrn")
        self.journal_file = self.journal_files[0][-14:]
        self.reg_num = f"{self.journal_file[2:6]}-{self.journal_file[6:8]}"
        """Initialize the end zip filename."""
        self.zip_filename = f"Polling files - {self.reg_num}"
        """Initializes the directory and file of the end zip file."""
        self.end_zip_file = self.flashdrive + "\\" +  self.zip_filename + ".zip"

    def create_zip(self):
        """
        Creates a ZIP file containing the register path.
        The ZIP file will be named as zip_filename.
        """
        make_archive(self.zip_filename, 'zip', self.reg_path)

    def check_creation(self):
        """
        Returns True if the file was successfully created.
        The file is expected to be in the current working directory.
        """
        return path.exists(self.current_path + "\\" +  self.zip_filename + ".zip")

    def move_zip_file(self):
        """
        Moves the created zip file to the flashdrive,
        in case the file is not located there already.
        """
        if self.check_creation():
            if "C:" in self.current_path:
                move(path.join(getcwd(), self.zip_filename + ".zip"), self.flashdrive)
                if path.exists(self.end_zip_file):
                    self.zip_creation_notification()
            else:
                if path.exists(self.end_zip_file):
                    self.zip_creation_notification()

    def check_end_file(self):
        """Checks wheather the file exists"""
        if path.exists(self.end_zip_file):
            self.zip_creation_notification()
        else:
            print("An error occured when converting the compressing the files.")

    def zip_creation_notification(self):
        """
        Prints a message caliming that the zip file was successfully created,
        and the final location of the file.
        """
        print(f"The zip file is ready to be sent to the IT Service Center. \n"
            f"\nYou can find it in '{self.end_zip_file}'\n")
        print(f"Please email the file to 'ITServiceCenter@paradies-na.com'")