import random


class Sensor:

    _OFFSET: int = 16

    @property
    def sample_pressure(self) -> float:
        pressure_telemetry_value: float = self.simulate_pressure()
        return Sensor._OFFSET + pressure_telemetry_value

    @staticmethod
    def simulate_pressure() -> float:
        pressure_telemetry_value: float = 6 * random.random() * random.random()
        return pressure_telemetry_value

