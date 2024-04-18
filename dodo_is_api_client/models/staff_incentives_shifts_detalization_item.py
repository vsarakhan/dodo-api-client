import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.staff_incentives_shifts_detalization_item_staff_type import StaffIncentivesShiftsDetalizationItemStaffType

T = TypeVar("T", bound="StaffIncentivesShiftsDetalizationItem")


@_attrs_define
class StaffIncentivesShiftsDetalizationItem:
    """
    Attributes:
        shift_id (str): Идентификатор смены
        unit_id (str): Идентификатор заведения
        staff_type (StaffIncentivesShiftsDetalizationItemStaffType): Тип сотрудника Example: KitchenMember.
        position_name (str): Должность (категория) сотрудника на смене
        employment_type_id (str): Идентификатор типа трудоустройства
        clock_in_at_local (datetime.datetime): Дата и время начала смены в формате ISO 8601 (локальное время) Example:
            2019-08-24T14:15:22.
        clock_out_at_local (datetime.datetime): Дата и время окончания смены в формате ISO
            8601 (локальное время) Example: 2019-08-24T14:15:22.
        night_shift_wage (float): Вознаграждение за работу в ночные часы
        day_shift_wage (float): Вознаграждение за работу в дневные часы
        orders_wage (float): Вознаграждение за доставленные заказы
        trips_distance_wage (float): Вознаграждение за пройденное расстояние
        trips_count_wage (float): Вознаграждение за количество поездок
        shift_premiums (float): Сумма премий менеджера смены
        shift_premiums_comment (str): Комментарии к премиям менеджера смены
        seniority_bonus (float): Вознаграждение за стаж
        total_wage (float): Итоговое вознаграждение за смену
    """

    shift_id: str
    unit_id: str
    staff_type: StaffIncentivesShiftsDetalizationItemStaffType
    position_name: str
    employment_type_id: str
    clock_in_at_local: datetime.datetime
    clock_out_at_local: datetime.datetime
    night_shift_wage: float
    day_shift_wage: float
    orders_wage: float
    trips_distance_wage: float
    trips_count_wage: float
    shift_premiums: float
    shift_premiums_comment: str
    seniority_bonus: float
    total_wage: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shift_id = self.shift_id

        unit_id = self.unit_id

        staff_type = self.staff_type.value

        position_name = self.position_name

        employment_type_id = self.employment_type_id

        clock_in_at_local = self.clock_in_at_local.isoformat()

        clock_out_at_local = self.clock_out_at_local.isoformat()

        night_shift_wage = self.night_shift_wage

        day_shift_wage = self.day_shift_wage

        orders_wage = self.orders_wage

        trips_distance_wage = self.trips_distance_wage

        trips_count_wage = self.trips_count_wage

        shift_premiums = self.shift_premiums

        shift_premiums_comment = self.shift_premiums_comment

        seniority_bonus = self.seniority_bonus

        total_wage = self.total_wage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shiftId": shift_id,
                "unitId": unit_id,
                "staffType": staff_type,
                "positionName": position_name,
                "employmentTypeId": employment_type_id,
                "clockInAtLocal": clock_in_at_local,
                "clockOutAtLocal": clock_out_at_local,
                "nightShiftWage": night_shift_wage,
                "dayShiftWage": day_shift_wage,
                "ordersWage": orders_wage,
                "tripsDistanceWage": trips_distance_wage,
                "tripsCountWage": trips_count_wage,
                "shiftPremiums": shift_premiums,
                "shiftPremiumsComment": shift_premiums_comment,
                "seniorityBonus": seniority_bonus,
                "totalWage": total_wage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        shift_id = d.pop("shiftId")

        unit_id = d.pop("unitId")

        staff_type = StaffIncentivesShiftsDetalizationItemStaffType(d.pop("staffType"))

        position_name = d.pop("positionName")

        employment_type_id = d.pop("employmentTypeId")

        clock_in_at_local = isoparse(d.pop("clockInAtLocal"))

        clock_out_at_local = isoparse(d.pop("clockOutAtLocal"))

        night_shift_wage = d.pop("nightShiftWage")

        day_shift_wage = d.pop("dayShiftWage")

        orders_wage = d.pop("ordersWage")

        trips_distance_wage = d.pop("tripsDistanceWage")

        trips_count_wage = d.pop("tripsCountWage")

        shift_premiums = d.pop("shiftPremiums")

        shift_premiums_comment = d.pop("shiftPremiumsComment")

        seniority_bonus = d.pop("seniorityBonus")

        total_wage = d.pop("totalWage")

        staff_incentives_shifts_detalization_item = cls(
            shift_id=shift_id,
            unit_id=unit_id,
            staff_type=staff_type,
            position_name=position_name,
            employment_type_id=employment_type_id,
            clock_in_at_local=clock_in_at_local,
            clock_out_at_local=clock_out_at_local,
            night_shift_wage=night_shift_wage,
            day_shift_wage=day_shift_wage,
            orders_wage=orders_wage,
            trips_distance_wage=trips_distance_wage,
            trips_count_wage=trips_count_wage,
            shift_premiums=shift_premiums,
            shift_premiums_comment=shift_premiums_comment,
            seniority_bonus=seniority_bonus,
            total_wage=total_wage,
        )

        staff_incentives_shifts_detalization_item.additional_properties = d
        return staff_incentives_shifts_detalization_item

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
