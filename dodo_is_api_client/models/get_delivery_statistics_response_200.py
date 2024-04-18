from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.unit_delivery_statistics import UnitDeliveryStatistics


T = TypeVar("T", bound="GetDeliveryStatisticsResponse200")


@_attrs_define
class GetDeliveryStatisticsResponse200:
    """
    Attributes:
        units_statistics (List['UnitDeliveryStatistics']): Основные метрики доставки
    """

    units_statistics: List["UnitDeliveryStatistics"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        units_statistics = []
        for units_statistics_item_data in self.units_statistics:
            units_statistics_item = units_statistics_item_data.to_dict()
            units_statistics.append(units_statistics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitsStatistics": units_statistics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.unit_delivery_statistics import UnitDeliveryStatistics

        d = src_dict.copy()
        units_statistics = []
        _units_statistics = d.pop("unitsStatistics")
        for units_statistics_item_data in _units_statistics:
            units_statistics_item = UnitDeliveryStatistics.from_dict(units_statistics_item_data)

            units_statistics.append(units_statistics_item)

        get_delivery_statistics_response_200 = cls(
            units_statistics=units_statistics,
        )

        get_delivery_statistics_response_200.additional_properties = d
        return get_delivery_statistics_response_200

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
