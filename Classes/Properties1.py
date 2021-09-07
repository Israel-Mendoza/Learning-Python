# Using getters and setters the Java way


class Person:
    def __init__(self, name: str):
        print("Initializating object...")
        self.set_name(name)

    def get_name(self) -> str:  # Getter
        return self._name

    def set_name(self, value: str):  # Setter
        if isinstance(value, str):
            value = value.strip()
            if len(value) > 1:
                self._name = value
                print(f"{self}.name = '{self.get_name()}'\n")
            else:
                raise ValueError(f"'{value}' is too short for a name!\n")
        else:
            raise ValueError(f"'{value}' is not a valid string for a name!\n")


# Instantiating the class
p = Person("Israel")
# Seeing the namespace of "p"
print(f"namespace of 'p': {p.__dict__}\n")

# Trying to set an int as the name
try:
    p.set_name(155225)
except ValueError as error:
    print(error)

# Trying to set an empty string as the name
try:
    p.set_name("      ")
except ValueError as error:
    print(error)

# Trying to set a valid string as the name
try:
    p.set_name("Coco")
except ValueError as error:
    print(error)
