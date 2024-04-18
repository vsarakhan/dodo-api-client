from enum import Enum


class StockConsumptionConsumptionType(str, Enum):
    CANCELED = "Canceled"
    DEFECT = "Defect"
    GENERIC = "Generic"
    PERSONALFOOD = "PersonalFood"
    PRODUCTION = "Production"
    SALES = "Sales"

    def __str__(self) -> str:
        return str(self.value)
