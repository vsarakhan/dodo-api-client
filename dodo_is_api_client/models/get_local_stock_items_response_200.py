from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.stock_item import StockItem


T = TypeVar("T", bound="GetLocalStockItemsResponse200")


@_attrs_define
class GetLocalStockItemsResponse200:
    """
    Attributes:
        stock_items (List['StockItem']): Сырье
        is_end_of_list_reached (bool): Индикатор того, что достигнут конец списка. Выдаёт true, если достигнут конец
            списка.
    """

    stock_items: List["StockItem"]
    is_end_of_list_reached: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stock_items = []
        for stock_items_item_data in self.stock_items:
            stock_items_item = stock_items_item_data.to_dict()
            stock_items.append(stock_items_item)

        is_end_of_list_reached = self.is_end_of_list_reached

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stockItems": stock_items,
                "isEndOfListReached": is_end_of_list_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stock_item import StockItem

        d = src_dict.copy()
        stock_items = []
        _stock_items = d.pop("stockItems")
        for stock_items_item_data in _stock_items:
            stock_items_item = StockItem.from_dict(stock_items_item_data)

            stock_items.append(stock_items_item)

        is_end_of_list_reached = d.pop("isEndOfListReached")

        get_local_stock_items_response_200 = cls(
            stock_items=stock_items,
            is_end_of_list_reached=is_end_of_list_reached,
        )

        get_local_stock_items_response_200.additional_properties = d
        return get_local_stock_items_response_200

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
