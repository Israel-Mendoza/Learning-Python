class Countdown:
    """Non-data descriptor."""

    def __init__(self, start):
        self.start = start + 1

    def __get__(self, instance, owner):
        """
        Returns the descriptor instance if called
        from a class. Otherwise, will decrease the
        self.start value by one and return the value.
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

print(f"Rocket 1 value: {r1.countdown}") # Rocket 1 value: 10
print(f"Rocket 2 value: {r2.countdown}") # Rocket 2 value: 9
print(f"Rocket 1 value: {r1.countdown}") # Rocket 1 value: 8
print(f"Rocket 2 value: {r2.countdown}") # Rocket 2 value: 7
print(f"Rocket 1 value: {r1.countdown}") # Rocket 1 value: 6
print(f"Rocket 2 value: {r2.countdown}") # Rocket 2 value: 5
print(f"Rocket 1 value: {r1.countdown}") # Rocket 1 value: 4
print(f"Rocket 2 value: {r2.countdown}") # Rocket 2 value: 3
print(f"Rocket 1 value: {r1.countdown}") # Rocket 1 value: 2
print(f"Rocket 2 value: {r2.countdown}") # Rocket 2 value: 1
