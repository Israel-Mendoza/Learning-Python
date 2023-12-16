class Phonebook:
    def __init__(self) -> None:
        self._numbers: dict[str, str] = {}
        self._is_consistent: bool = True

    def add(self, name: str, phone: str) -> None:
        for number in self._numbers.values():
            if phone == number:
                self._is_consistent = False
                break
            if number.startswith(phone):
                self._is_consistent = False
                break
            if phone.startswith(number):
                self._is_consistent = False
                break
        self._numbers[name] = phone

    def lookup(self, name: str) -> str:
        result: str | None = self._numbers.get(name, None)
        if result is None:
            raise KeyError
        return result

    @property
    def is_consistent(self) -> bool:
        return self._is_consistent
