import sys


def add(a, b):
    return a + b


print("-Does 'add' have the '__get__' method?")
print("-Yes!" if hasattr(add, '__get__') else "-No!")
print()
print("-Does 'add' have the '__set__' method?")
print("-Yes!" if hasattr(add, '__set__') else "-No!")
print()


me = sys.modules["__main__"]
f = add.__get__(None, me)
print(f"That is 'f'? {f}")
print(f"Is 'f' the same as 'add'? {f is add}")
