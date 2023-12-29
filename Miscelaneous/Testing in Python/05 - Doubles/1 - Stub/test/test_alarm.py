from unittest.mock import Mock
from src.alarm import Alarm
from src.sensor import Sensor


"""A Stub is an object that responds with fixed, pre-prepared data. """


"""Using MOCK from unittest to create a stub"""


def test_alarm_is_off_by_default() -> None:
    alarm = Alarm()
    assert not alarm.is_alarm_on


def test_alarm_should_be_on_when_pressure_equals_lower_threshold_mock() -> None:
    # Creating a Sensor instance in Mock mode.
    stub = Mock(Sensor)
    # Overriding the "sample_pressure" property return value
    stub.sample_pressure = 17.0  # For methods, overriding looks like this: "stub.sample_pressure.return_value = 17.0

    # Passing the stub to the Alarm
    alarm = Alarm(stub)
    alarm.check()
    assert alarm.is_alarm_on


def test_alarm_should_be_on_when_pressure_lower_than_lower_threshold_mock() -> None:
    # Creating a Sensor instance in Mock mode.
    stub = Mock(Sensor)
    # Overriding the "sample_pressure" property return value
    stub.sample_pressure = 16.0  # For methods, overriding looks like this: "stub.sample_pressure.return_value = 16.0

    # Passing the stub to the Alarm
    alarm = Alarm(stub)
    alarm.check()
    assert alarm.is_alarm_on


def test_alarm_should_be_on_when_pressure_equals_higher_threshold_mock() -> None:
    # Creating a Sensor instance in Mock mode.
    stub = Mock(Sensor)
    #  Overriding the "sample_pressure" property return value
    stub.sample_pressure = 21.0  # For methods, overriding looks like this: "stub.sample_pressure.return_value = 16.0

    # Passing the stub to the Alarm
    alarm = Alarm(stub)
    alarm.check()
    assert alarm.is_alarm_on


def test_alarm_should_be_on_when_pressure_higher_than_higher_threshold_mock() -> None:
    # Creating a Sensor instance in Mock mode.
    stub = Mock(Sensor)
    #  Overriding the "sample_pressure" property return value
    stub.sample_pressure = 22.0  # For methods, overriding looks like this: "stub.sample_pressure.return_value = 22.0

    # Passing the stub to the Alarm
    alarm = Alarm(stub)
    alarm.check()
    assert alarm.is_alarm_on


"""Using a Stub class instead"""


class StubSensor(Sensor):
    """Stub class that will replace the Sensor during the tests"""

    def __init__(self, sample_pressure: float) -> None:
        """The value returned by the sample_pressure property will be hard coded upon object creation"""
        self._sample_pressure: float = sample_pressure

    @property
    def sample_pressure(self) -> float:
        return self._sample_pressure


def test_alarm_should_be_on_pressure_equals_lower_threshold_stub() -> None:
    alarm = Alarm(StubSensor(17.0))
    alarm.check()
    assert alarm.is_alarm_on


def test_alarm_should_be_on_when_pressure_is_lower_than_lower_threshold_stub() -> None:
    alarm = Alarm(StubSensor(16.0))
    alarm.check()
    assert alarm.is_alarm_on


def test_alarm_should_be_on_when_pressure_equals_higher_threshold_stub() -> None:
    alarm = Alarm(StubSensor(21.0))
    alarm.check()
    assert alarm.is_alarm_on


def test_alarm_should_be_on_when_pressure_higher_than_higher_threshold_stub() -> None:
    alarm = Alarm(StubSensor(22.0))
    alarm.check()
    assert alarm.is_alarm_on
