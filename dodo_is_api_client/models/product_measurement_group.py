from enum import Enum


class ProductMeasurementGroup(str, Enum):
    LARGE = "Large"
    MEDIUM = "Medium"
    STANDARD = "Standard"

    def __str__(self) -> str:
        return str(self.value)
