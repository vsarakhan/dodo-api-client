from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApplicantsVacanciesCountResponse200UnitsItemMetroStationsItem")


@_attrs_define
class GetApplicantsVacanciesCountResponse200UnitsItemMetroStationsItem:
    """
    Attributes:
        name (str): Название стацнии метро
    """

    name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        get_applicants_vacancies_count_response_200_units_item_metro_stations_item = cls(
            name=name,
        )

        get_applicants_vacancies_count_response_200_units_item_metro_stations_item.additional_properties = d
        return get_applicants_vacancies_count_response_200_units_item_metro_stations_item

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
