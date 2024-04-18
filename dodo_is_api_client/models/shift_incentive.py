import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ShiftIncentive")


@_attrs_define
class ShiftIncentive:
    """Вознаграждение за смену

    Attributes:
        id (str): Идентификатор смены Example: 045d6a240y879a3111e68aba13f7gt15.
        unit_id (str): Идентификатор заведения Example: 000d3a240c719a8711e68aba13f7fe13.
        employment_type_id (str): Идентификатор типа трудоустройства Example: 000d3a240c719a8711e68aba13f7fe75.
        employment_type_name (str): Тип трудоустройства Example: Самозанятый.
        category_name (str): Должность (категория) сотрудника на смене Example: Автомобильный.
        clock_in (datetime.datetime): Дата и время начала смены в формате ISO 8601 Example: 2016-01-01T11:31:42.
        clock_out (datetime.datetime): Дата и время окончания смены в формате ISO 8601 Example: 2016-01-01T20:41:01.
        seniority (int): Стаж сотрудника в месяцах Example: 11.
        delivered_orders_count (int): Количество доставленных заказов Example: 59.
        total_trips_distance (float): Расстояние всех поездок за смену в метрах Example: 91.
        total_trips_count (int): Количество всех поездок за смену Example: 13.
        day_shift_minutes (int): Дневное время смены в минутах Example: 454.
        night_shift_minutes (int): Ночное время смены в минутах Example: 38.
        total_wage (float): Итого вознаграждение за смену Example: 5210.
        last_modified_at (datetime.datetime): Дата и время последнего редактирования смены Example: 2016-01-01T20:41:01.
    """

    id: str
    unit_id: str
    employment_type_id: str
    employment_type_name: str
    category_name: str
    clock_in: datetime.datetime
    clock_out: datetime.datetime
    seniority: int
    delivered_orders_count: int
    total_trips_distance: float
    total_trips_count: int
    day_shift_minutes: int
    night_shift_minutes: int
    total_wage: float
    last_modified_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        unit_id = self.unit_id

        employment_type_id = self.employment_type_id

        employment_type_name = self.employment_type_name

        category_name = self.category_name

        clock_in = self.clock_in.isoformat()

        clock_out = self.clock_out.isoformat()

        seniority = self.seniority

        delivered_orders_count = self.delivered_orders_count

        total_trips_distance = self.total_trips_distance

        total_trips_count = self.total_trips_count

        day_shift_minutes = self.day_shift_minutes

        night_shift_minutes = self.night_shift_minutes

        total_wage = self.total_wage

        last_modified_at = self.last_modified_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "unitId": unit_id,
                "employmentTypeId": employment_type_id,
                "employmentTypeName": employment_type_name,
                "categoryName": category_name,
                "clockIn": clock_in,
                "clockOut": clock_out,
                "seniority": seniority,
                "deliveredOrdersCount": delivered_orders_count,
                "totalTripsDistance": total_trips_distance,
                "totalTripsCount": total_trips_count,
                "dayShiftMinutes": day_shift_minutes,
                "nightShiftMinutes": night_shift_minutes,
                "totalWage": total_wage,
                "lastModifiedAt": last_modified_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        unit_id = d.pop("unitId")

        employment_type_id = d.pop("employmentTypeId")

        employment_type_name = d.pop("employmentTypeName")

        category_name = d.pop("categoryName")

        clock_in = isoparse(d.pop("clockIn"))

        clock_out = isoparse(d.pop("clockOut"))

        seniority = d.pop("seniority")

        delivered_orders_count = d.pop("deliveredOrdersCount")

        total_trips_distance = d.pop("totalTripsDistance")

        total_trips_count = d.pop("totalTripsCount")

        day_shift_minutes = d.pop("dayShiftMinutes")

        night_shift_minutes = d.pop("nightShiftMinutes")

        total_wage = d.pop("totalWage")

        last_modified_at = isoparse(d.pop("lastModifiedAt"))

        shift_incentive = cls(
            id=id,
            unit_id=unit_id,
            employment_type_id=employment_type_id,
            employment_type_name=employment_type_name,
            category_name=category_name,
            clock_in=clock_in,
            clock_out=clock_out,
            seniority=seniority,
            delivered_orders_count=delivered_orders_count,
            total_trips_distance=total_trips_distance,
            total_trips_count=total_trips_count,
            day_shift_minutes=day_shift_minutes,
            night_shift_minutes=night_shift_minutes,
            total_wage=total_wage,
            last_modified_at=last_modified_at,
        )

        shift_incentive.additional_properties = d
        return shift_incentive

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
