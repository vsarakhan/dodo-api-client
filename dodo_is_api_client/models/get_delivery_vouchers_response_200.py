from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.late_delivery_vouchers_item import LateDeliveryVouchersItem


T = TypeVar("T", bound="GetDeliveryVouchersResponse200")


@_attrs_define
class GetDeliveryVouchersResponse200:
    """
    Attributes:
        vouchers (List['LateDeliveryVouchersItem']): Сертификаты за опоздание
        is_end_of_list_reached (bool): Индикатор того, что достигнут конец списка. Выдаёт true, если достигнут конец
            списка.
    """

    vouchers: List["LateDeliveryVouchersItem"]
    is_end_of_list_reached: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vouchers = []
        for vouchers_item_data in self.vouchers:
            vouchers_item = vouchers_item_data.to_dict()
            vouchers.append(vouchers_item)

        is_end_of_list_reached = self.is_end_of_list_reached

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vouchers": vouchers,
                "isEndOfListReached": is_end_of_list_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.late_delivery_vouchers_item import LateDeliveryVouchersItem

        d = src_dict.copy()
        vouchers = []
        _vouchers = d.pop("vouchers")
        for vouchers_item_data in _vouchers:
            vouchers_item = LateDeliveryVouchersItem.from_dict(vouchers_item_data)

            vouchers.append(vouchers_item)

        is_end_of_list_reached = d.pop("isEndOfListReached")

        get_delivery_vouchers_response_200 = cls(
            vouchers=vouchers,
            is_end_of_list_reached=is_end_of_list_reached,
        )

        get_delivery_vouchers_response_200.additional_properties = d
        return get_delivery_vouchers_response_200

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
