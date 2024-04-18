from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.courier_on_shift_reponse import CourierOnShiftReponse


T = TypeVar("T", bound="GetStaffMembersCuriersOnShiftResponse200")


@_attrs_define
class GetStaffMembersCuriersOnShiftResponse200:
    """
    Attributes:
        couriers (List['CourierOnShiftReponse']): Курьеры на смене
    """

    couriers: List["CourierOnShiftReponse"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        couriers = []
        for couriers_item_data in self.couriers:
            couriers_item = couriers_item_data.to_dict()
            couriers.append(couriers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "couriers": couriers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.courier_on_shift_reponse import CourierOnShiftReponse

        d = src_dict.copy()
        couriers = []
        _couriers = d.pop("couriers")
        for couriers_item_data in _couriers:
            couriers_item = CourierOnShiftReponse.from_dict(couriers_item_data)

            couriers.append(couriers_item)

        get_staff_members_curiers_on_shift_response_200 = cls(
            couriers=couriers,
        )

        get_staff_members_curiers_on_shift_response_200.additional_properties = d
        return get_staff_members_curiers_on_shift_response_200

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
