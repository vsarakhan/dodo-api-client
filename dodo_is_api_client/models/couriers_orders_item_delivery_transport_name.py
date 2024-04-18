from enum import Enum


class CouriersOrdersItemDeliveryTransportName(str, Enum):
    BICYCLE = "Bicycle"
    ONFOOT = "OnFoot"
    VEHICLE = "Vehicle"

    def __str__(self) -> str:
        return str(self.value)
