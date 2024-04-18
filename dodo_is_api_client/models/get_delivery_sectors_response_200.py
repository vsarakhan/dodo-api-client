from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.delivery_sectors_item import DeliverySectorsItem


T = TypeVar("T", bound="GetDeliverySectorsResponse200")


@_attrs_define
class GetDeliverySectorsResponse200:
    """
    Attributes:
        delivery_sectors (List['DeliverySectorsItem']): Данные по секторам доставки
    """

    delivery_sectors: List["DeliverySectorsItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delivery_sectors = []
        for delivery_sectors_item_data in self.delivery_sectors:
            delivery_sectors_item = delivery_sectors_item_data.to_dict()
            delivery_sectors.append(delivery_sectors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deliverySectors": delivery_sectors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.delivery_sectors_item import DeliverySectorsItem

        d = src_dict.copy()
        delivery_sectors = []
        _delivery_sectors = d.pop("deliverySectors")
        for delivery_sectors_item_data in _delivery_sectors:
            delivery_sectors_item = DeliverySectorsItem.from_dict(delivery_sectors_item_data)

            delivery_sectors.append(delivery_sectors_item)

        get_delivery_sectors_response_200 = cls(
            delivery_sectors=delivery_sectors,
        )

        get_delivery_sectors_response_200.additional_properties = d
        return get_delivery_sectors_response_200

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
