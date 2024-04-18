import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.staff_match_status import StaffMatchStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.staff_match_matches import StaffMatchMatches


T = TypeVar("T", bound="StaffMatch")


@_attrs_define
class StaffMatch:
    """Данные по сотруднику в маскированном формате

    Attributes:
        first_name (Union[Unset, str]): Имя, маскируется до 3 символов, если не передано в качестве параметра на поиск
            Example: ***ван.
        last_name (Union[Unset, str]): Фамилия, маскируется до 3 символов если не передано в качестве параметра на поиск
            Example: ***нов.
        patronymic_name (Union[None, Unset, str]): Отчество, маскируется до 3 символов если не передано в качестве
            параметра на поиск Example: ***вич.
        taxpayer_identification_number (Union[None, Unset, str]): ИНН, маскируется полностью если не передано в качестве
            параметра на поиск Example: ***.
        phone_number (Union[Unset, str]): Телефон, маскируется до 4 символов если не передано в качестве параметра на
            поиск Example: ***12-02.
        date_of_birth (Union[None, Unset, str]): Дата рождения, маскируются первые 4 символа если не передано в качестве
            параметра на поиск Example: ****-06-01.
        hired_on (Union[Unset, datetime.date]): Дата найма Example: 2015-10-01.
        dismissed_on (Union[None, Unset, datetime.date]): Дата увольнения Example: 2015-10-02.
        position_name (Union[None, Unset, str]): Должность Example: Пиццамейкер.
        position_id (Union[None, Unset, str]): Идентификатор должности Example: 000d3a240c719a8711e68aba13f7fe13.
        status (Union[Unset, StaffMatchStatus]): Состояние сотрудника `Dismissed` - уволен, `Suspended` - отстранен,
            `Active` - работает Example: Active.
        dismissal_reason (Union[None, Unset, str]): Причина увольнения Example: По инициативе работодателя.
        dismissal_comment (Union[None, Unset, str]): Комментарий к причине увольнения Example: Постоянные опоздания.
        unit_id (Union[Unset, str]): Идентификатор юнита Example: 000d3a240c719a8711e68aba13f7fe16.
        unit_name (Union[Unset, str]): Юнит Example: Москва 1-1.
        matches_count (Union[Unset, int]):  Example: 3.
        matches (Union[Unset, StaffMatchMatches]):
    """

    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    patronymic_name: Union[None, Unset, str] = UNSET
    taxpayer_identification_number: Union[None, Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    date_of_birth: Union[None, Unset, str] = UNSET
    hired_on: Union[Unset, datetime.date] = UNSET
    dismissed_on: Union[None, Unset, datetime.date] = UNSET
    position_name: Union[None, Unset, str] = UNSET
    position_id: Union[None, Unset, str] = UNSET
    status: Union[Unset, StaffMatchStatus] = UNSET
    dismissal_reason: Union[None, Unset, str] = UNSET
    dismissal_comment: Union[None, Unset, str] = UNSET
    unit_id: Union[Unset, str] = UNSET
    unit_name: Union[Unset, str] = UNSET
    matches_count: Union[Unset, int] = UNSET
    matches: Union[Unset, "StaffMatchMatches"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        patronymic_name: Union[None, Unset, str]
        if isinstance(self.patronymic_name, Unset):
            patronymic_name = UNSET
        else:
            patronymic_name = self.patronymic_name

        taxpayer_identification_number: Union[None, Unset, str]
        if isinstance(self.taxpayer_identification_number, Unset):
            taxpayer_identification_number = UNSET
        else:
            taxpayer_identification_number = self.taxpayer_identification_number

        phone_number = self.phone_number

        date_of_birth: Union[None, Unset, str]
        if isinstance(self.date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = self.date_of_birth

        hired_on: Union[Unset, str] = UNSET
        if not isinstance(self.hired_on, Unset):
            hired_on = self.hired_on.isoformat()

        dismissed_on: Union[None, Unset, str]
        if isinstance(self.dismissed_on, Unset):
            dismissed_on = UNSET
        elif isinstance(self.dismissed_on, datetime.date):
            dismissed_on = self.dismissed_on.isoformat()
        else:
            dismissed_on = self.dismissed_on

        position_name: Union[None, Unset, str]
        if isinstance(self.position_name, Unset):
            position_name = UNSET
        else:
            position_name = self.position_name

        position_id: Union[None, Unset, str]
        if isinstance(self.position_id, Unset):
            position_id = UNSET
        else:
            position_id = self.position_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        dismissal_reason: Union[None, Unset, str]
        if isinstance(self.dismissal_reason, Unset):
            dismissal_reason = UNSET
        else:
            dismissal_reason = self.dismissal_reason

        dismissal_comment: Union[None, Unset, str]
        if isinstance(self.dismissal_comment, Unset):
            dismissal_comment = UNSET
        else:
            dismissal_comment = self.dismissal_comment

        unit_id = self.unit_id

        unit_name = self.unit_name

        matches_count = self.matches_count

        matches: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.matches, Unset):
            matches = self.matches.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if patronymic_name is not UNSET:
            field_dict["patronymicName"] = patronymic_name
        if taxpayer_identification_number is not UNSET:
            field_dict["taxpayerIdentificationNumber"] = taxpayer_identification_number
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if hired_on is not UNSET:
            field_dict["hiredOn"] = hired_on
        if dismissed_on is not UNSET:
            field_dict["dismissedOn"] = dismissed_on
        if position_name is not UNSET:
            field_dict["positionName"] = position_name
        if position_id is not UNSET:
            field_dict["positionId"] = position_id
        if status is not UNSET:
            field_dict["status"] = status
        if dismissal_reason is not UNSET:
            field_dict["dismissalReason"] = dismissal_reason
        if dismissal_comment is not UNSET:
            field_dict["dismissalComment"] = dismissal_comment
        if unit_id is not UNSET:
            field_dict["unitId"] = unit_id
        if unit_name is not UNSET:
            field_dict["unitName"] = unit_name
        if matches_count is not UNSET:
            field_dict["matchesCount"] = matches_count
        if matches is not UNSET:
            field_dict["matches"] = matches

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.staff_match_matches import StaffMatchMatches

        d = src_dict.copy()
        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        def _parse_patronymic_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        patronymic_name = _parse_patronymic_name(d.pop("patronymicName", UNSET))

        def _parse_taxpayer_identification_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        taxpayer_identification_number = _parse_taxpayer_identification_number(
            d.pop("taxpayerIdentificationNumber", UNSET)
        )

        phone_number = d.pop("phoneNumber", UNSET)

        def _parse_date_of_birth(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        date_of_birth = _parse_date_of_birth(d.pop("dateOfBirth", UNSET))

        _hired_on = d.pop("hiredOn", UNSET)
        hired_on: Union[Unset, datetime.date]
        if isinstance(_hired_on, Unset):
            hired_on = UNSET
        else:
            hired_on = isoparse(_hired_on).date()

        def _parse_dismissed_on(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dismissed_on_type_0 = isoparse(data).date()

                return dismissed_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        dismissed_on = _parse_dismissed_on(d.pop("dismissedOn", UNSET))

        def _parse_position_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        position_name = _parse_position_name(d.pop("positionName", UNSET))

        def _parse_position_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        position_id = _parse_position_id(d.pop("positionId", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, StaffMatchStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StaffMatchStatus(_status)

        def _parse_dismissal_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        dismissal_reason = _parse_dismissal_reason(d.pop("dismissalReason", UNSET))

        def _parse_dismissal_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        dismissal_comment = _parse_dismissal_comment(d.pop("dismissalComment", UNSET))

        unit_id = d.pop("unitId", UNSET)

        unit_name = d.pop("unitName", UNSET)

        matches_count = d.pop("matchesCount", UNSET)

        _matches = d.pop("matches", UNSET)
        matches: Union[Unset, StaffMatchMatches]
        if isinstance(_matches, Unset):
            matches = UNSET
        else:
            matches = StaffMatchMatches.from_dict(_matches)

        staff_match = cls(
            first_name=first_name,
            last_name=last_name,
            patronymic_name=patronymic_name,
            taxpayer_identification_number=taxpayer_identification_number,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            hired_on=hired_on,
            dismissed_on=dismissed_on,
            position_name=position_name,
            position_id=position_id,
            status=status,
            dismissal_reason=dismissal_reason,
            dismissal_comment=dismissal_comment,
            unit_id=unit_id,
            unit_name=unit_name,
            matches_count=matches_count,
            matches=matches,
        )

        staff_match.additional_properties = d
        return staff_match

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
