from enum import Enum


class ProductSalesSaleOrderSource(str, Enum):
    AGGREGATOR = "Aggregator"
    CALLCENTER = "CallCenter"
    DINE_IN = "Dine-in"
    KIOSK = "Kiosk"
    MANAGER = "Manager"
    MOBILEAPP = "MobileApp"
    WEBSITE = "Website"

    def __str__(self) -> str:
        return str(self.value)
