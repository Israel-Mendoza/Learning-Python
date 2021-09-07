# Implementing the __call__ method to make the instance
# a callable object


class Person:
    def __call__(self):
        print("__call__ was called! LOL")


p = Person()
p()  # -> "__call__ was called! LOL"


# Implementing the "partial" function as an object


class MyPartial:
    def __init__(self, func, *args):
        self._func = func
        self._args = args

    def __call__(self, *args):
        return self._func(*self._args, *args)


partial_func = MyPartial(lambda a, b, c: (a, b, c), 10, 20)
print(f"type(partial_func) = {type(partial_func)}")
print(partial_func(30))
