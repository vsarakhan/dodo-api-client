from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApplicantsVacanciesCountResponse200UnitsItemLocalitiesItem")


@_attrs_define
class GetApplicantsVacanciesCountResponse200UnitsItemLocalitiesItem:
    """
    Attributes:
        locality_id (str): Идентификатор населенного пункта Example: 2a69836ab8f583ec11ed90098ae24dff.
    """

    locality_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        locality_id = self.locality_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "localityId": locality_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        locality_id = d.pop("localityId")

        get_applicants_vacancies_count_response_200_units_item_localities_item = cls(
            locality_id=locality_id,
        )

        get_applicants_vacancies_count_response_200_units_item_localities_item.additional_properties = d
        return get_applicants_vacancies_count_response_200_units_item_localities_item

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
