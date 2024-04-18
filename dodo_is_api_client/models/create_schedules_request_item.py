import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="CreateSchedulesRequestItem")


@_attrs_define
class CreateSchedulesRequestItem:
    """
    Attributes:
        unit_id (str): Идентификатор заведения (пиццерии) Example: 2a69836ab8f583ec11ed90098ae24dff.
        staff_id (str): Идентификатор сотрудника Example: 2a69836ab8f583ec11ed90098ae24dff.
        scheduled_shift_start_at_local (datetime.datetime): Запланированное начало смены (локальное время).
            Передаются в разрезе 15-ти минут.
            Формат:
             - YYYY-MM-DDTHH:00:00
             - YYYY-MM-DDTHH:15:00
             - YYYY-MM-DDTHH:30:00
             - YYYY-MM-DDTHH:45:00 Example: 2022-01-01T12:00:00.
        scheduled_shift_end_at_local (datetime.datetime): Запланированный конец смены (локальное время).
            Передаются в разрезе 15-ти минут.
            Формат:
             - YYYY-MM-DDTHH:00:00
             - YYYY-MM-DDTHH:15:00
             - YYYY-MM-DDTHH:30:00
             - YYYY-MM-DDTHH:45:00 Example: 2022-01-01T12:30:00.
        work_station_id (str): Идентификатор производственной станции Example: 2a69836ab8f583ec11ed90098ae24dff.
        shift_position_id (str): Идентификатор должности сотрудника на смене, если она отличалась от текущей должности
            сотрудника Example: 2a69836ab8f583ec11ed90098ae24dff.
    """

    unit_id: str
    staff_id: str
    scheduled_shift_start_at_local: datetime.datetime
    scheduled_shift_end_at_local: datetime.datetime
    work_station_id: str
    shift_position_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        staff_id = self.staff_id

        scheduled_shift_start_at_local = self.scheduled_shift_start_at_local.isoformat()

        scheduled_shift_end_at_local = self.scheduled_shift_end_at_local.isoformat()

        work_station_id = self.work_station_id

        shift_position_id = self.shift_position_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitId": unit_id,
                "staffId": staff_id,
                "scheduledShiftStartAtLocal": scheduled_shift_start_at_local,
                "scheduledShiftEndAtLocal": scheduled_shift_end_at_local,
                "workStationId": work_station_id,
                "shiftPositionId": shift_position_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit_id = d.pop("unitId")

        staff_id = d.pop("staffId")

        scheduled_shift_start_at_local = isoparse(d.pop("scheduledShiftStartAtLocal"))

        scheduled_shift_end_at_local = isoparse(d.pop("scheduledShiftEndAtLocal"))

        work_station_id = d.pop("workStationId")

        shift_position_id = d.pop("shiftPositionId")

        create_schedules_request_item = cls(
            unit_id=unit_id,
            staff_id=staff_id,
            scheduled_shift_start_at_local=scheduled_shift_start_at_local,
            scheduled_shift_end_at_local=scheduled_shift_end_at_local,
            work_station_id=work_station_id,
            shift_position_id=shift_position_id,
        )

        create_schedules_request_item.additional_properties = d
        return create_schedules_request_item

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
