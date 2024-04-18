from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_applicants_vacancies_count_response_200_units_item_localities_item import (
        GetApplicantsVacanciesCountResponse200UnitsItemLocalitiesItem,
    )
    from ..models.get_applicants_vacancies_count_response_200_units_item_location_type_0 import (
        GetApplicantsVacanciesCountResponse200UnitsItemLocationType0,
    )
    from ..models.get_applicants_vacancies_count_response_200_units_item_metro_stations_item import (
        GetApplicantsVacanciesCountResponse200UnitsItemMetroStationsItem,
    )


T = TypeVar("T", bound="GetApplicantsVacanciesCountResponse200UnitsItem")


@_attrs_define
class GetApplicantsVacanciesCountResponse200UnitsItem:
    """
    Attributes:
        id (str): Идентификатор заведения (пиццерии) Example: 2a69836ab8f583ec11ed90098ae24dff.
        name (str):  Example: Сыктывкар-1.
        address (str): Адрес заведения Example: Первомайская, 85 (ул. Первомайская, 85).
        localities (List['GetApplicantsVacanciesCountResponse200UnitsItemLocalitiesItem']): Населенные пункты,
            привязанные к заведению
        vacancies_count (float): Количество вакансий в заведении Example: 10.
        location (Union['GetApplicantsVacanciesCountResponse200UnitsItemLocationType0', None]): Координаты заведения.
            Null возвращется, если координаты заведения не заведены в системе или имеют невалидный формат.
        metro_stations (List['GetApplicantsVacanciesCountResponse200UnitsItemMetroStationsItem']): Список станций метро
            связанных с заведением
    """

    id: str
    name: str
    address: str
    localities: List["GetApplicantsVacanciesCountResponse200UnitsItemLocalitiesItem"]
    vacancies_count: float
    location: Union["GetApplicantsVacanciesCountResponse200UnitsItemLocationType0", None]
    metro_stations: List["GetApplicantsVacanciesCountResponse200UnitsItemMetroStationsItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.get_applicants_vacancies_count_response_200_units_item_location_type_0 import (
            GetApplicantsVacanciesCountResponse200UnitsItemLocationType0,
        )

        id = self.id

        name = self.name

        address = self.address

        localities = []
        for localities_item_data in self.localities:
            localities_item = localities_item_data.to_dict()
            localities.append(localities_item)

        vacancies_count = self.vacancies_count

        location: Union[Dict[str, Any], None]
        if isinstance(self.location, GetApplicantsVacanciesCountResponse200UnitsItemLocationType0):
            location = self.location.to_dict()
        else:
            location = self.location

        metro_stations = []
        for metro_stations_item_data in self.metro_stations:
            metro_stations_item = metro_stations_item_data.to_dict()
            metro_stations.append(metro_stations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "address": address,
                "localities": localities,
                "vacanciesCount": vacancies_count,
                "location": location,
                "metroStations": metro_stations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_applicants_vacancies_count_response_200_units_item_localities_item import (
            GetApplicantsVacanciesCountResponse200UnitsItemLocalitiesItem,
        )
        from ..models.get_applicants_vacancies_count_response_200_units_item_location_type_0 import (
            GetApplicantsVacanciesCountResponse200UnitsItemLocationType0,
        )
        from ..models.get_applicants_vacancies_count_response_200_units_item_metro_stations_item import (
            GetApplicantsVacanciesCountResponse200UnitsItemMetroStationsItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        address = d.pop("address")

        localities = []
        _localities = d.pop("localities")
        for localities_item_data in _localities:
            localities_item = GetApplicantsVacanciesCountResponse200UnitsItemLocalitiesItem.from_dict(
                localities_item_data
            )

            localities.append(localities_item)

        vacancies_count = d.pop("vacanciesCount")

        def _parse_location(
            data: object,
        ) -> Union["GetApplicantsVacanciesCountResponse200UnitsItemLocationType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = GetApplicantsVacanciesCountResponse200UnitsItemLocationType0.from_dict(data)

                return location_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GetApplicantsVacanciesCountResponse200UnitsItemLocationType0", None], data)

        location = _parse_location(d.pop("location"))

        metro_stations = []
        _metro_stations = d.pop("metroStations")
        for metro_stations_item_data in _metro_stations:
            metro_stations_item = GetApplicantsVacanciesCountResponse200UnitsItemMetroStationsItem.from_dict(
                metro_stations_item_data
            )

            metro_stations.append(metro_stations_item)

        get_applicants_vacancies_count_response_200_units_item = cls(
            id=id,
            name=name,
            address=address,
            localities=localities,
            vacancies_count=vacancies_count,
            location=location,
            metro_stations=metro_stations,
        )

        get_applicants_vacancies_count_response_200_units_item.additional_properties = d
        return get_applicants_vacancies_count_response_200_units_item

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
