from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_staff_positions_history_response_200_history_item import (
        GetStaffPositionsHistoryResponse200HistoryItem,
    )


T = TypeVar("T", bound="GetStaffPositionsHistoryResponse200")


@_attrs_define
class GetStaffPositionsHistoryResponse200:
    """
    Attributes:
        history (List['GetStaffPositionsHistoryResponse200HistoryItem']):
        is_end_of_list_reached (bool):
    """

    history: List["GetStaffPositionsHistoryResponse200HistoryItem"]
    is_end_of_list_reached: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)

        is_end_of_list_reached = self.is_end_of_list_reached

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "history": history,
                "isEndOfListReached": is_end_of_list_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_staff_positions_history_response_200_history_item import (
            GetStaffPositionsHistoryResponse200HistoryItem,
        )

        d = src_dict.copy()
        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = GetStaffPositionsHistoryResponse200HistoryItem.from_dict(history_item_data)

            history.append(history_item)

        is_end_of_list_reached = d.pop("isEndOfListReached")

        get_staff_positions_history_response_200 = cls(
            history=history,
            is_end_of_list_reached=is_end_of_list_reached,
        )

        get_staff_positions_history_response_200.additional_properties = d
        return get_staff_positions_history_response_200

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
