import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.legal_entity_requisites_item import LegalEntityRequisitesItem


T = TypeVar("T", bound="LegalEntity")


@_attrs_define
class LegalEntity:
    """Юрлицо

    Attributes:
        id (str): Идентификатор юрлица Example: 64a23920251811ed861d0242ac120002.
        name (str): Название Example: Dodo.
        type_id (str): Идентификатор типа юрлица Example: 64a23920251811ed861d0242ac120002.
        type_name (str): Название типа юрлица (сокращённое) Example: ООО.
        requisites (List['LegalEntityRequisitesItem']): Реквизиты
        country_code (int): Код страны Example: 643.
        address (str): Адрес Example: 115280, Москва, ул. Ленинская Слобода, 19с7.
        modified_at (datetime.datetime): Дата и время изменения в формате ISO 8601 Example: 2022-10-01T08:00:00.
    """

    id: str
    name: str
    type_id: str
    type_name: str
    requisites: List["LegalEntityRequisitesItem"]
    country_code: int
    address: str
    modified_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        type_id = self.type_id

        type_name = self.type_name

        requisites = []
        for requisites_item_data in self.requisites:
            requisites_item = requisites_item_data.to_dict()
            requisites.append(requisites_item)

        country_code = self.country_code

        address = self.address

        modified_at = self.modified_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "typeId": type_id,
                "typeName": type_name,
                "requisites": requisites,
                "countryCode": country_code,
                "address": address,
                "modifiedAt": modified_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.legal_entity_requisites_item import LegalEntityRequisitesItem

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        type_id = d.pop("typeId")

        type_name = d.pop("typeName")

        requisites = []
        _requisites = d.pop("requisites")
        for requisites_item_data in _requisites:
            requisites_item = LegalEntityRequisitesItem.from_dict(requisites_item_data)

            requisites.append(requisites_item)

        country_code = d.pop("countryCode")

        address = d.pop("address")

        modified_at = isoparse(d.pop("modifiedAt"))

        legal_entity = cls(
            id=id,
            name=name,
            type_id=type_id,
            type_name=type_name,
            requisites=requisites,
            country_code=country_code,
            address=address,
            modified_at=modified_at,
        )

        legal_entity.additional_properties = d
        return legal_entity

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
