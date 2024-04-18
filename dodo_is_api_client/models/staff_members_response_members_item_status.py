from enum import Enum


class StaffMembersResponseMembersItemStatus(str, Enum):
    ACTIVE = "Active"
    DISMISSED = "Dismissed"
    SUSPENDED = "Suspended"

    def __str__(self) -> str:
        return str(self.value)
