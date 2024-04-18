from enum import Enum


class GetStaffMembersIdFindby(str, Enum):
    STAFFID = "staffid"
    USERID = "userid"

    def __str__(self) -> str:
        return str(self.value)
