def read_txt(file_name: str) -> None:
    with open(file_name) as file:
        print(file.read())


def read_txt_by_line(file_name ) -> None:
    with open(file_name) as file:
        lines: list[str] = file.readlines()
        for line in lines:
            print(line)


def write_new_text(file_name: str, text: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(text)


def append_line_text(file_name: str, text: str) -> None:
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write('\n')
        file.write(text)


# Reading
read_txt('../files_to_read/backup.py')  # A lot of output
read_txt_by_line('../files_to_read/backup.py')  # A lot of output

# Writing
write_new_text("../files_to_read/example.txt", "This is a text")

# Appending
append_line_text("../files_to_read/example.txt", "This is the second line to that freaking file")

# Reading from recently created file:
read_txt("../files_to_read/example.txt")
# This is a text
# This is the second line to that freaking file
