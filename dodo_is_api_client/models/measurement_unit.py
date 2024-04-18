from enum import Enum


class MeasurementUnit(str, Enum):
    KILOGRAM = "Kilogram"
    LITER = "Liter"
    METER = "Meter"
    QUANTITY = "Quantity"

    def __str__(self) -> str:
        return str(self.value)
