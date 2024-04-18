from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_staff_positions_response_200_positions_item import GetStaffPositionsResponse200PositionsItem


T = TypeVar("T", bound="GetStaffPositionsResponse200")


@_attrs_define
class GetStaffPositionsResponse200:
    """
    Attributes:
        positions (Union[Unset, List['GetStaffPositionsResponse200PositionsItem']]):
    """

    positions: Union[Unset, List["GetStaffPositionsResponse200PositionsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        positions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.positions, Unset):
            positions = []
            for positions_item_data in self.positions:
                positions_item = positions_item_data.to_dict()
                positions.append(positions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if positions is not UNSET:
            field_dict["positions"] = positions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_staff_positions_response_200_positions_item import GetStaffPositionsResponse200PositionsItem

        d = src_dict.copy()
        positions = []
        _positions = d.pop("positions", UNSET)
        for positions_item_data in _positions or []:
            positions_item = GetStaffPositionsResponse200PositionsItem.from_dict(positions_item_data)

            positions.append(positions_item)

        get_staff_positions_response_200 = cls(
            positions=positions,
        )

        get_staff_positions_response_200.additional_properties = d
        return get_staff_positions_response_200

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
