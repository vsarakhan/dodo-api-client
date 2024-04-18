from enum import Enum


class ProductMeasurementUnit(str, Enum):
    CENTIMETER = "Centimeter"
    CHINAITEM = "ChinaItem"
    FLUIDOUNCE = "FluidOunce"
    FOOT = "Foot"
    GALLON = "Gallon"
    GRAM = "Gram"
    INCH = "Inch"
    ITEM = "Item"
    KILOGRAM = "Kilogram"
    LITER = "Liter"
    METER = "Meter"
    MILLILITER = "Milliliter"
    MILLIMETER = "Millimeter"
    OUNCE = "Ounce"
    PARTOFSALAD = "PartOfSalad"
    PIECE = "Piece"
    PORTION = "Portion"
    POUND = "Pound"
    TON = "Ton"

    def __str__(self) -> str:
        return str(self.value)
