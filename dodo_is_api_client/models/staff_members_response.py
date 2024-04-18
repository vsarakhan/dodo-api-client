from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.staff_members_response_members_item import StaffMembersResponseMembersItem


T = TypeVar("T", bound="StaffMembersResponse")


@_attrs_define
class StaffMembersResponse:
    """Список сотрудников (с постраничным выводом)

    Attributes:
        members (Union[Unset, List['StaffMembersResponseMembersItem']]):
        skipped_count (Union[Unset, int]): Количество записей, пропущенных в результате выполнения запроса Example: 100.
        taken_count (Union[Unset, int]): Количество записей, выбранных в результате выполнения запроса Example: 100.
        total_count (Union[Unset, int]): Количество всех записей, удовлетворяющих заданным параметрам фильтрации, без
            учета постраничного вывода Example: 10000.
    """

    members: Union[Unset, List["StaffMembersResponseMembersItem"]] = UNSET
    skipped_count: Union[Unset, int] = UNSET
    taken_count: Union[Unset, int] = UNSET
    total_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        members: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        skipped_count = self.skipped_count

        taken_count = self.taken_count

        total_count = self.total_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if members is not UNSET:
            field_dict["members"] = members
        if skipped_count is not UNSET:
            field_dict["skippedCount"] = skipped_count
        if taken_count is not UNSET:
            field_dict["takenCount"] = taken_count
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.staff_members_response_members_item import StaffMembersResponseMembersItem

        d = src_dict.copy()
        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = StaffMembersResponseMembersItem.from_dict(members_item_data)

            members.append(members_item)

        skipped_count = d.pop("skippedCount", UNSET)

        taken_count = d.pop("takenCount", UNSET)

        total_count = d.pop("totalCount", UNSET)

        staff_members_response = cls(
            members=members,
            skipped_count=skipped_count,
            taken_count=taken_count,
            total_count=total_count,
        )

        staff_members_response.additional_properties = d
        return staff_members_response

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
