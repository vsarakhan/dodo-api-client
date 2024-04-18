from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetCashboxesIdsResponse200IdsItem")


@_attrs_define
class GetCashboxesIdsResponse200IdsItem:
    """
    Attributes:
        id (str): Идентификатор кассы Example: 64a23920251811ed861d0242ac120002.
        obsolete_id (int): Устаревший идентификатор кассы Example: 1.
    """

    id: str
    obsolete_id: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        obsolete_id = self.obsolete_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "obsoleteId": obsolete_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        obsolete_id = d.pop("obsoleteId")

        get_cashboxes_ids_response_200_ids_item = cls(
            id=id,
            obsolete_id=obsolete_id,
        )

        get_cashboxes_ids_response_200_ids_item.additional_properties = d
        return get_cashboxes_ids_response_200_ids_item

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
