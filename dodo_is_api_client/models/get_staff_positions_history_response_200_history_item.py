import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="GetStaffPositionsHistoryResponse200HistoryItem")


@_attrs_define
class GetStaffPositionsHistoryResponse200HistoryItem:
    """
    Attributes:
        staff_id (str): Идентификатор сотрудника Example: 000d3abf84c3bb2e11ec4b927ea7327f.
        unit_id (str): Идентификатор заведения (пиццерии) в которой сотрудник вступил в должность Example:
            2a69836ab8f583ec11ed90098ae24dff.
        position_id (str): Идентификатор должности сотрудника Example: 09b059ae5fceac4211eb7bf91936f57c.
        position_name (str): Должность сотрудника Example: Пиццамейкер.
        take_position_on (datetime.date): Дата начала работы на должности Example: 2022-03-09.
        leave_position_on (Union[None, datetime.date]): Дата окончания работы на должности. Null если текущая должность.
            Example: 2022-04-11.
        is_active (bool): Текущая должность
    """

    staff_id: str
    unit_id: str
    position_id: str
    position_name: str
    take_position_on: datetime.date
    leave_position_on: Union[None, datetime.date]
    is_active: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        staff_id = self.staff_id

        unit_id = self.unit_id

        position_id = self.position_id

        position_name = self.position_name

        take_position_on = self.take_position_on.isoformat()

        leave_position_on: Union[None, str]
        if isinstance(self.leave_position_on, datetime.date):
            leave_position_on = self.leave_position_on.isoformat()
        else:
            leave_position_on = self.leave_position_on

        is_active = self.is_active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "staffId": staff_id,
                "unitId": unit_id,
                "positionId": position_id,
                "positionName": position_name,
                "takePositionOn": take_position_on,
                "leavePositionOn": leave_position_on,
                "isActive": is_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        staff_id = d.pop("staffId")

        unit_id = d.pop("unitId")

        position_id = d.pop("positionId")

        position_name = d.pop("positionName")

        take_position_on = isoparse(d.pop("takePositionOn")).date()

        def _parse_leave_position_on(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                leave_position_on_type_0 = isoparse(data).date()

                return leave_position_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.date], data)

        leave_position_on = _parse_leave_position_on(d.pop("leavePositionOn"))

        is_active = d.pop("isActive")

        get_staff_positions_history_response_200_history_item = cls(
            staff_id=staff_id,
            unit_id=unit_id,
            position_id=position_id,
            position_name=position_name,
            take_position_on=take_position_on,
            leave_position_on=leave_position_on,
            is_active=is_active,
        )

        get_staff_positions_history_response_200_history_item.additional_properties = d
        return get_staff_positions_history_response_200_history_item

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
