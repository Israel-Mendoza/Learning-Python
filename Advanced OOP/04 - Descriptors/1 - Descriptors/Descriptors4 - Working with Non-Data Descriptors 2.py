from __future__ import annotations


class Countdown:
    """Non-data descriptor"""

    def __init__(self, start: int) -> None:
        self.start: int = start + 1
        self.current_value: int = self.start

    def __get__(self, instance: any, owner: type):
        """
        Returns the descriptor instance if called from a class. 
        Otherwise, will decrease the self.start value 
        by one and return the value.
        """
        if instance is None:
            return self
        if self.current_value > 0:
            # Current value may decrease.
            self.current_value -= 1
        else: 
            # Current value has reached 0. Resetting it.
            self.current_value = self.start - 1
        return self.current_value


class Rocket:
    """A rocket class, holding a down counter as attribute"""
    # The countdown class attribute will be shared
    # amont all instances
    countdown = Countdown(10)


# Creating two instances of Rocket.
r1: Rocket = Rocket()
r2: Rocket = Rocket()
r3: Rocket = Rocket()


# Notice how the Countdown instance is shared among all Rocket instances:
print(f"{r1.countdown = }") # r1.countdown = 10
print(f"{r2.countdown = }") # r2.countdown = 9
print(f"{r3.countdown = }") # r3.countdown = 8
print(f"{r1.countdown = }") # r1.countdown = 7
print(f"{r2.countdown = }") # r2.countdown = 6
print(f"{r3.countdown = }") # r3.countdown = 5
print(f"{r1.countdown = }") # r1.countdown = 4
print(f"{r2.countdown = }") # r2.countdown = 3
print(f"{r3.countdown = }") # r3.countdown = 2
print(f"{r1.countdown = }") # r1.countdown = 1
print(f"{r2.countdown = }") # r2.countdown = 0
print(f"{r3.countdown = }") # r3.countdown = 10
print(f"{r1.countdown = }") # r1.countdown = 9
print(f"{r2.countdown = }") # r2.countdown = 8
print(f"{r3.countdown = }") # r3.countdown = 7
print(f"{r1.countdown = }") # r1.countdown = 6
print(f"{r2.countdown = }") # r2.countdown = 5
print(f"{r3.countdown = }") # r3.countdown = 4
print(f"{r1.countdown = }") # r1.countdown = 3
print(f"{r2.countdown = }") # r2.countdown = 2
print(f"{r3.countdown = }") # r3.countdown = 1
print(f"{r1.countdown = }") # r1.countdown = 0
