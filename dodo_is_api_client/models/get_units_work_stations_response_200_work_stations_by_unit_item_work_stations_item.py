from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetUnitsWorkStationsResponse200WorkStationsByUnitItemWorkStationsItem")


@_attrs_define
class GetUnitsWorkStationsResponse200WorkStationsByUnitItemWorkStationsItem:
    """
    Attributes:
        id (str): Идентификатор производственной станции Example: 2a69836ab8f583ec11ed90098ae24dff.
        name (str): Производственная станция (Доставка, Кухня, Касса) Example: Кухня.
        sub_station_name (str): Производственная подстанция (Холодный цех, Чистота и тд) Example: Холодный цех.
        available_staff_positions (List[str]): Должности сотрудников которые могут работать на данной производственной
            станции Example: ['2a69836ab8f583ec11ed90098ae24dff'].
    """

    id: str
    name: str
    sub_station_name: str
    available_staff_positions: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        sub_station_name = self.sub_station_name

        available_staff_positions = self.available_staff_positions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "subStationName": sub_station_name,
                "availableStaffPositions": available_staff_positions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        sub_station_name = d.pop("subStationName")

        available_staff_positions = cast(List[str], d.pop("availableStaffPositions"))

        get_units_work_stations_response_200_work_stations_by_unit_item_work_stations_item = cls(
            id=id,
            name=name,
            sub_station_name=sub_station_name,
            available_staff_positions=available_staff_positions,
        )

        get_units_work_stations_response_200_work_stations_by_unit_item_work_stations_item.additional_properties = d
        return get_units_work_stations_response_200_work_stations_by_unit_item_work_stations_item

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
