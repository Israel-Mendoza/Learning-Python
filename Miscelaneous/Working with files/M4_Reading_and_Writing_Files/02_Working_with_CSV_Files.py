import csv


def read_csv(file_name: str, delimiter: str) -> None:
    with open(file_name) as csv_file:
        count: int = -1  # Using a counter to differentiate between the header and the content of the file
        rows = csv.reader(csv_file, delimiter=delimiter)
        for row in rows:
            if count < 0:
                print(f" | ".join(row))
            else:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

            count += 1

        print(f"[{count}] lines")


def write_new_csv(file_name: str, header: list[str], row: list[str]) -> None:
    with open(file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(row)


read_csv("../files_to_read/names.csv", ",")
# name | lastname | age | sex
# John | Smith | 41 | male
# Joe | Clark | 25 | male
# Israel | Mendoza | 31 | male
# Roberto | Mendoza | 1 | male
# Sandra | Aguilar | 35 | female
# [5] lines


my_header: list[str] = ["name", "lastname", "age", "sex"]
first_row: list[str] = ["Foo", "Fighter", "82", "male"]

write_new_csv("../files_to_read/names2.csv", my_header, first_row)

read_csv("../files_to_read/names2.csv", ",")
# name | lastname | age | sex
# Foo | Fighter | 82 | male
# [1] lines
