from enum import Enum


class StaffMatchStatus(str, Enum):
    ACTIVE = "Active"
    DISMISSED = "Dismissed"
    SUSPENDED = "Suspended"

    def __str__(self) -> str:
        return str(self.value)
