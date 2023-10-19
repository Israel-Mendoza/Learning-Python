from time import sleep
from random import randint
from datetime import datetime, timezone, timedelta


class Timer:
    tz: timezone = timezone.utc

    def __init__(self) -> None:
        self._time_start: datetime | None = None
        self._time_end: datetime | None = None

    def start(self) -> None:
        """Starts the instance of the timer"""
        self._time_start = self.current_dt_utc()
        self._time_end = None

    def stop(self) -> None:
        """Stops the instance of the timer"""
        if self._time_start is None:
            raise TimerError("Timer hasn't been started yet!")
        self._time_end: datetime = self.current_dt_utc()

    @property
    def start_time(self) -> datetime:
        """The time the timer was started"""
        if self._time_start is None:
            raise TimerError("Timer hasn't been started yet!")
        return self._time_start.astimezone(self.tz)

    @property
    def end_time(self) -> datetime:
        """The time the timer was stopped"""
        if self._time_end is None:
            raise TimerError("Timer hasn't been stopped yet!")
        return self._time_end.astimezone(self.tz)

    @property
    def elapsed_time(self) -> float:
        """Returns the elapsed time since the start of the timer"""
        if self._time_start is None:
            raise TimerError("The timer must be started first!")
        if self._time_end is None:
            elapsed = self.current_dt_utc() - self._time_start
        else:
            elapsed = self._time_end - self._time_start
        return elapsed.total_seconds()

    @classmethod
    def set_tz(cls, offset: float, name: str) -> None:
        """Sets the class' timezone information"""
        cls.tz = timezone(timedelta(hours=offset), name)

    @classmethod
    def current_dt(cls) -> datetime:
        """Returns the current datetime, set with the class timezone"""
        return datetime.now(cls.tz)

    @staticmethod
    def current_dt_utc() -> datetime:
        """Returns the current datetime, set with the passed timezone information"""
        return datetime.now(timezone.utc)


class TimerError(Exception):
    """A custom exception used for the Timer class"""
    pass


Timer.set_tz(-5, "CDMX")
print(Timer.tz)
# CDMX


# Instantiating the Timer class
t1: Timer = Timer()
t2: Timer = Timer()
t3: Timer = Timer()


# Creating start_time placeholder:
start_time: datetime | None = None

try:
    start_time = t1.start_time
except TimerError as error:
    print(error)
# Timer hasn't been started yet!

try:
    start_time = t2.start_time
except TimerError as error:
    print(error)
# Timer hasn't been started yet!

try:
    start_time = t3.start_time
except TimerError as error:
    print(error)
# Timer hasn't been started yet!

t1.start()
sleep(randint(0, 5))
t1.stop()
print(f"\nStart time: {t1.start_time}")
# Start time: 2023-03-31 14:55:03.884109-05:00
print(f"Stop time: {t1.end_time}")
# Stop time: 2023-03-31 14:55:06.885079-05:00
print(f"Total time elapsed: {t1.elapsed_time:.2f} seconds")
# Total time elapsed: 3.00 seconds
