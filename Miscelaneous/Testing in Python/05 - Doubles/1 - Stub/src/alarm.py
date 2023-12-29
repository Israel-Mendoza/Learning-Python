from src.sensor import Sensor


class Alarm:

    def __init__(self, sensor: Sensor | None = None) -> None:
        self._low_pressure_threshold: float = 17.0
        self._high_pressure_threshold: float = 21.0
        self._sensor = sensor or Sensor()
        self._is_alarm_on: bool = False

    @property
    def low_pressure_threshold(self) -> float:
        return self._low_pressure_threshold

    @property
    def high_pressure_threshold(self) -> float:
        return self._high_pressure_threshold

    @property
    def is_alarm_on(self) -> bool:
        return self._is_alarm_on

    def check(self) -> None:
        pressure: float = self._sensor.sample_pressure
        if pressure <= self.low_pressure_threshold or pressure >= self.high_pressure_threshold:
            self._is_alarm_on = True
