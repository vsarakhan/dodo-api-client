from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.delivery_efficiency import DeliveryEfficiency


T = TypeVar("T", bound="GetDeliveryEfficiencyResponse200")


@_attrs_define
class GetDeliveryEfficiencyResponse200:
    """
    Attributes:
        unit_delivery_efficiency (List['DeliveryEfficiency']): Еффективность доставки по пиццериям
    """

    unit_delivery_efficiency: List["DeliveryEfficiency"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_delivery_efficiency = []
        for unit_delivery_efficiency_item_data in self.unit_delivery_efficiency:
            unit_delivery_efficiency_item = unit_delivery_efficiency_item_data.to_dict()
            unit_delivery_efficiency.append(unit_delivery_efficiency_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitDeliveryEfficiency": unit_delivery_efficiency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.delivery_efficiency import DeliveryEfficiency

        d = src_dict.copy()
        unit_delivery_efficiency = []
        _unit_delivery_efficiency = d.pop("unitDeliveryEfficiency")
        for unit_delivery_efficiency_item_data in _unit_delivery_efficiency:
            unit_delivery_efficiency_item = DeliveryEfficiency.from_dict(unit_delivery_efficiency_item_data)

            unit_delivery_efficiency.append(unit_delivery_efficiency_item)

        get_delivery_efficiency_response_200 = cls(
            unit_delivery_efficiency=unit_delivery_efficiency,
        )

        get_delivery_efficiency_response_200.additional_properties = d
        return get_delivery_efficiency_response_200

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
