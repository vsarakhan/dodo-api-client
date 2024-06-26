from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_schedules_request_item import CreateSchedulesRequestItem


T = TypeVar("T", bound="PostStaffSchedulesBody")


@_attrs_define
class PostStaffSchedulesBody:
    """
    Attributes:
        schedules (List['CreateSchedulesRequestItem']): Смены в расписании
    """

    schedules: List["CreateSchedulesRequestItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schedules = []
        for schedules_item_data in self.schedules:
            schedules_item = schedules_item_data.to_dict()
            schedules.append(schedules_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedules": schedules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_schedules_request_item import CreateSchedulesRequestItem

        d = src_dict.copy()
        schedules = []
        _schedules = d.pop("schedules")
        for schedules_item_data in _schedules:
            schedules_item = CreateSchedulesRequestItem.from_dict(schedules_item_data)

            schedules.append(schedules_item)

        post_staff_schedules_body = cls(
            schedules=schedules,
        )

        post_staff_schedules_body.additional_properties = d
        return post_staff_schedules_body

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
