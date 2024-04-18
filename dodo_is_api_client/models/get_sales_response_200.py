from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.product_sales_sale import ProductSalesSale


T = TypeVar("T", bound="GetSalesResponse200")


@_attrs_define
class GetSalesResponse200:
    """
    Attributes:
        sales (List['ProductSalesSale']):
        is_end_of_list_reached (bool): Индикатор того, что достигнут конец списка. Выдаёт true, если достигнут конец
            списка.
    """

    sales: List["ProductSalesSale"]
    is_end_of_list_reached: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sales = []
        for sales_item_data in self.sales:
            sales_item = sales_item_data.to_dict()
            sales.append(sales_item)

        is_end_of_list_reached = self.is_end_of_list_reached

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sales": sales,
                "isEndOfListReached": is_end_of_list_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_sales_sale import ProductSalesSale

        d = src_dict.copy()
        sales = []
        _sales = d.pop("sales")
        for sales_item_data in _sales:
            sales_item = ProductSalesSale.from_dict(sales_item_data)

            sales.append(sales_item)

        is_end_of_list_reached = d.pop("isEndOfListReached")

        get_sales_response_200 = cls(
            sales=sales,
            is_end_of_list_reached=is_end_of_list_reached,
        )

        get_sales_response_200.additional_properties = d
        return get_sales_response_200

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
