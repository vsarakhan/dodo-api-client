from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.staff_meal import StaffMeal


T = TypeVar("T", bound="GetStaffMealsResponse200")


@_attrs_define
class GetStaffMealsResponse200:
    """
    Attributes:
        staff_meals (List['StaffMeal']):
        is_end_of_list_reached (bool): Индикатор того, что достигнут конец списка. Выдаёт true, если достигнут конец
            списка.
    """

    staff_meals: List["StaffMeal"]
    is_end_of_list_reached: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        staff_meals = []
        for staff_meals_item_data in self.staff_meals:
            staff_meals_item = staff_meals_item_data.to_dict()
            staff_meals.append(staff_meals_item)

        is_end_of_list_reached = self.is_end_of_list_reached

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "staffMeals": staff_meals,
                "isEndOfListReached": is_end_of_list_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.staff_meal import StaffMeal

        d = src_dict.copy()
        staff_meals = []
        _staff_meals = d.pop("staffMeals")
        for staff_meals_item_data in _staff_meals:
            staff_meals_item = StaffMeal.from_dict(staff_meals_item_data)

            staff_meals.append(staff_meals_item)

        is_end_of_list_reached = d.pop("isEndOfListReached")

        get_staff_meals_response_200 = cls(
            staff_meals=staff_meals,
            is_end_of_list_reached=is_end_of_list_reached,
        )

        get_staff_meals_response_200.additional_properties = d
        return get_staff_meals_response_200

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
