from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.couriers_orders_item import CouriersOrdersItem


T = TypeVar("T", bound="GetDeliveryCouriersOrdersResponse200")


@_attrs_define
class GetDeliveryCouriersOrdersResponse200:
    """
    Attributes:
        is_end_of_list_reached (bool): Индикатор того, что достигнут конец списка. Выдаёт true, если достигнут конец
            списка.
        couriers_orders (Union[Unset, List['CouriersOrdersItem']]): Заказы курьеров
    """

    is_end_of_list_reached: bool
    couriers_orders: Union[Unset, List["CouriersOrdersItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_end_of_list_reached = self.is_end_of_list_reached

        couriers_orders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.couriers_orders, Unset):
            couriers_orders = []
            for couriers_orders_item_data in self.couriers_orders:
                couriers_orders_item = couriers_orders_item_data.to_dict()
                couriers_orders.append(couriers_orders_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEndOfListReached": is_end_of_list_reached,
            }
        )
        if couriers_orders is not UNSET:
            field_dict["couriersOrders"] = couriers_orders

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.couriers_orders_item import CouriersOrdersItem

        d = src_dict.copy()
        is_end_of_list_reached = d.pop("isEndOfListReached")

        couriers_orders = []
        _couriers_orders = d.pop("couriersOrders", UNSET)
        for couriers_orders_item_data in _couriers_orders or []:
            couriers_orders_item = CouriersOrdersItem.from_dict(couriers_orders_item_data)

            couriers_orders.append(couriers_orders_item)

        get_delivery_couriers_orders_response_200 = cls(
            is_end_of_list_reached=is_end_of_list_reached,
            couriers_orders=couriers_orders,
        )

        get_delivery_couriers_orders_response_200.additional_properties = d
        return get_delivery_couriers_orders_response_200

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
