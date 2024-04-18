from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_units_work_stations_response_200_work_stations_by_unit_item import (
        GetUnitsWorkStationsResponse200WorkStationsByUnitItem,
    )


T = TypeVar("T", bound="GetUnitsWorkStationsResponse200")


@_attrs_define
class GetUnitsWorkStationsResponse200:
    """
    Attributes:
        work_stations_by_unit (List['GetUnitsWorkStationsResponse200WorkStationsByUnitItem']):
    """

    work_stations_by_unit: List["GetUnitsWorkStationsResponse200WorkStationsByUnitItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        work_stations_by_unit = []
        for work_stations_by_unit_item_data in self.work_stations_by_unit:
            work_stations_by_unit_item = work_stations_by_unit_item_data.to_dict()
            work_stations_by_unit.append(work_stations_by_unit_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workStationsByUnit": work_stations_by_unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_units_work_stations_response_200_work_stations_by_unit_item import (
            GetUnitsWorkStationsResponse200WorkStationsByUnitItem,
        )

        d = src_dict.copy()
        work_stations_by_unit = []
        _work_stations_by_unit = d.pop("workStationsByUnit")
        for work_stations_by_unit_item_data in _work_stations_by_unit:
            work_stations_by_unit_item = GetUnitsWorkStationsResponse200WorkStationsByUnitItem.from_dict(
                work_stations_by_unit_item_data
            )

            work_stations_by_unit.append(work_stations_by_unit_item)

        get_units_work_stations_response_200 = cls(
            work_stations_by_unit=work_stations_by_unit,
        )

        get_units_work_stations_response_200.additional_properties = d
        return get_units_work_stations_response_200

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
