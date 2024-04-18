from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LegalEntityType")


@_attrs_define
class LegalEntityType:
    """Тип юрлица

    Attributes:
        id (str): Идентификатор типа юрлица Example: 64a23920251811ed861d0242ac120002.
        full_name (str): Полное название Example: Общество с ограниченной ответственностью.
        short_name (str): Сокращенное название Example: ООО.
        country_code (int): Код страны Example: 643.
    """

    id: str
    full_name: str
    short_name: str
    country_code: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        full_name = self.full_name

        short_name = self.short_name

        country_code = self.country_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fullName": full_name,
                "shortName": short_name,
                "countryCode": country_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        full_name = d.pop("fullName")

        short_name = d.pop("shortName")

        country_code = d.pop("countryCode")

        legal_entity_type = cls(
            id=id,
            full_name=full_name,
            short_name=short_name,
            country_code=country_code,
        )

        legal_entity_type.additional_properties = d
        return legal_entity_type

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
