from collections import defaultdict


class DefaultValue:
    def __init__(self, default_value: str) -> None:
        self.default_value: str = default_value
        self._counter: int = 0

    @property
    def counter(self) -> int:
        """The counter attribute of the object"""
        return self._counter

    def __call__(self) -> str:
        self._counter += 1
        return self.default_value


# Creating a couple of DefaultValue instances:
counter_1 = DefaultValue("N/A")
counter_2 = DefaultValue("Undefined")

# Creating a couple of defaultdict instances with our
# DefaultValue instances (remmber that they're callable):
my_dict_1: defaultdict[str, str] = defaultdict(counter_1)
my_dict_2: defaultdict[str, str] = defaultdict(counter_2)

# Let's create some key/value pairs in both dictionaries:
my_dict_1["a"] = "Alpha"
my_dict_1["b"] = "Beta"
my_dict_2["g"] = "Gamma"
my_dict_2["d"] = "Delta"

# Trying accessing some keys in both dictionaries:
for letter in "abcde":
    print(f"'{letter}' in my_dict_1 = {my_dict_1[letter]}")
    print(f"'{letter}' in my_dict_2 = {my_dict_2[letter]}")
# 'a' in my_dict_1 = Alpha
# 'a' in my_dict_2 = Undefined
# 'b' in my_dict_1 = Beta
# 'b' in my_dict_2 = Undefined
# 'c' in my_dict_1 = N/A
# 'c' in my_dict_2 = Undefined
# 'd' in my_dict_1 = N/A
# 'd' in my_dict_2 = Delta
# 'e' in my_dict_1 = N/A
# 'e' in my_dict_2 = Undefined

print(f"{counter_1.counter = }")
# counter_1.counter = 3
print(f"{counter_2.counter = }")
# counter_2.counter = 4
