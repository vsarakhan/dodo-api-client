from enum import Enum


class GetStockTransfersStatuses(str, Enum):
    CANCELLED = "Cancelled"
    CREATED = "Created"
    ORDERED = "Ordered"
    RECEIVED = "Received"
    SHIPPED = "Shipped"

    def __str__(self) -> str:
        return str(self.value)
