import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.staff_shift_item_staff_type_name import StaffShiftItemStaffTypeName

T = TypeVar("T", bound="StaffShiftItem")


@_attrs_define
class StaffShiftItem:
    """
    Attributes:
        id (str): Идентификатор смены Example: 000d3a240c719a8711e68aba13f7f862.
        staff_id (str): Идентификатор сотрудника Example: 000d3a38a8a3956a11e85cdf246d6a31.
        clock_in_at_local (datetime.datetime): Локальные дата и время начала смены в формате ISO 8601 Example:
            2016-01-01T11:31:42.
        clock_out_at_local (datetime.datetime): Локальные дата и время окончания смены в формате ISO 8601 Example:
            2016-01-01T20:41:01.
        staff_position_id (str): Id должности сотрудника на смене
        staff_position_name (str): Должность (категория) сотрудника на смене Example: Автомобильный.
        staff_type_name (StaffShiftItemStaffTypeName): Тип сотрудника. `Operator` - оператор, `KitchenMember` - работник
            кухни, `Courier` - курьер, `Cashier` - кассир, `PersonalManager` - менеджер офиса Example: KitchenMember.
        schedule_id (Union[None, str]): Идентификатор запланированной смены. Принимает значение `null` для
            незапланированной смены и для смен до 04.04.2024 Example: 000d3a38a8a3956a11e85cdf24610f83.
        seniority (int): Стаж сотрудника в месяцах Example: 11.
        delivered_orders_count (int): Количество доставленных заказов Default: 0.
        total_trips_distance (float): Расстояние всех поездок за смену в метрах Example: 91.
        total_trips_count (int): Количество всех поездок за смену Default: 0. Example: 13.
        day_shift_minutes (int): Дневное время смены в минутах
             Example: 454.
        night_shift_minutes (int): Ночное время смены в минутах Example: 59.
        holiday_minutes (int): Сколько минут от праздничного дня попало в смену (из настроек Dodo IS) Example: 31.
        last_modified_at (datetime.datetime): Дата и время последнего редактирования смены по UTC Example:
            2016-01-01T20:41:01.
        last_modified_by_user_id (str): Идентификатор пользователя, который редактировал смену Example:
            000d3a38a8a3956a11e85cdf246d6a31.
        employment_type_name (str): Тип трудоустройства Example: Самозанятый.
        employment_type_id (str): Идентификатор типа трудоустройства Example: 000d3a240c719a8711e68aba13f7fe75.
        unit_id (str): Идентификатор заведения (пиццерии) Example: 000d3a240c719a8711e68aba13f7fe13.
        unit_name (str): Название заведения Example: Сыктывкар-1.
    """

    id: str
    staff_id: str
    clock_in_at_local: datetime.datetime
    clock_out_at_local: datetime.datetime
    staff_position_id: str
    staff_position_name: str
    staff_type_name: StaffShiftItemStaffTypeName
    schedule_id: Union[None, str]
    seniority: int
    total_trips_distance: float
    day_shift_minutes: int
    night_shift_minutes: int
    holiday_minutes: int
    last_modified_at: datetime.datetime
    last_modified_by_user_id: str
    employment_type_name: str
    employment_type_id: str
    unit_id: str
    unit_name: str
    delivered_orders_count: int = 0
    total_trips_count: int = 0
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        staff_id = self.staff_id

        clock_in_at_local = self.clock_in_at_local.isoformat()

        clock_out_at_local = self.clock_out_at_local.isoformat()

        staff_position_id = self.staff_position_id

        staff_position_name = self.staff_position_name

        staff_type_name = self.staff_type_name.value

        schedule_id: Union[None, str]
        schedule_id = self.schedule_id

        seniority = self.seniority

        delivered_orders_count = self.delivered_orders_count

        total_trips_distance = self.total_trips_distance

        total_trips_count = self.total_trips_count

        day_shift_minutes = self.day_shift_minutes

        night_shift_minutes = self.night_shift_minutes

        holiday_minutes = self.holiday_minutes

        last_modified_at = self.last_modified_at.isoformat()

        last_modified_by_user_id = self.last_modified_by_user_id

        employment_type_name = self.employment_type_name

        employment_type_id = self.employment_type_id

        unit_id = self.unit_id

        unit_name = self.unit_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "staffId": staff_id,
                "clockInAtLocal": clock_in_at_local,
                "clockOutAtLocal": clock_out_at_local,
                "staffPositionId": staff_position_id,
                "staffPositionName": staff_position_name,
                "staffTypeName": staff_type_name,
                "scheduleId": schedule_id,
                "seniority": seniority,
                "deliveredOrdersCount": delivered_orders_count,
                "totalTripsDistance": total_trips_distance,
                "totalTripsCount": total_trips_count,
                "dayShiftMinutes": day_shift_minutes,
                "nightShiftMinutes": night_shift_minutes,
                "holidayMinutes": holiday_minutes,
                "lastModifiedAt": last_modified_at,
                "lastModifiedByUserId": last_modified_by_user_id,
                "employmentTypeName": employment_type_name,
                "employmentTypeId": employment_type_id,
                "unitId": unit_id,
                "unitName": unit_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        staff_id = d.pop("staffId")

        clock_in_at_local = isoparse(d.pop("clockInAtLocal"))

        clock_out_at_local = isoparse(d.pop("clockOutAtLocal"))

        staff_position_id = d.pop("staffPositionId")

        staff_position_name = d.pop("staffPositionName")

        staff_type_name = StaffShiftItemStaffTypeName(d.pop("staffTypeName"))

        def _parse_schedule_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        schedule_id = _parse_schedule_id(d.pop("scheduleId"))

        seniority = d.pop("seniority")

        delivered_orders_count = d.pop("deliveredOrdersCount")

        total_trips_distance = d.pop("totalTripsDistance")

        total_trips_count = d.pop("totalTripsCount")

        day_shift_minutes = d.pop("dayShiftMinutes")

        night_shift_minutes = d.pop("nightShiftMinutes")

        holiday_minutes = d.pop("holidayMinutes")

        last_modified_at = isoparse(d.pop("lastModifiedAt"))

        last_modified_by_user_id = d.pop("lastModifiedByUserId")

        employment_type_name = d.pop("employmentTypeName")

        employment_type_id = d.pop("employmentTypeId")

        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        staff_shift_item = cls(
            id=id,
            staff_id=staff_id,
            clock_in_at_local=clock_in_at_local,
            clock_out_at_local=clock_out_at_local,
            staff_position_id=staff_position_id,
            staff_position_name=staff_position_name,
            staff_type_name=staff_type_name,
            schedule_id=schedule_id,
            seniority=seniority,
            delivered_orders_count=delivered_orders_count,
            total_trips_distance=total_trips_distance,
            total_trips_count=total_trips_count,
            day_shift_minutes=day_shift_minutes,
            night_shift_minutes=night_shift_minutes,
            holiday_minutes=holiday_minutes,
            last_modified_at=last_modified_at,
            last_modified_by_user_id=last_modified_by_user_id,
            employment_type_name=employment_type_name,
            employment_type_id=employment_type_id,
            unit_id=unit_id,
            unit_name=unit_name,
        )

        staff_shift_item.additional_properties = d
        return staff_shift_item

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
