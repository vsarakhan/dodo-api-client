from enum import Enum


class StockItemCategoryName(str, Enum):
    CONSUMABLES = "Consumables"
    FINISHEDPRODUCT = "FinishedProduct"
    INGREDIENT = "Ingredient"
    INVENTORY = "Inventory"
    PACKING = "Packing"
    SEMIFINISHEDPRODUCT = "SemiFinishedProduct"

    def __str__(self) -> str:
        return str(self.value)
