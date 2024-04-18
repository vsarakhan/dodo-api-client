from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_applicants_vacancies_response_200_vacancies_item import (
        GetApplicantsVacanciesResponse200VacanciesItem,
    )


T = TypeVar("T", bound="GetApplicantsVacanciesResponse200")


@_attrs_define
class GetApplicantsVacanciesResponse200:
    """
    Attributes:
        vacancies (List['GetApplicantsVacanciesResponse200VacanciesItem']):
        is_end_of_list_reached (bool):
    """

    vacancies: List["GetApplicantsVacanciesResponse200VacanciesItem"]
    is_end_of_list_reached: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vacancies = []
        for vacancies_item_data in self.vacancies:
            vacancies_item = vacancies_item_data.to_dict()
            vacancies.append(vacancies_item)

        is_end_of_list_reached = self.is_end_of_list_reached

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vacancies": vacancies,
                "isEndOfListReached": is_end_of_list_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_applicants_vacancies_response_200_vacancies_item import (
            GetApplicantsVacanciesResponse200VacanciesItem,
        )

        d = src_dict.copy()
        vacancies = []
        _vacancies = d.pop("vacancies")
        for vacancies_item_data in _vacancies:
            vacancies_item = GetApplicantsVacanciesResponse200VacanciesItem.from_dict(vacancies_item_data)

            vacancies.append(vacancies_item)

        is_end_of_list_reached = d.pop("isEndOfListReached")

        get_applicants_vacancies_response_200 = cls(
            vacancies=vacancies,
            is_end_of_list_reached=is_end_of_list_reached,
        )

        get_applicants_vacancies_response_200.additional_properties = d
        return get_applicants_vacancies_response_200

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
