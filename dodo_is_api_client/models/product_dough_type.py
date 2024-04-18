from enum import Enum


class ProductDoughType(str, Enum):
    THIN = "Thin"
    TRADITIONAL = "Traditional"

    def __str__(self) -> str:
        return str(self.value)
