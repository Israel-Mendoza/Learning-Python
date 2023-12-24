import zipfile


zip_file: str = "./files.zip"


def read_zip(zip_file_name: str) -> None:
    with zipfile.ZipFile(zip_file_name, "r") as archive:
        list_of_files: list[str] = archive.namelist()
        for file_name in list_of_files:
            file_info: zipfile.ZipInfo = archive.getinfo(file_name)
            print(f"{file_name}: {file_info.file_size} bytes, {file_info.compress_size}")


read_zip(zip_file)
