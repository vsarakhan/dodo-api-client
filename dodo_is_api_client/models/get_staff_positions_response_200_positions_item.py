from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_staff_positions_response_200_positions_item_staff_type_name import (
    GetStaffPositionsResponse200PositionsItemStaffTypeName,
)

T = TypeVar("T", bound="GetStaffPositionsResponse200PositionsItem")


@_attrs_define
class GetStaffPositionsResponse200PositionsItem:
    """
    Attributes:
        id (str): Идентификатор должности сотрудника на смене Example: 09b059ae5fceac4211eb7bf91936f57c.
        name (str): Наименование должности Example: Автомобильный.
        staff_type_name (GetStaffPositionsResponse200PositionsItemStaffTypeName): Тип сотрудника. `Operator` - оператор,
            `KitchenMember` - работник кухни, `Courier` - курьер, `Cashier` - кассир, `PersonalManager` - менеджер офиса
            Example: KitchenMember.
    """

    id: str
    name: str
    staff_type_name: GetStaffPositionsResponse200PositionsItemStaffTypeName
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        staff_type_name = self.staff_type_name.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "staffTypeName": staff_type_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        staff_type_name = GetStaffPositionsResponse200PositionsItemStaffTypeName(d.pop("staffTypeName"))

        get_staff_positions_response_200_positions_item = cls(
            id=id,
            name=name,
            staff_type_name=staff_type_name,
        )

        get_staff_positions_response_200_positions_item.additional_properties = d
        return get_staff_positions_response_200_positions_item

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
