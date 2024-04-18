from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.handover_time import HandoverTime


T = TypeVar("T", bound="GetProductionOrdershandovertimeResponse200")


@_attrs_define
class GetProductionOrdershandovertimeResponse200:
    """
    Attributes:
        orders_handover_time (List['HandoverTime']): Время выдачи заказа
    """

    orders_handover_time: List["HandoverTime"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        orders_handover_time = []
        for orders_handover_time_item_data in self.orders_handover_time:
            orders_handover_time_item = orders_handover_time_item_data.to_dict()
            orders_handover_time.append(orders_handover_time_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ordersHandoverTime": orders_handover_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.handover_time import HandoverTime

        d = src_dict.copy()
        orders_handover_time = []
        _orders_handover_time = d.pop("ordersHandoverTime")
        for orders_handover_time_item_data in _orders_handover_time:
            orders_handover_time_item = HandoverTime.from_dict(orders_handover_time_item_data)

            orders_handover_time.append(orders_handover_time_item)

        get_production_ordershandovertime_response_200 = cls(
            orders_handover_time=orders_handover_time,
        )

        get_production_ordershandovertime_response_200.additional_properties = d
        return get_production_ordershandovertime_response_200

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
