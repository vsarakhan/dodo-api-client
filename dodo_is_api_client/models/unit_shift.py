import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnitShift")


@_attrs_define
class UnitShift:
    """Смена заведения

    Attributes:
        id (str): Идентификатор смены Example: 000d3a240c719a8711e68aba13f7f862.
        unit_id (str): Идентификатор заведения Example: 000d3a240c719a8711e68aba13f7fe13.
        unit_name (str): Название заведения Example: Сыктывкар-1.
        started_at_local (datetime.datetime): Дата и время начала смены в формате ISO 8601 (локальное время) Example:
            2022-10-01T08:00:00.
        is_open (bool): Индикатор того, что смена открыта
        opened_by_user_id (str): Id пользователя, который открыл смену Example: 000d3a240c719a8711e68aba13f7fe13.
        previous_shift_ended_at_local (Union[None, Unset, datetime.datetime]): Дата и время окончания предыдущей смены в
            формате ISO 8601 (локальное время) Example: 2022-10-01T08:00:00.
        ended_at_local (Union[None, Unset, datetime.datetime]): Дата и время окончания смены в формате ISO 8601
            (локальное время) Example: 2022-10-01T23:00:00.
        previous_shift_ended_at (Union[None, Unset, datetime.datetime]): Дата и время окончания предыдущей смены в
            формате ISO 8601 (Возвращает локальное время вместо UTC) Example: 2022-10-01T08:00:00.
        started_at (Union[Unset, datetime.datetime]): Дата и время начала смены в формате ISO 8601 (Возвращает локальное
            время вместо UTC) Example: 2022-10-01T08:00:00.
        ended_at (Union[None, Unset, datetime.datetime]): Дата и время окончания смены в формате ISO 8601 (Возвращает
            локальное время вместо UTC) Example: 2022-10-01T23:00:00.
    """

    id: str
    unit_id: str
    unit_name: str
    started_at_local: datetime.datetime
    is_open: bool
    opened_by_user_id: str
    previous_shift_ended_at_local: Union[None, Unset, datetime.datetime] = UNSET
    ended_at_local: Union[None, Unset, datetime.datetime] = UNSET
    previous_shift_ended_at: Union[None, Unset, datetime.datetime] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    ended_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        unit_id = self.unit_id

        unit_name = self.unit_name

        started_at_local = self.started_at_local.isoformat()

        is_open = self.is_open

        opened_by_user_id = self.opened_by_user_id

        previous_shift_ended_at_local: Union[None, Unset, str]
        if isinstance(self.previous_shift_ended_at_local, Unset):
            previous_shift_ended_at_local = UNSET
        elif isinstance(self.previous_shift_ended_at_local, datetime.datetime):
            previous_shift_ended_at_local = self.previous_shift_ended_at_local.isoformat()
        else:
            previous_shift_ended_at_local = self.previous_shift_ended_at_local

        ended_at_local: Union[None, Unset, str]
        if isinstance(self.ended_at_local, Unset):
            ended_at_local = UNSET
        elif isinstance(self.ended_at_local, datetime.datetime):
            ended_at_local = self.ended_at_local.isoformat()
        else:
            ended_at_local = self.ended_at_local

        previous_shift_ended_at: Union[None, Unset, str]
        if isinstance(self.previous_shift_ended_at, Unset):
            previous_shift_ended_at = UNSET
        elif isinstance(self.previous_shift_ended_at, datetime.datetime):
            previous_shift_ended_at = self.previous_shift_ended_at.isoformat()
        else:
            previous_shift_ended_at = self.previous_shift_ended_at

        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        ended_at: Union[None, Unset, str]
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "unitId": unit_id,
                "unitName": unit_name,
                "startedAtLocal": started_at_local,
                "isOpen": is_open,
                "openedByUserId": opened_by_user_id,
            }
        )
        if previous_shift_ended_at_local is not UNSET:
            field_dict["previousShiftEndedAtLocal"] = previous_shift_ended_at_local
        if ended_at_local is not UNSET:
            field_dict["endedAtLocal"] = ended_at_local
        if previous_shift_ended_at is not UNSET:
            field_dict["previousShiftEndedAt"] = previous_shift_ended_at
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        started_at_local = isoparse(d.pop("startedAtLocal"))

        is_open = d.pop("isOpen")

        opened_by_user_id = d.pop("openedByUserId")

        def _parse_previous_shift_ended_at_local(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                previous_shift_ended_at_local_type_0 = isoparse(data)

                return previous_shift_ended_at_local_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        previous_shift_ended_at_local = _parse_previous_shift_ended_at_local(d.pop("previousShiftEndedAtLocal", UNSET))

        def _parse_ended_at_local(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_local_type_0 = isoparse(data)

                return ended_at_local_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        ended_at_local = _parse_ended_at_local(d.pop("endedAtLocal", UNSET))

        def _parse_previous_shift_ended_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                previous_shift_ended_at_type_0 = isoparse(data)

                return previous_shift_ended_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        previous_shift_ended_at = _parse_previous_shift_ended_at(d.pop("previousShiftEndedAt", UNSET))

        _started_at = d.pop("startedAt", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        def _parse_ended_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = isoparse(data)

                return ended_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        ended_at = _parse_ended_at(d.pop("endedAt", UNSET))

        unit_shift = cls(
            id=id,
            unit_id=unit_id,
            unit_name=unit_name,
            started_at_local=started_at_local,
            is_open=is_open,
            opened_by_user_id=opened_by_user_id,
            previous_shift_ended_at_local=previous_shift_ended_at_local,
            ended_at_local=ended_at_local,
            previous_shift_ended_at=previous_shift_ended_at,
            started_at=started_at,
            ended_at=ended_at,
        )

        unit_shift.additional_properties = d
        return unit_shift

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
