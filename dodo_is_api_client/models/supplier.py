import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.supplier_requisites_item import SupplierRequisitesItem


T = TypeVar("T", bound="Supplier")


@_attrs_define
class Supplier:
    """Поставщик

    Attributes:
        id (str): Идентификатор поставщика Example: 64a23920251811ed861d0242ac120002.
        name (str): Название Example: ООО Продукты.
        country_code (int): Код страны Example: 643.
        modified_at (datetime.datetime): Дата и время изменения в формате ISO 8601 Example: 2022-10-01T08:00:00.
        external_id (Union[Unset, str]): Внешний идентификатор поставщика Example: SUP-0001.
        requisites (Union[Unset, List['SupplierRequisitesItem']]): Реквизиты
    """

    id: str
    name: str
    country_code: int
    modified_at: datetime.datetime
    external_id: Union[Unset, str] = UNSET
    requisites: Union[Unset, List["SupplierRequisitesItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        country_code = self.country_code

        modified_at = self.modified_at.isoformat()

        external_id = self.external_id

        requisites: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.requisites, Unset):
            requisites = []
            for requisites_item_data in self.requisites:
                requisites_item = requisites_item_data.to_dict()
                requisites.append(requisites_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "countryCode": country_code,
                "modifiedAt": modified_at,
            }
        )
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if requisites is not UNSET:
            field_dict["requisites"] = requisites

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.supplier_requisites_item import SupplierRequisitesItem

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        country_code = d.pop("countryCode")

        modified_at = isoparse(d.pop("modifiedAt"))

        external_id = d.pop("externalId", UNSET)

        requisites = []
        _requisites = d.pop("requisites", UNSET)
        for requisites_item_data in _requisites or []:
            requisites_item = SupplierRequisitesItem.from_dict(requisites_item_data)

            requisites.append(requisites_item)

        supplier = cls(
            id=id,
            name=name,
            country_code=country_code,
            modified_at=modified_at,
            external_id=external_id,
            requisites=requisites,
        )

        supplier.additional_properties = d
        return supplier

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
