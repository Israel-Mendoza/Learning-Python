"""Using __weakref__ and __slots__"""

# Slots will store the instance attributes some-
# where else than the usual __dict__ dictionary.
# The specified attribute names will now live in
# the class namespace.
#
# No __weakref__ and no __dict__ in the class and instance!


import weakref


class Location:
    __slots__: tuple[str, str, str] = "name", "_longitude", "_latitude"

    service: str = "Google maps"

    def __init__(self, name: str, longitude: float, latitude: float) -> None:
        self._longitude: float = longitude
        self._latitude: float = latitude
        self.name: str = name

    @property
    def longitude(self) -> float:
        return self._longitude

    @property
    def latitude(self) -> float:
        return self._latitude

    def speak(self) -> None:
        print(f"{self} can't speak!")


location: Location = Location("My house", 101.33332, -92.33335)

# Printing the Location class' namespace (no __dict__ and no __weakref__).
# '_latitude', '_longitude' and 'name' are now class attributes!
for k, v in Location.__dict__.items():
    if "__slots__" in dir(Location) and k in Location.__dict__["__slots__"]:
        print(f"Slotted instance attribute: '{k}': {type(v)}/{v}")
    else:
        print(f"Class attribute '{k}': {type(v)}/{v}")
# Class attribute '__module__': <class 'str'>/__main__
# Class attribute '__annotations__': <class 'dict'>/{'__slots__': tuple[str, str, str], 'service': <class 'str'>}
# Class attribute '__slots__': <class 'tuple'>/('name', '_longitude', '_latitude')
# Class attribute 'service': <class 'str'>/Google maps
# Class attribute '__init__': <class 'function'>/<function Location.__init__ at 0x1047759e0>
# Class attribute 'longitude': <class 'property'>/<property object at 0x104779e40>
# Class attribute 'latitude': <class 'property'>/<property object at 0x1047a9530>
# Class attribute 'speak': <class 'function'>/<function Location.speak at 0x1047762a0>
# Slotted instance attribute: '_latitude': <class 'member_descriptor'>/<member '_latitude' of 'Location' objects>
# Slotted instance attribute: '_longitude': <class 'member_descriptor'>/<member '_longitude' of 'Location' objects>
# Slotted instance attribute: 'name': <class 'member_descriptor'>/<member 'name' of 'Location' objects>
# Class attribute '__doc__': <class 'NoneType'>/None

# location_object's namespace (no __dict__ when using __slots__):
try:
    for k, v in location.__dict__.items():
        print(f"|{k}:{v}")
        print(f"\t{hex(id(k)).upper()}: {hex(id(v)).upper()}|")
except AttributeError as error:
    print(f"AttributeError: {error}")
# AttributeError: 'Location' object has no attribute '__dict__'

# Creating a weak reference (no __weakref__ when using __slots__):
try:
    wr1: weakref.ref[Location] = weakref.ref(location)
except Exception as error:
    print(f"{type(error).__name__}: {error}")
# TypeError: cannot create weak reference to 'Location' object
