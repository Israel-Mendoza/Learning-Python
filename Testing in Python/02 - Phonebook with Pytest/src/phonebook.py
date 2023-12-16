import os
import pathlib


class Phonebook:

    def __init__(self, temp_dir: str) -> None:
        self._contacts: dict[str, str] = {}
        self._is_consistent: bool = True
        self._file_name = pathlib.Path(temp_dir) / "phonebook.txt"
        self._cache = open(self._file_name, "w")

    @property
    def is_consistent(self) -> bool:
        return self._is_consistent

    @property
    def all_names(self) -> set[str]:
        return set(self._contacts.keys())

    def add(self, name: str, phone: str) -> None:
        for phone_number in self._contacts.values():
            if phone in phone_number:
                self._is_consistent = False
                break
            if phone_number in phone:
                self._is_consistent = False
                break
        self._contacts[name] = phone

    def lookup(self, name: str) -> str:
        phone: str = self._contacts.get(name, None)
        if phone is None:
            raise KeyError
        return phone

    def clear(self) -> None:
        self._cache.close()
        os.remove(self._file_name)
