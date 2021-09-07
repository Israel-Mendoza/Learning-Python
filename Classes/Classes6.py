# Monkeypatching


class Person:
    def say_hello(self):
        print(f"{self} instance says hello!")


p = Person()
p.say_hello()

# Adding a instance method on the fly using the class namespace
print(f"Setting a 'do_work' function to the Person class...")
setattr(Person, "do_work", lambda self: f"{self} is working!")

# Checking the Person's namespace:
print(f"\nPerson's namespace after monkeypatching:")
for k in Person.__dict__:
    print(f"Person.{k}: {Person.__dict__[k]}")

print(f"\nThe instance will be able to use the recently defined method:")
print(f"p.do_work: {p.do_work}")
print(p.do_work(), "\n")

# Adding an instance method on the fly using the instance namespace
print(f"Setting a 'other_func' method to the 'p' object...")
setattr(p, "other_func", lambda *args: f"Other function with args: {args}")
print(f"Using the recently defined method:")
print(p.other_func())  # No self argument is passed

