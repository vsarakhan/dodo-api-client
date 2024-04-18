from enum import Enum


class StockWriteOffReason(str, Enum):
    DAMAGEDPACKAGING = "DamagedPackaging"
    DEFECTED = "Defected"
    EXPIRED = "Expired"
    EXPIREDSHOWCASETIME = "ExpiredShowcaseTime"
    HUMANELEMENT = "HumanElement"
    MARKETING = "Marketing"
    SHOWCASEWRITEOFF = "ShowcaseWriteOff"

    def __str__(self) -> str:
        return str(self.value)
