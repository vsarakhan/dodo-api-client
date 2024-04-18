from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_applicants_vacancies_count_response_200_units_item import (
        GetApplicantsVacanciesCountResponse200UnitsItem,
    )


T = TypeVar("T", bound="GetApplicantsVacanciesCountResponse200")


@_attrs_define
class GetApplicantsVacanciesCountResponse200:
    """
    Attributes:
        units (List['GetApplicantsVacanciesCountResponse200UnitsItem']):
        is_end_of_list_reached (bool):
    """

    units: List["GetApplicantsVacanciesCountResponse200UnitsItem"]
    is_end_of_list_reached: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        units = []
        for units_item_data in self.units:
            units_item = units_item_data.to_dict()
            units.append(units_item)

        is_end_of_list_reached = self.is_end_of_list_reached

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "units": units,
                "isEndOfListReached": is_end_of_list_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_applicants_vacancies_count_response_200_units_item import (
            GetApplicantsVacanciesCountResponse200UnitsItem,
        )

        d = src_dict.copy()
        units = []
        _units = d.pop("units")
        for units_item_data in _units:
            units_item = GetApplicantsVacanciesCountResponse200UnitsItem.from_dict(units_item_data)

            units.append(units_item)

        is_end_of_list_reached = d.pop("isEndOfListReached")

        get_applicants_vacancies_count_response_200 = cls(
            units=units,
            is_end_of_list_reached=is_end_of_list_reached,
        )

        get_applicants_vacancies_count_response_200.additional_properties = d
        return get_applicants_vacancies_count_response_200

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
