import requests


post_files_url: str = "http://localhost:8000/upload-files"

file_one = open("../files_to_upload/one.csv", "rb")
file_two = open("../files_to_upload/two.csv", "rb")

files = [
    ("files", ("one.csv", file_one, "text/csv")),  # Tuple with the variable name (in server), the file, and the format
    ("files", ("two.csv", file_two, "text/csv")),
]

# To add one single file, you can use:
# files = {"file": open("../files_to_upload/one.csv", "rb")}

response = requests.post(
    post_files_url,  # Post url
    files=files  # The files kwyword argument is the one receiving the files
)

file_one.close()
file_two.close()

print(response.json())
