from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.stock_transfer import StockTransfer


T = TypeVar("T", bound="GetStockTransfersResponse200")


@_attrs_define
class GetStockTransfersResponse200:
    """
    Attributes:
        transfers (List['StockTransfer']): Список записей о расходах сырья
        is_end_of_list_reached (bool): Индикатор того, что достигнут конец списка. Выдаёт true, если достигнут конец
            списка.
    """

    transfers: List["StockTransfer"]
    is_end_of_list_reached: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transfers = []
        for transfers_item_data in self.transfers:
            transfers_item = transfers_item_data.to_dict()
            transfers.append(transfers_item)

        is_end_of_list_reached = self.is_end_of_list_reached

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transfers": transfers,
                "isEndOfListReached": is_end_of_list_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stock_transfer import StockTransfer

        d = src_dict.copy()
        transfers = []
        _transfers = d.pop("transfers")
        for transfers_item_data in _transfers:
            transfers_item = StockTransfer.from_dict(transfers_item_data)

            transfers.append(transfers_item)

        is_end_of_list_reached = d.pop("isEndOfListReached")

        get_stock_transfers_response_200 = cls(
            transfers=transfers,
            is_end_of_list_reached=is_end_of_list_reached,
        )

        get_stock_transfers_response_200.additional_properties = d
        return get_stock_transfers_response_200

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
