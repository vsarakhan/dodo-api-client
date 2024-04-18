from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.staff_shift_item import StaffShiftItem


T = TypeVar("T", bound="GetStaffShiftsResponse200")


@_attrs_define
class GetStaffShiftsResponse200:
    """
    Attributes:
        shifts (List['StaffShiftItem']): Смены (рабочее время) сотрудников
        is_end_of_list_reached (bool): Индикатор того, что достигнут конец списка. Выдаёт true, если достигнут конец
            списка.
    """

    shifts: List["StaffShiftItem"]
    is_end_of_list_reached: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shifts = []
        for shifts_item_data in self.shifts:
            shifts_item = shifts_item_data.to_dict()
            shifts.append(shifts_item)

        is_end_of_list_reached = self.is_end_of_list_reached

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shifts": shifts,
                "isEndOfListReached": is_end_of_list_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.staff_shift_item import StaffShiftItem

        d = src_dict.copy()
        shifts = []
        _shifts = d.pop("shifts")
        for shifts_item_data in _shifts:
            shifts_item = StaffShiftItem.from_dict(shifts_item_data)

            shifts.append(shifts_item)

        is_end_of_list_reached = d.pop("isEndOfListReached")

        get_staff_shifts_response_200 = cls(
            shifts=shifts,
            is_end_of_list_reached=is_end_of_list_reached,
        )

        get_staff_shifts_response_200.additional_properties = d
        return get_staff_shifts_response_200

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
