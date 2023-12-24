import shutil


"""Copying files using the shutil module"""


def copy_file(src: str, dst: str) -> None:
    shutil.copy(src, dst)


def copy_folder(src: str, dst: str) -> None:
    shutil.copytree(src, dst)


copy_file("./01_File_attrs.py", "../")
copy_folder("../files/subfolder", "./parent")
