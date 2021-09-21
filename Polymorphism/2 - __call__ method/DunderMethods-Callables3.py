from collections import defaultdict


class DefaultValue:
    def __init__(self, default_value):
        self._default_value = default_value
        self._counter = 0

    @property
    def default_value(self):
        """The object's default value"""
        return self._default_value

    @property
    def counter(self):
        """The counter attribute of the object"""
        return self._counter

    def __call__(self):
        self._counter += 1
        return self.default_value


counter_1 = DefaultValue("N/A")
counter_2 = DefaultValue("No aplica")
my_dict_1 = defaultdict(counter_1)
my_dict_2 = defaultdict(counter_2)

# Let's create some key/value pairs in both dictionaries:
my_dict_1["a"] = "Alpha"
my_dict_1["b"] = "Beta"
my_dict_2["g"] = "Gamma"
my_dict_2["d"] = "Delta"

# Trying accessing some keys in both dictionaries:
for letter in "abcde":
    print(f"'{letter}' in my_dict_1 = {my_dict_1[letter]}")
    print(f"'{letter}' in my_dict_2 = {my_dict_2[letter]}")


print(f"Counter for my_dict_1 = {counter_1.counter}")
print(f"Counter for my_dict_2 = {counter_2.counter}")
