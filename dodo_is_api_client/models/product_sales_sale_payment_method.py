from enum import Enum


class ProductSalesSalePaymentMethod(str, Enum):
    AGGREGATOR = "Aggregator"
    CARD = "Card"
    CASH = "Cash"
    ONLINE = "Online"

    def __str__(self) -> str:
        return str(self.value)
