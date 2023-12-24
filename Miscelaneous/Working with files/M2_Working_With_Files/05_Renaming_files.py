import os
from pathlib import Path


def rename_file_1(original: str, new_name: str) -> None:
    os.rename(original, new_name)


def rename_file_2(original: str, new_name: str) -> None:
    file = Path(original)
    file.rename(new_name)


# Using the two functions to rename files:
rename_file_1("../files/text.txt", "../files/TEXTO.txt")
rename_file_2("../files/TEXTO.txt", "../files/text.txt")  # Reverting changes
