import os


"""Removing files with the os module"""


def remove_file(file_path: str) -> None:
    if os.path.isfile(file_path):
        try:
            os.remove(file_path)
            print(f"File '{file_path}' successfully removed!")
        except OSError as err:
            print(f"{err.__class__}: {err}")

    else:
        print(f"Error: {file_path} is not a valid file")


remove_file("../files/text.txt")
# File '../files/text.txt' successfully removed!
remove_file("../files/text.txt")
# Error: ../files/text.txt is not a valid file
