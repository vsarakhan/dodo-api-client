import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.staff_type_name import StaffTypeName

T = TypeVar("T", bound="SchedulesItem")


@_attrs_define
class SchedulesItem:
    """
    Attributes:
        id (str): Идентификатор запланированной смены Example: 2a69836ab8f583ec11ed90098ae24dff.
        scheduled_shift_end_at_local (datetime.datetime): Запланированный конец смены (локальное время) Example:
            2023-01-15T16:00:00.
        scheduled_shift_start_at_local (datetime.datetime): Запланированное начало смены (локальное время) Example:
            2023-01-15T08:00:00.
        work_station_id (str): Идентификатор производственной станции Example: 2a69836ab8f583ec11ed90098ae24dff.
        work_station_name (str): Производственная станция (Доставка, Кухня, Касса) Example: Кухня.
        work_sub_station_name (str): Производственная подстанция (Холодный цех, Чистота и тд) Example: Холодный цех.
        staff_position_id (str): Идентификатор текущей должности сотрудника на данный момент (даже если расписание за
            прошлые периоды) Example: 09b059ae5fceac4211eb7bf91936f57c.
        staff_id (str): Идентификатор сотрудника Example: 000d3abf84c3bb2e11ec4b927ea7327f.
        staff_position_name (str): Текущая должность сотрудника на данный момент (даже если расписание за прошлые
            периоды) Example: Пиццамейкер.
        staff_shift_position_id (str): Идентификатор должности сотрудника на смене, если она отличалась от текущей
            Example: 09b059ae5fceac4211eb7bf91936f57c.
        staff_shift_position_name (str): Должность сотрудника на смене, если она отличалась от текущей
        staff_type_name (StaffTypeName): Тип сотрудника Example: KitchenMember.
        unit_id (str): Идентификатор заведения (пиццерии) Example: 2a69836ab8f583ec11ed90098ae24dff.
        unit_name (str): Название заведения Example: Сыктывкар-1.
        modified_at (datetime.datetime): Дата и время последнего изменения Example: 2023-01-06T13:44:59.
        modified_by_user_id (str): Идентификатор пользователя, редактировавшего запланированную смену Example:
            000d3a22fa54a81311e92d28d355ed6e.
    """

    id: str
    scheduled_shift_end_at_local: datetime.datetime
    scheduled_shift_start_at_local: datetime.datetime
    work_station_id: str
    work_station_name: str
    work_sub_station_name: str
    staff_position_id: str
    staff_id: str
    staff_position_name: str
    staff_shift_position_id: str
    staff_shift_position_name: str
    staff_type_name: StaffTypeName
    unit_id: str
    unit_name: str
    modified_at: datetime.datetime
    modified_by_user_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        scheduled_shift_end_at_local = self.scheduled_shift_end_at_local.isoformat()

        scheduled_shift_start_at_local = self.scheduled_shift_start_at_local.isoformat()

        work_station_id = self.work_station_id

        work_station_name = self.work_station_name

        work_sub_station_name = self.work_sub_station_name

        staff_position_id = self.staff_position_id

        staff_id = self.staff_id

        staff_position_name = self.staff_position_name

        staff_shift_position_id = self.staff_shift_position_id

        staff_shift_position_name = self.staff_shift_position_name

        staff_type_name = self.staff_type_name.value

        unit_id = self.unit_id

        unit_name = self.unit_name

        modified_at = self.modified_at.isoformat()

        modified_by_user_id = self.modified_by_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "scheduledShiftEndAtLocal": scheduled_shift_end_at_local,
                "scheduledShiftStartAtLocal": scheduled_shift_start_at_local,
                "workStationId": work_station_id,
                "workStationName": work_station_name,
                "workSubStationName": work_sub_station_name,
                "staffPositionId": staff_position_id,
                "staffId": staff_id,
                "staffPositionName": staff_position_name,
                "staffShiftPositionId": staff_shift_position_id,
                "staffShiftPositionName": staff_shift_position_name,
                "staffTypeName": staff_type_name,
                "unitId": unit_id,
                "unitName": unit_name,
                "modifiedAt": modified_at,
                "modifiedByUserId": modified_by_user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        scheduled_shift_end_at_local = isoparse(d.pop("scheduledShiftEndAtLocal"))

        scheduled_shift_start_at_local = isoparse(d.pop("scheduledShiftStartAtLocal"))

        work_station_id = d.pop("workStationId")

        work_station_name = d.pop("workStationName")

        work_sub_station_name = d.pop("workSubStationName")

        staff_position_id = d.pop("staffPositionId")

        staff_id = d.pop("staffId")

        staff_position_name = d.pop("staffPositionName")

        staff_shift_position_id = d.pop("staffShiftPositionId")

        staff_shift_position_name = d.pop("staffShiftPositionName")

        staff_type_name = StaffTypeName(d.pop("staffTypeName"))

        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        modified_at = isoparse(d.pop("modifiedAt"))

        modified_by_user_id = d.pop("modifiedByUserId")

        schedules_item = cls(
            id=id,
            scheduled_shift_end_at_local=scheduled_shift_end_at_local,
            scheduled_shift_start_at_local=scheduled_shift_start_at_local,
            work_station_id=work_station_id,
            work_station_name=work_station_name,
            work_sub_station_name=work_sub_station_name,
            staff_position_id=staff_position_id,
            staff_id=staff_id,
            staff_position_name=staff_position_name,
            staff_shift_position_id=staff_shift_position_id,
            staff_shift_position_name=staff_shift_position_name,
            staff_type_name=staff_type_name,
            unit_id=unit_id,
            unit_name=unit_name,
            modified_at=modified_at,
            modified_by_user_id=modified_by_user_id,
        )

        schedules_item.additional_properties = d
        return schedules_item

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
