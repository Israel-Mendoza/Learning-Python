"""GETTERS AND SETTERS?"""


class Person:
    def __init__(self, name: str) -> None:
        print("Initializing object...")
        self.set_name(name)

    def get_name(self) -> str:  # Getter
        """Returns the "_name" attribute of the instance"""
        return self._name

    def set_name(self, value: str) -> None:  # Setter
        """
        Sets the "_name" attribute of the instance 
        only if the passed argument is a string longer than
        one character.        
        """
        if isinstance(value, str):
            value = value.strip()
            if len(value) > 1:
                self._name: str = value
                print(f"{self}.name = '{self.get_name()}'\n")
            else:
                raise ValueError(f"'{value}' is too short for a name!\n")
        else:
            raise ValueError(f"'{value}' is not a valid string for a name!\n")


# Instantiating the class
p: Person = Person("Israel")
# Initializing object...
# <__main__.Person object at 0x7f3ae8e2afd0>.name = 'Israel'

print(f"{p.__dict__ = }")
# p.__dict__ = {'_name': 'Israel'}

# Trying to set an int as the name
try:
    p.set_name(155225)
except ValueError as error:
    print(error)
# '155225' is not a valid string for a name!

# Trying to set an empty string as the name
try:
    p.set_name("      ")
except ValueError as error:
    print(error)
# '' is too short for a name!

# Trying to set a valid string as the name
try:
    p.set_name("Coco")
except ValueError as error:
    print(error)
# <__main__.Person object at 0x7f3ae8e2afd0>.name = 'Coco'
