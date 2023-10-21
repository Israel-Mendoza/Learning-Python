"""Callables return a value!"""


# BUILT-IN FUNCTIONS AND METHODS

print(callable(print))  # True

result = print("Hello")
print(result)
# None

l = [1, 2, 3]
print(callable(l.append))  # True

result = l.append(4)
print(result)
# None

s = "hello"
print(callable(s.upper))  # True

result = s.upper()
print(result)
# HELLO