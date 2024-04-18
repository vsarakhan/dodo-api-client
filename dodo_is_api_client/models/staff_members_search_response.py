from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.staff_match import StaffMatch


T = TypeVar("T", bound="StaffMembersSearchResponse")


@_attrs_define
class StaffMembersSearchResponse:
    """Результат поиска по сотрудникам

    Attributes:
        staff_matches (Union[Unset, List['StaffMatch']]):
    """

    staff_matches: Union[Unset, List["StaffMatch"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        staff_matches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.staff_matches, Unset):
            staff_matches = []
            for staff_matches_item_data in self.staff_matches:
                staff_matches_item = staff_matches_item_data.to_dict()
                staff_matches.append(staff_matches_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if staff_matches is not UNSET:
            field_dict["staffMatches"] = staff_matches

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.staff_match import StaffMatch

        d = src_dict.copy()
        staff_matches = []
        _staff_matches = d.pop("staffMatches", UNSET)
        for staff_matches_item_data in _staff_matches or []:
            staff_matches_item = StaffMatch.from_dict(staff_matches_item_data)

            staff_matches.append(staff_matches_item)

        staff_members_search_response = cls(
            staff_matches=staff_matches,
        )

        staff_members_search_response.additional_properties = d
        return staff_members_search_response

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
