class Location:
    # Slots will store the instance attributes somewhere else than the
    # usual __dict__ dictionary
    # The specified attribute names will now live in the class namespace.
    # No __weakref__ and no __dict__ in the class and instance.
    __slots__ = "name", "_longitude", "_latitude"

    service = "Google maps"

    def __init__(self, name, longitude, latitude):
        self._longitude = longitude
        self._latitude = latitude
        self.name = name

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude(self):
        return self._latitude

    def speak(self):
        print(f"{self} can't speak!")


location = Location("My house", 101.33332, -92.33335)

print("LOCATION CLASS NAMESPACE")
for k, v in Location.__dict__.items():
    if "__slots__" in dir(Location) and k in Location.__dict__["__slots__"]:
        print(f"Slotted instance attribute: '{k}': {v}")
    else:
        print(f"Class attribute '{k}': {v}")

print("\n\n")

print("LOCATION OBJECT NAMESPACE")
try:
    for k, v in location.__dict__.items():
        print(f"|{k}:{v}")
        print(f"\t{hex(id(k)).upper()}: {hex(id(v)).upper()}|")
except AttributeError as error:
    print(f"AttributeError: {error}")
