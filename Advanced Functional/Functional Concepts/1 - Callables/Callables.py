"""Callables return a value!"""

print(callable(print))
# True

result = print("Hello")
print(result)
# None

a_list: list[int] = [1, 2, 3]
print(callable(a_list.append))  # True

list_result = a_list.append(4)
print(list_result)
# None

message: str = "hello"
print(callable(message.upper))
# True

str_result: str = message.upper()
print(result)
# HELLO
