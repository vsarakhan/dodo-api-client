from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApplicantsVacanciesCountResponse200UnitsItemLocationType0")


@_attrs_define
class GetApplicantsVacanciesCountResponse200UnitsItemLocationType0:
    """Координаты заведения. Null возвращется, если координаты заведения не заведены в системе или имеют невалидный формат.

    Attributes:
        latitude (float): Широта Example: 43.909233.
        longitude (float): Долгота Example: 39.331818.
    """

    latitude: float
    longitude: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "latitude": latitude,
                "longitude": longitude,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        get_applicants_vacancies_count_response_200_units_item_location_type_0 = cls(
            latitude=latitude,
            longitude=longitude,
        )

        get_applicants_vacancies_count_response_200_units_item_location_type_0.additional_properties = d
        return get_applicants_vacancies_count_response_200_units_item_location_type_0

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
