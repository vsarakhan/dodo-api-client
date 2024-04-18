from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostStaffShiftsClockOutBody")


@_attrs_define
class PostStaffShiftsClockOutBody:
    """
    Attributes:
        staff_shift_id (str): Идентификатор смены сотрудника Example: 2a69836ab8f583ec11ed90098ae24dff.
    """

    staff_shift_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        staff_shift_id = self.staff_shift_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "staffShiftId": staff_shift_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        staff_shift_id = d.pop("staffShiftId")

        post_staff_shifts_clock_out_body = cls(
            staff_shift_id=staff_shift_id,
        )

        post_staff_shifts_clock_out_body.additional_properties = d
        return post_staff_shifts_clock_out_body

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
