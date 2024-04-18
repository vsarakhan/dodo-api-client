from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.staff_incentives_by_member_item import StaffIncentivesByMemberItem


T = TypeVar("T", bound="GetStaffIncentivesByMembersResponse200")


@_attrs_define
class GetStaffIncentivesByMembersResponse200:
    """
    Attributes:
        staff_members (List['StaffIncentivesByMemberItem']): Вознаграждения по сотрудникам
    """

    staff_members: List["StaffIncentivesByMemberItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        staff_members = []
        for staff_members_item_data in self.staff_members:
            staff_members_item = staff_members_item_data.to_dict()
            staff_members.append(staff_members_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "staffMembers": staff_members,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.staff_incentives_by_member_item import StaffIncentivesByMemberItem

        d = src_dict.copy()
        staff_members = []
        _staff_members = d.pop("staffMembers")
        for staff_members_item_data in _staff_members:
            staff_members_item = StaffIncentivesByMemberItem.from_dict(staff_members_item_data)

            staff_members.append(staff_members_item)

        get_staff_incentives_by_members_response_200 = cls(
            staff_members=staff_members,
        )

        get_staff_incentives_by_members_response_200.additional_properties = d
        return get_staff_incentives_by_members_response_200

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
