from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.legal_entity_type import LegalEntityType


T = TypeVar("T", bound="GetLegalEntityTypesResponse200")


@_attrs_define
class GetLegalEntityTypesResponse200:
    """
    Attributes:
        legal_entity_types (Union[Unset, List['LegalEntityType']]):
    """

    legal_entity_types: Union[Unset, List["LegalEntityType"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        legal_entity_types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.legal_entity_types, Unset):
            legal_entity_types = []
            for legal_entity_types_item_data in self.legal_entity_types:
                legal_entity_types_item = legal_entity_types_item_data.to_dict()
                legal_entity_types.append(legal_entity_types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if legal_entity_types is not UNSET:
            field_dict["legalEntityTypes"] = legal_entity_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.legal_entity_type import LegalEntityType

        d = src_dict.copy()
        legal_entity_types = []
        _legal_entity_types = d.pop("legalEntityTypes", UNSET)
        for legal_entity_types_item_data in _legal_entity_types or []:
            legal_entity_types_item = LegalEntityType.from_dict(legal_entity_types_item_data)

            legal_entity_types.append(legal_entity_types_item)

        get_legal_entity_types_response_200 = cls(
            legal_entity_types=legal_entity_types,
        )

        get_legal_entity_types_response_200.additional_properties = d
        return get_legal_entity_types_response_200

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
