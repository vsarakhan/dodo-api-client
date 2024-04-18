from enum import Enum


class ProductSalesSaleCashBoxType(str, Enum):
    DELIVERY = "Delivery"
    DINE_IN = "Dine-in"

    def __str__(self) -> str:
        return str(self.value)
