"""
Non-data descriptors.
We can change the behavior of the descriptor whether 
it is accessed from a class or an instance.
"""


from datetime import datetime


class UTCTime:

    """Non-data descriptor."""

    def __get__(self, instance, owner):
        """
        Returns the descriptor instance if called from a class.
        Returns the current UTC datetime in ISO format if called
        from a class instance.
        """
        if instance is None:
            return self
        else:
            return datetime.utcnow().isoformat()


class Logger:
    """A simple logger class"""

    current_time = UTCTime()


# Instantiating the Logger
logger = Logger()

"""Accessing the descriptor"""

# Expecting the descriptor's instance
print(Logger.current_time)
# <__main__.UTCTime object at 0x010BB808>

# Expecting the time string
print(logger.current_time)
# 2020-09-28T03:26:29.654123
