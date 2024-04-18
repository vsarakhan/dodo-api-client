from enum import Enum


class StockTransferStatus(str, Enum):
    CANCELLED = "Cancelled"
    CREATED = "Created"
    ORDERED = "Ordered"
    RECEIVED = "Received"
    SHIPPED = "Shipped"

    def __str__(self) -> str:
        return str(self.value)
