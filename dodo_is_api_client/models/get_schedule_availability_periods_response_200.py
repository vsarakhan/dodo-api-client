from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.availability_period import AvailabilityPeriod


T = TypeVar("T", bound="GetScheduleAvailabilityPeriodsResponse200")


@_attrs_define
class GetScheduleAvailabilityPeriodsResponse200:
    """
    Attributes:
        availability_periods (List['AvailabilityPeriod']): Интервалы времени в которые сотрудник доступен для выхода на
            смену
    """

    availability_periods: List["AvailabilityPeriod"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        availability_periods = []
        for availability_periods_item_data in self.availability_periods:
            availability_periods_item = availability_periods_item_data.to_dict()
            availability_periods.append(availability_periods_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "availabilityPeriods": availability_periods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.availability_period import AvailabilityPeriod

        d = src_dict.copy()
        availability_periods = []
        _availability_periods = d.pop("availabilityPeriods")
        for availability_periods_item_data in _availability_periods:
            availability_periods_item = AvailabilityPeriod.from_dict(availability_periods_item_data)

            availability_periods.append(availability_periods_item)

        get_schedule_availability_periods_response_200 = cls(
            availability_periods=availability_periods,
        )

        get_schedule_availability_periods_response_200.additional_properties = d
        return get_schedule_availability_periods_response_200

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
