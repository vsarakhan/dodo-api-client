from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.orders_handover_statistics import OrdersHandoverStatistics


T = TypeVar("T", bound="GetProductionOrdersHandoverTimeStatisticsResponse200")


@_attrs_define
class GetProductionOrdersHandoverTimeStatisticsResponse200:
    """
    Attributes:
        orders_handover_statistics (Union[Unset, List['OrdersHandoverStatistics']]): Статистика выдачи заказов
    """

    orders_handover_statistics: Union[Unset, List["OrdersHandoverStatistics"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        orders_handover_statistics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.orders_handover_statistics, Unset):
            orders_handover_statistics = []
            for orders_handover_statistics_item_data in self.orders_handover_statistics:
                orders_handover_statistics_item = orders_handover_statistics_item_data.to_dict()
                orders_handover_statistics.append(orders_handover_statistics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if orders_handover_statistics is not UNSET:
            field_dict["ordersHandoverStatistics"] = orders_handover_statistics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.orders_handover_statistics import OrdersHandoverStatistics

        d = src_dict.copy()
        orders_handover_statistics = []
        _orders_handover_statistics = d.pop("ordersHandoverStatistics", UNSET)
        for orders_handover_statistics_item_data in _orders_handover_statistics or []:
            orders_handover_statistics_item = OrdersHandoverStatistics.from_dict(orders_handover_statistics_item_data)

            orders_handover_statistics.append(orders_handover_statistics_item)

        get_production_orders_handover_time_statistics_response_200 = cls(
            orders_handover_statistics=orders_handover_statistics,
        )

        get_production_orders_handover_time_statistics_response_200.additional_properties = d
        return get_production_orders_handover_time_statistics_response_200

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
