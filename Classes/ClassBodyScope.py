class Language:
    MAJOR = 3
    MINOR = 7
    REVISION = 4
    FULL = f"{MAJOR}.{MINOR}.{REVISION}"


print(f"By attribute: {Language.FULL}")


class Language:
    MAJOR = 3
    MINOR = 7
    REVISION = 4

    @property
    def version(self):
        return f"{self.MAJOR}.{self.MINOR}.{self.REVISION}"

    @classmethod
    def cls_version(cls):
        return f"{cls.MAJOR}.{cls.MINOR}.{cls.REVISION}"

    @staticmethod
    def static_version():
        return f"{Language.MAJOR}.{Language.MINOR}.{Language.REVISION}"


l = Language()

print(f"By instance property: {l.version}")
print(f"By class method: {Language.cls_version()}")
print(f"By static method: {Language.static_version()}")
