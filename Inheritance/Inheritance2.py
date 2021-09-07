class Person:
    def eat(self):
        print(f"{self.__class__.__name__} eats")

    def work(self):
        print(f"{self.__class__.__name__} works")

    def sleep(self):
        print(f"{self.__class__.__name__} sleeps")

    def routine(self):
        self.eat()
        self.work()
        self.sleep()


class Student(Person):
    def work(self):
        print(f"{self.__class__.__name__} goes to school")

    def sleep(self):
        print(f"{self.__class__.__name__} doesn't sleep")


p = Person()
s = Student()

p.routine()
print()
s.routine()
