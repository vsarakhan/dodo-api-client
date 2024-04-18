from enum import Enum


class HandoverTimeSalesChannel(str, Enum):
    DELIVERY = "Delivery"
    DINE_IN = "Dine-in"
    TAKEAWAY = "Takeaway"

    def __str__(self) -> str:
        return str(self.value)
