import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AvailabilityPeriod")


@_attrs_define
class AvailabilityPeriod:
    """
    Attributes:
        staff_id (str): Идентификатор сотрудника Example: 000d3abf84c3bb2e11ec4b927ea7327f.
        unit_id (str): Идентификатор заведения (пиццерии) Example: 2a69836ab8f583ec11ed90098ae24dff.
        position_id (str): Идентификатор текущей должности сотрудника на данный момент. Example:
            09b059ae5fceac4211eb7bf91936f57c.
        from_local (datetime.datetime): Дата и время начала периода в формате ISO 8601 Example: 2000-01-01T00:00:00.
        to_local (datetime.datetime): Дата и время окончания периода в формате ISO 8601 Example: 2000-01-02T00:00:00.
    """

    staff_id: str
    unit_id: str
    position_id: str
    from_local: datetime.datetime
    to_local: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        staff_id = self.staff_id

        unit_id = self.unit_id

        position_id = self.position_id

        from_local = self.from_local.isoformat()

        to_local = self.to_local.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "staffId": staff_id,
                "unitId": unit_id,
                "positionId": position_id,
                "fromLocal": from_local,
                "toLocal": to_local,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        staff_id = d.pop("staffId")

        unit_id = d.pop("unitId")

        position_id = d.pop("positionId")

        from_local = isoparse(d.pop("fromLocal"))

        to_local = isoparse(d.pop("toLocal"))

        availability_period = cls(
            staff_id=staff_id,
            unit_id=unit_id,
            position_id=position_id,
            from_local=from_local,
            to_local=to_local,
        )

        availability_period.additional_properties = d
        return availability_period

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
