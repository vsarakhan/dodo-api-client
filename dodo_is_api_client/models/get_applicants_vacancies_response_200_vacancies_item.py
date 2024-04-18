from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.staff_type_name import StaffTypeName

if TYPE_CHECKING:
    from ..models.get_applicants_vacancies_response_200_vacancies_item_unit_localities_item import (
        GetApplicantsVacanciesResponse200VacanciesItemUnitLocalitiesItem,
    )


T = TypeVar("T", bound="GetApplicantsVacanciesResponse200VacanciesItem")


@_attrs_define
class GetApplicantsVacanciesResponse200VacanciesItem:
    """
    Attributes:
        unit_id (str): Идентификатор заведения (пиццерии) Example: 2a69836ab8f583ec11ed90098ae24dff.
        unit_name (str): Название заведения Example: Сыктывкар-1.
        unit_address (str): Адрес заведения Example: Первомайская, 85 (ул. Первомайская, 85).
        unit_localities (List['GetApplicantsVacanciesResponse200VacanciesItemUnitLocalitiesItem']): Населенные пункты,
            привязанные к заведению
        position_name (str): Наименование должности Example: Пиццамейкер.
        staff_type_name (StaffTypeName): Тип сотрудника Example: KitchenMember.
        avg_incentive (float): Среднее вознаграждение за месяц Example: 45000.
        weekly_working_hours (int): Количество рабочих часов в неделю Example: 40.
    """

    unit_id: str
    unit_name: str
    unit_address: str
    unit_localities: List["GetApplicantsVacanciesResponse200VacanciesItemUnitLocalitiesItem"]
    position_name: str
    staff_type_name: StaffTypeName
    avg_incentive: float
    weekly_working_hours: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        unit_name = self.unit_name

        unit_address = self.unit_address

        unit_localities = []
        for unit_localities_item_data in self.unit_localities:
            unit_localities_item = unit_localities_item_data.to_dict()
            unit_localities.append(unit_localities_item)

        position_name = self.position_name

        staff_type_name = self.staff_type_name.value

        avg_incentive = self.avg_incentive

        weekly_working_hours = self.weekly_working_hours

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitId": unit_id,
                "unitName": unit_name,
                "unitAddress": unit_address,
                "unitLocalities": unit_localities,
                "positionName": position_name,
                "staffTypeName": staff_type_name,
                "avgIncentive": avg_incentive,
                "weeklyWorkingHours": weekly_working_hours,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_applicants_vacancies_response_200_vacancies_item_unit_localities_item import (
            GetApplicantsVacanciesResponse200VacanciesItemUnitLocalitiesItem,
        )

        d = src_dict.copy()
        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        unit_address = d.pop("unitAddress")

        unit_localities = []
        _unit_localities = d.pop("unitLocalities")
        for unit_localities_item_data in _unit_localities:
            unit_localities_item = GetApplicantsVacanciesResponse200VacanciesItemUnitLocalitiesItem.from_dict(
                unit_localities_item_data
            )

            unit_localities.append(unit_localities_item)

        position_name = d.pop("positionName")

        staff_type_name = StaffTypeName(d.pop("staffTypeName"))

        avg_incentive = d.pop("avgIncentive")

        weekly_working_hours = d.pop("weeklyWorkingHours")

        get_applicants_vacancies_response_200_vacancies_item = cls(
            unit_id=unit_id,
            unit_name=unit_name,
            unit_address=unit_address,
            unit_localities=unit_localities,
            position_name=position_name,
            staff_type_name=staff_type_name,
            avg_incentive=avg_incentive,
            weekly_working_hours=weekly_working_hours,
        )

        get_applicants_vacancies_response_200_vacancies_item.additional_properties = d
        return get_applicants_vacancies_response_200_vacancies_item

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
