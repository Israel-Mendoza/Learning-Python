from datetime import datetime, timezone, timedelta
from time import sleep
from random import randint


class Timer:
    tz = timezone.utc

    def __init__(self):
        self._time_start = None
        self._time_end = None

    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)

    @staticmethod
    def current_dt_utc():
        return datetime.now(timezone.utc)

    @classmethod
    def current_dt(cls):
        return datetime.now(cls.tz)

    def start(self):
        """Starts the instance of the timer"""
        self._time_start = self.current_dt_utc()
        self._time_end = None

    def stop(self):
        """Stops the instance of the timer"""
        if self._time_start is None:
            raise TimerError("Timer hasn't been started yet!")
        self._time_end = self.current_dt_utc()

    @property
    def start_time(self):
        """The time the timer was started"""
        if self._time_start is None:
            raise TimerError("Timer hasn't been started yet!")
        return self._time_start.astimezone(self.tz)

    @property
    def end_time(self):
        """The time the timer was stopped"""
        if self._time_end is None:
            raise TimerError("Timer hasn't been stopped yet!")
        return self._time_end.astimezone(self.tz)

    @property
    def elapsed_time(self):
        """Returns the elapsed time since the start of the timer"""
        if self._time_start is None:
            raise TimerError("The timer must be started first!")
        if self._time_end is None:
            elapsed = self.current_dt_utc() - self._time_start
        else:
            elapsed = self._time_end - self._time_start
        return elapsed.total_seconds()


class TimerError(Exception):
    """A custom excepion used for the Timer class"""


Timer.set_tz(-5, "CDMX")
print(Timer.tz)

# Instantiating the Timer class
t1 = Timer()
t2 = Timer()
t3 = Timer()

try:
    t1.start_time
except TimerError as error:
    print(error)

try:
    t2.start_time
except TimerError as error:
    print(error)

try:
    t3.start_time
except TimerError as error:
    print(error)

t1.start()
sleep(randint(0, 5))
t1.stop()
print(f"\nStart time: {t1.start_time}")
print(f"Stop time: {t1.end_time}")
print(f"Total time elapsed: {t1.elapsed_time:.2f} seconds")
