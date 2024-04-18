from enum import Enum


class StaffMemberBusinessId(str, Enum):
    DODOPIZZA = "dodopizza"
    DONER42 = "doner42"
    DRINKIT = "drinkit"

    def __str__(self) -> str:
        return str(self.value)
