from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.stock_consumption import StockConsumption


T = TypeVar("T", bound="GetStockConsumptionsByPeriodResponse200")


@_attrs_define
class GetStockConsumptionsByPeriodResponse200:
    """
    Attributes:
        consumptions (List['StockConsumption']): Список записей о расходах сырья
        is_end_of_list_reached (bool): Индикатор того, что достигнут конец списка. Выдаёт true, если достигнут конец
            списка.
    """

    consumptions: List["StockConsumption"]
    is_end_of_list_reached: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        consumptions = []
        for consumptions_item_data in self.consumptions:
            consumptions_item = consumptions_item_data.to_dict()
            consumptions.append(consumptions_item)

        is_end_of_list_reached = self.is_end_of_list_reached

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "consumptions": consumptions,
                "isEndOfListReached": is_end_of_list_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stock_consumption import StockConsumption

        d = src_dict.copy()
        consumptions = []
        _consumptions = d.pop("consumptions")
        for consumptions_item_data in _consumptions:
            consumptions_item = StockConsumption.from_dict(consumptions_item_data)

            consumptions.append(consumptions_item)

        is_end_of_list_reached = d.pop("isEndOfListReached")

        get_stock_consumptions_by_period_response_200 = cls(
            consumptions=consumptions,
            is_end_of_list_reached=is_end_of_list_reached,
        )

        get_stock_consumptions_by_period_response_200.additional_properties = d
        return get_stock_consumptions_by_period_response_200

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
