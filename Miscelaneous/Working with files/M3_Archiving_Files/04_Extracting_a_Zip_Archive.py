import zipfile

zip_file: str = "./files.zip"
file_to_extract: str = "../files/01_file_test.txt"
extraction_dir: str = "extracted"


def extract_file(zip_file_name: str, file_name: str, extraction_path: str) -> None:
    with zipfile.ZipFile(zip_file_name, "r") as archive:
        archive.extract(file_name, path=extraction_path)


def extract_all(zip_file_name: str, extraction_path: str) -> None:
    with zipfile.ZipFile(zip_file_name, "r") as archive:
        archive.extractall(extraction_path)


extract_file(zip_file, file_to_extract, extraction_dir)
extract_all(zip_file, extraction_dir)
