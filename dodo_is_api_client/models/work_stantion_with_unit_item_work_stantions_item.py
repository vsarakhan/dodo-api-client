from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkStantionWithUnitItemWorkStantionsItem")


@_attrs_define
class WorkStantionWithUnitItemWorkStantionsItem:
    """
    Attributes:
        work_station_id (Union[Unset, str]): Идентификатор производственной станции Example:
            2a69836ab8f583ec11ed90098ae24dff.
        work_station_name (Union[Unset, str]): Производственная станция (Доставка, Кухня, Касса) Example: Кухня.
        work_sub_station_name (Union[Unset, str]): Производственная подстанция (Холодный цех, Чистота и тд) Example:
            Холодный цех.
    """

    work_station_id: Union[Unset, str] = UNSET
    work_station_name: Union[Unset, str] = UNSET
    work_sub_station_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        work_station_id = self.work_station_id

        work_station_name = self.work_station_name

        work_sub_station_name = self.work_sub_station_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if work_station_id is not UNSET:
            field_dict["workStationId"] = work_station_id
        if work_station_name is not UNSET:
            field_dict["workStationName"] = work_station_name
        if work_sub_station_name is not UNSET:
            field_dict["workSubStationName"] = work_sub_station_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        work_station_id = d.pop("workStationId", UNSET)

        work_station_name = d.pop("workStationName", UNSET)

        work_sub_station_name = d.pop("workSubStationName", UNSET)

        work_stantion_with_unit_item_work_stantions_item = cls(
            work_station_id=work_station_id,
            work_station_name=work_station_name,
            work_sub_station_name=work_sub_station_name,
        )

        work_stantion_with_unit_item_work_stantions_item.additional_properties = d
        return work_stantion_with_unit_item_work_stantions_item

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
