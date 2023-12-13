class Employee:

    def __init__(self, first_name: str, last_name: str, annual_salary: int) -> None:
        self._first_name: str = first_name
        self._last_name: str = last_name
        self._annual_salary: int = annual_salary

    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @property
    def annual_salary(self) -> int:
        return self._annual_salary

    def give_raise(self, raise_value: int = 0) -> None:
        if raise_value:
            self._annual_salary += raise_value
        else:
            self._annual_salary += 5000
        