from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cancelled_sale import CancelledSale


T = TypeVar("T", bound="GetCancelledSalesResponse200")


@_attrs_define
class GetCancelledSalesResponse200:
    """
    Attributes:
        cancelled_sales (List['CancelledSale']):
        is_end_of_list_reached (bool): Индикатор того, что достигнут конец списка. Выдаёт true, если достигнут конец
            списка.
    """

    cancelled_sales: List["CancelledSale"]
    is_end_of_list_reached: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cancelled_sales = []
        for cancelled_sales_item_data in self.cancelled_sales:
            cancelled_sales_item = cancelled_sales_item_data.to_dict()
            cancelled_sales.append(cancelled_sales_item)

        is_end_of_list_reached = self.is_end_of_list_reached

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cancelledSales": cancelled_sales,
                "isEndOfListReached": is_end_of_list_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cancelled_sale import CancelledSale

        d = src_dict.copy()
        cancelled_sales = []
        _cancelled_sales = d.pop("cancelledSales")
        for cancelled_sales_item_data in _cancelled_sales:
            cancelled_sales_item = CancelledSale.from_dict(cancelled_sales_item_data)

            cancelled_sales.append(cancelled_sales_item)

        is_end_of_list_reached = d.pop("isEndOfListReached")

        get_cancelled_sales_response_200 = cls(
            cancelled_sales=cancelled_sales,
            is_end_of_list_reached=is_end_of_list_reached,
        )

        get_cancelled_sales_response_200.additional_properties = d
        return get_cancelled_sales_response_200

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
