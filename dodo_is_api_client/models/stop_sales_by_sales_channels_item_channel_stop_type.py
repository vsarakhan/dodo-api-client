from enum import Enum


class StopSalesBySalesChannelsItemChannelStopType(str, Enum):
    COMPLETE = "Complete"
    REDIRECTION = "Redirection"

    def __str__(self) -> str:
        return str(self.value)
