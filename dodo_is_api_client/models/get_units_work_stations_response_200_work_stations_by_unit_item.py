from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_units_work_stations_response_200_work_stations_by_unit_item_work_stations_item import (
        GetUnitsWorkStationsResponse200WorkStationsByUnitItemWorkStationsItem,
    )


T = TypeVar("T", bound="GetUnitsWorkStationsResponse200WorkStationsByUnitItem")


@_attrs_define
class GetUnitsWorkStationsResponse200WorkStationsByUnitItem:
    """
    Attributes:
        unit_id (str): Идентификатор заведения (пиццерии) Example: 2a69836ab8f583ec11ed90098ae24dff.
        work_stations (List['GetUnitsWorkStationsResponse200WorkStationsByUnitItemWorkStationsItem']):
    """

    unit_id: str
    work_stations: List["GetUnitsWorkStationsResponse200WorkStationsByUnitItemWorkStationsItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        work_stations = []
        for work_stations_item_data in self.work_stations:
            work_stations_item = work_stations_item_data.to_dict()
            work_stations.append(work_stations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitId": unit_id,
                "workStations": work_stations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_units_work_stations_response_200_work_stations_by_unit_item_work_stations_item import (
            GetUnitsWorkStationsResponse200WorkStationsByUnitItemWorkStationsItem,
        )

        d = src_dict.copy()
        unit_id = d.pop("unitId")

        work_stations = []
        _work_stations = d.pop("workStations")
        for work_stations_item_data in _work_stations:
            work_stations_item = GetUnitsWorkStationsResponse200WorkStationsByUnitItemWorkStationsItem.from_dict(
                work_stations_item_data
            )

            work_stations.append(work_stations_item)

        get_units_work_stations_response_200_work_stations_by_unit_item = cls(
            unit_id=unit_id,
            work_stations=work_stations,
        )

        get_units_work_stations_response_200_work_stations_by_unit_item.additional_properties = d
        return get_units_work_stations_response_200_work_stations_by_unit_item

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
