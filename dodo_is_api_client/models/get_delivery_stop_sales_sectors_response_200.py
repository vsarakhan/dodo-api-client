from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.stop_sales_by_sectors_item import StopSalesBySectorsItem


T = TypeVar("T", bound="GetDeliveryStopSalesSectorsResponse200")


@_attrs_define
class GetDeliveryStopSalesSectorsResponse200:
    """
    Attributes:
        stop_sales_by_sectors (List['StopSalesBySectorsItem']): Данные о стопах продаж сгруппированные по заведениям и
            секторам
    """

    stop_sales_by_sectors: List["StopSalesBySectorsItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stop_sales_by_sectors = []
        for stop_sales_by_sectors_item_data in self.stop_sales_by_sectors:
            stop_sales_by_sectors_item = stop_sales_by_sectors_item_data.to_dict()
            stop_sales_by_sectors.append(stop_sales_by_sectors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stopSalesBySectors": stop_sales_by_sectors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stop_sales_by_sectors_item import StopSalesBySectorsItem

        d = src_dict.copy()
        stop_sales_by_sectors = []
        _stop_sales_by_sectors = d.pop("stopSalesBySectors")
        for stop_sales_by_sectors_item_data in _stop_sales_by_sectors:
            stop_sales_by_sectors_item = StopSalesBySectorsItem.from_dict(stop_sales_by_sectors_item_data)

            stop_sales_by_sectors.append(stop_sales_by_sectors_item)

        get_delivery_stop_sales_sectors_response_200 = cls(
            stop_sales_by_sectors=stop_sales_by_sectors,
        )

        get_delivery_stop_sales_sectors_response_200.additional_properties = d
        return get_delivery_stop_sales_sectors_response_200

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
