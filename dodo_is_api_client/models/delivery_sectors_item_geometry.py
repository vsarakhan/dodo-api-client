from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeliverySectorsItemGeometry")


@_attrs_define
class DeliverySectorsItemGeometry:
    """Объект в формате Geo-json, описывающий форму зоны доставки на карте

    Example:
        {"type":"Polygon","coordinates":[[[129.763343,62.032773],[129.751052,62.032828],[129.749372,62.028192],[129.7633
            43,62.032773]]]}

    """

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        delivery_sectors_item_geometry = cls()

        delivery_sectors_item_geometry.additional_properties = d
        return delivery_sectors_item_geometry

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
