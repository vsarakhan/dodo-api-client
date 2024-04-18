from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.stock_write_off import StockWriteOff


T = TypeVar("T", bound="GetWriteOffsStockItemsResponse200")


@_attrs_define
class GetWriteOffsStockItemsResponse200:
    """
    Attributes:
        write_offs (List['StockWriteOff']): Список записей о списаниях сырья
        is_end_of_list_reached (bool): Индикатор того, что достигнут конец списка. Выдаёт true, если достигнут конец
            списка.
    """

    write_offs: List["StockWriteOff"]
    is_end_of_list_reached: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        write_offs = []
        for write_offs_item_data in self.write_offs:
            write_offs_item = write_offs_item_data.to_dict()
            write_offs.append(write_offs_item)

        is_end_of_list_reached = self.is_end_of_list_reached

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "writeOffs": write_offs,
                "isEndOfListReached": is_end_of_list_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stock_write_off import StockWriteOff

        d = src_dict.copy()
        write_offs = []
        _write_offs = d.pop("writeOffs")
        for write_offs_item_data in _write_offs:
            write_offs_item = StockWriteOff.from_dict(write_offs_item_data)

            write_offs.append(write_offs_item)

        is_end_of_list_reached = d.pop("isEndOfListReached")

        get_write_offs_stock_items_response_200 = cls(
            write_offs=write_offs,
            is_end_of_list_reached=is_end_of_list_reached,
        )

        get_write_offs_stock_items_response_200.additional_properties = d
        return get_write_offs_stock_items_response_200

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
