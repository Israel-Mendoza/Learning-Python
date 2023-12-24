import shutil
from typing import override

"""Moving files and folders with the shutil module"""


def move_files(src: str, dst: str) -> None:
    shutil.move(src, dst)


# Moving individual files:
# move_files("../files/text.txt", "../files/empty/")
# move_files("../files/empty/text.txt", "../files/")  # Reverting

# Moving folders:
# move_files("../files/subfolder", "../files/empty/")
# move_files("../files/empty/subfolder", "../files/")  # Reverting
