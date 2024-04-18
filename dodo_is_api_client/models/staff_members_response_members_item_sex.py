from enum import Enum


class StaffMembersResponseMembersItemSex(str, Enum):
    FEMALE = "Female"
    MALE = "Male"

    def __str__(self) -> str:
        return str(self.value)
