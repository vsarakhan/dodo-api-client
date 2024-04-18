from enum import Enum


class StaffShiftItemStaffTypeName(str, Enum):
    CASHIER = "Cashier"
    COURIER = "Courier"
    KITCHENMEMBER = "KitchenMember"
    OPERATOR = "Operator"
    PERSONALMANAGER = "PersonalManager"

    def __str__(self) -> str:
        return str(self.value)
