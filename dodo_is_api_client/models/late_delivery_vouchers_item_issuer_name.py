from enum import Enum


class LateDeliveryVouchersItemIssuerName(str, Enum):
    CONTACT_CENTER = "Contact Center"
    SYSTEM = "System"

    def __str__(self) -> str:
        return str(self.value)
