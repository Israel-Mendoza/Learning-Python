class MyClass:
    def hello():
        print("Hello...")

    def inst_hello(self):
        print(f"Hello from {self}")

    @classmethod
    def cls_hello(cls):
        print(f"Hello from {cls}")

    @staticmethod
    def static_hello():
        print("Hello statically!")


o = MyClass()

print("Calling 'hello':")
MyClass.hello()
try:
    o.hello()
except TypeError as error:
    print(error)
print()

print("Calling 'inst_hello':")
try:
    MyClass.inst_hello()
except TypeError as error:
    print(error)
o.inst_hello()
print()

print("Calling 'cls_hello':")
MyClass.cls_hello()
o.cls_hello()
print()

print("Calling 'static_hello':")
MyClass.static_hello()
o.static_hello()
print()
