from enum import Enum


class ScheduleWorkStationNames(str, Enum):
    CASH = "Cash"
    COURIER = "Courier"
    DELIVERY = "Delivery"
    KITCHENDOUGH = "KitchenDough"
    KITCHENLINE = "KitchenLine"
    KITCHENPREP = "KitchenPrep"
    KITCHENSLICING = "KitchenSlicing"
    KITCHENSUPPLIES = "KitchenSupplies"
    SANITATION = "Sanitation"
    SUPERVISORS = "Supervisors"
    TRAINEES = "Trainees"

    def __str__(self) -> str:
        return str(self.value)
