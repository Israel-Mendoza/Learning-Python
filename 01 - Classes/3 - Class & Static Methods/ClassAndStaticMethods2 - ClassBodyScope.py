class Language1:
    MAJOR: int = 3
    MINOR: int = 12
    REVISION: int = 2
    FULL = f"{MAJOR}.{MINOR}.{REVISION}"


print(f"By attribute: {Language1.FULL}")
# By attribute: 3.12.2


class Language2:
    MAJOR: int = 3
    MINOR: int = 12
    REVISION: int = 2

    @property
    def version(self) -> str:  # Has access to an instance
        return f"{self.MAJOR}.{self.MINOR}.{self.REVISION}"

    @classmethod
    def class_version(cls) -> str:  # Has access to the class
        return f"{cls.MAJOR}.{cls.MINOR}.{cls.REVISION}"

    @staticmethod
    def static_version() -> str:  # Doesn't have access to the class or an instance. Must specify the class name
        return f"{Language2.MAJOR}.{Language2.MINOR}.{Language2.REVISION}"


l: Language2 = Language2()

print(f"By instance property: {l.version}")
# By instance property: 3.12.2
print(f"By class method: {Language2.class_version()}")
# By class method: 3.12.2
print(f"By static method: {Language2.static_version()}")
# By static method: 3.12.2
