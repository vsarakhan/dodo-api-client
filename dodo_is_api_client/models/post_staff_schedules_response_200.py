from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schedules_item import SchedulesItem


T = TypeVar("T", bound="PostStaffSchedulesResponse200")


@_attrs_define
class PostStaffSchedulesResponse200:
    """
    Attributes:
        schedules (List['SchedulesItem']):
    """

    schedules: List["SchedulesItem"]
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
        from ..models.schedules_item import SchedulesItem

        d = src_dict.copy()
        schedules = []
        _schedules = d.pop("schedules")
        for schedules_item_data in _schedules:
            schedules_item = SchedulesItem.from_dict(schedules_item_data)

            schedules.append(schedules_item)

        post_staff_schedules_response_200 = cls(
            schedules=schedules,
        )

        post_staff_schedules_response_200.additional_properties = d
        return post_staff_schedules_response_200

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
