class Countdown:
    """Non-data descriptor."""

    def __init__(self, start):
        self.start = start + 1

    def __get__(self, instance, owner):
        """
        Returns the descriptor instance if called
        from a class. 
        Otherwise, will decrease the self.start value 
        by one and return the value.
        """
        if instance is None:
            return self
        self.start -= 1
        return self.start


class Rocket:
    """A rocket class, holding a down counter as attribute"""
    # The countdown class attribute will be shared
    # amont all instances
    countdown = Countdown(10)


r1 = Rocket()
r2 = Rocket()

print(f"{r1.countdown = }") # r1.countdown = 10
print(f"{r1.countdown = }") # r1.countdown = 9
print(f"{r1.countdown = }") # r1.countdown = 8
print(f"{r1.countdown = }") # r1.countdown = 7
print(f"{r1.countdown = }") # r1.countdown = 6
print(f"{r1.countdown = }") # r1.countdown = 5
print(f"{r1.countdown = }") # r1.countdown = 4
print(f"{r1.countdown = }") # r1.countdown = 3
print(f"{r1.countdown = }") # r1.countdown = 2
print(f"{r1.countdown = }") # r1.countdown = 1
