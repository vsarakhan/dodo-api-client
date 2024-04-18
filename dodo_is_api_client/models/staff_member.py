import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.staff_member_business_id import StaffMemberBusinessId
from ..models.staff_member_sex import StaffMemberSex
from ..models.staff_member_staff_type import StaffMemberStaffType
from ..models.staff_member_status import StaffMemberStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="StaffMember")


@_attrs_define
class StaffMember:
    """Сотрудник

    Attributes:
        id (Union[Unset, str]): Уникальный идентификатор сотрудника в формате UUID Example:
            000d3a240c719a8711e68aba13f7fe13.
        user_id (Union[Unset, str]): Уникальный идентификатор учетной записи сотрудника в формате UUID Example:
            000d3a240c719a8711e68aba13f7fe13.
        first_name (Union[Unset, str]): Имя Example: Иван.
        last_name (Union[Unset, str]): Фамилия Example: Иванов.
        patronymic_name (Union[None, Unset, str]): Отчество Example: Иванович.
        sex (Union[Unset, StaffMemberSex]): Пол Example: Male.
        business_id (Union[Unset, StaffMemberBusinessId]): Название бизнеса (концепции), к которому прикреплен сотрудник
            Example: dodopizza.
        country_code (Union[Unset, str]): Код страны, к которой прикреплен сотрудник, в формате ISO 3166-1 alpha-2
            Example: ru.
        status (Union[Unset, StaffMemberStatus]): Статус. `Dismissed` - уволен, `Suspended` - отстранен, `Active` -
            работает Example: Active.
        dismissal_reason (Union[None, Unset, str]): Причина увольнения(причины зафиксированы в системе) Example: Нет
            возможности совмещать работу с учебой.
        dismissal_comment (Union[None, Unset, str]): Комментарий к причине увольнения Example: Студент, уволился на
            время сессии.
        date_of_birth (Union[Unset, datetime.date]): Дата рождения сотрудника в формате ISO 8601 Example: 1991-06-25.
        hired_on (Union[Unset, datetime.date]): Дата трудоустройства в формате ISO 8601 Example: 2022-10-23.
        dismissed_on (Union[None, Unset, datetime.date]): Дата увольнения в формате ISO 8601 Example: 2022-10-29.
        last_modified_at (Union[Unset, datetime.datetime]): Дата и время последнего изменения информации о сотруднике в
            формате ISO 8601 Example: 2022-10-01T20:41:01Z.
        phone_number (Union[Unset, str]): Номер телефона в формате без символов (только цифры) Example: 79001234567.
        email (Union[None, Unset, str]): Адрес электронной почты Example: ivanov@example.com.
        taxpayer_identification_number (Union[None, Unset, str]): Код налогоплательщика (для РФ - ИНН) Example:
            2524366131.
        unit_id (Union[Unset, str]): Уникальный идентификатор заведения, к которому прикреплен сотрудник, в формате UUID
            Example: 000d3a240c719a8711e68aba13f7fe13.
        unit_name (Union[Unset, str]): Название заведения, к которому прикреплен сотрудник Example: Москва 0-1.
        staff_type (Union[Unset, StaffMemberStaffType]): Тип сотрудника. `Operator` - оператор, `KitchenMember` -
            работник кухни, `Courier` - курьер, `Cashier` - кассир, `PersonalManager` - менеджер офиса Example:
            KitchenMember.
        position_id (Union[None, Unset, str]): Уникальный идентификатор должности в формате UUID. Отсутствует у типов
            сотрудника `Operator` и `PersonalManager` Example: 000d3a240c719a8711e68aba13f7fe13.
        position_name (Union[None, Unset, str]): Название должности. Отсутствует у типов сотрудника `Operator` и
            `PersonalManager` Example: Пиццамейкер.
        employment_type_id (Union[Unset, str]): Уникальный идентификатор типа трудоустройства в формате UUID Example:
            000d3a240c719a8711e68aba13f7fe13.
        employment_type_name (Union[Unset, str]): Название типа трудоустройства (ТК/ГПХ/самозанятый) Example:
            Самозанятый.
        is_health_permit_available (Union[Unset, bool]): Признак, показывающий наличие (true) или отсутствие (false) у
            сотрудника медицинской книжки Example: True.
        health_permit_issued_on (Union[None, Unset, datetime.date]): Дата выдачи медицинской книжки в формате ISO 8601
            Example: 2022-10-27.
        health_permit_expires_on (Union[None, Unset, datetime.date]): Дата окончания действия медициского осмотра в
            медицинской книжке в формате ISO 8601 Example: 2023-10-27.
        health_permit_valid_until (Union[None, Unset, datetime.date]): Дата окончания действия медицинской книжки в
            формате ISO 8601 Example: 2025-10-27.
    """

    id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    patronymic_name: Union[None, Unset, str] = UNSET
    sex: Union[Unset, StaffMemberSex] = UNSET
    business_id: Union[Unset, StaffMemberBusinessId] = UNSET
    country_code: Union[Unset, str] = UNSET
    status: Union[Unset, StaffMemberStatus] = UNSET
    dismissal_reason: Union[None, Unset, str] = UNSET
    dismissal_comment: Union[None, Unset, str] = UNSET
    date_of_birth: Union[Unset, datetime.date] = UNSET
    hired_on: Union[Unset, datetime.date] = UNSET
    dismissed_on: Union[None, Unset, datetime.date] = UNSET
    last_modified_at: Union[Unset, datetime.datetime] = UNSET
    phone_number: Union[Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET
    taxpayer_identification_number: Union[None, Unset, str] = UNSET
    unit_id: Union[Unset, str] = UNSET
    unit_name: Union[Unset, str] = UNSET
    staff_type: Union[Unset, StaffMemberStaffType] = UNSET
    position_id: Union[None, Unset, str] = UNSET
    position_name: Union[None, Unset, str] = UNSET
    employment_type_id: Union[Unset, str] = UNSET
    employment_type_name: Union[Unset, str] = UNSET
    is_health_permit_available: Union[Unset, bool] = UNSET
    health_permit_issued_on: Union[None, Unset, datetime.date] = UNSET
    health_permit_expires_on: Union[None, Unset, datetime.date] = UNSET
    health_permit_valid_until: Union[None, Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        user_id = self.user_id

        first_name = self.first_name

        last_name = self.last_name

        patronymic_name: Union[None, Unset, str]
        if isinstance(self.patronymic_name, Unset):
            patronymic_name = UNSET
        else:
            patronymic_name = self.patronymic_name

        sex: Union[Unset, str] = UNSET
        if not isinstance(self.sex, Unset):
            sex = self.sex.value

        business_id: Union[Unset, str] = UNSET
        if not isinstance(self.business_id, Unset):
            business_id = self.business_id.value

        country_code = self.country_code

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

        date_of_birth: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.isoformat()

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

        last_modified_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified_at, Unset):
            last_modified_at = self.last_modified_at.isoformat()

        phone_number = self.phone_number

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        taxpayer_identification_number: Union[None, Unset, str]
        if isinstance(self.taxpayer_identification_number, Unset):
            taxpayer_identification_number = UNSET
        else:
            taxpayer_identification_number = self.taxpayer_identification_number

        unit_id = self.unit_id

        unit_name = self.unit_name

        staff_type: Union[Unset, str] = UNSET
        if not isinstance(self.staff_type, Unset):
            staff_type = self.staff_type.value

        position_id: Union[None, Unset, str]
        if isinstance(self.position_id, Unset):
            position_id = UNSET
        else:
            position_id = self.position_id

        position_name: Union[None, Unset, str]
        if isinstance(self.position_name, Unset):
            position_name = UNSET
        else:
            position_name = self.position_name

        employment_type_id = self.employment_type_id

        employment_type_name = self.employment_type_name

        is_health_permit_available = self.is_health_permit_available

        health_permit_issued_on: Union[None, Unset, str]
        if isinstance(self.health_permit_issued_on, Unset):
            health_permit_issued_on = UNSET
        elif isinstance(self.health_permit_issued_on, datetime.date):
            health_permit_issued_on = self.health_permit_issued_on.isoformat()
        else:
            health_permit_issued_on = self.health_permit_issued_on

        health_permit_expires_on: Union[None, Unset, str]
        if isinstance(self.health_permit_expires_on, Unset):
            health_permit_expires_on = UNSET
        elif isinstance(self.health_permit_expires_on, datetime.date):
            health_permit_expires_on = self.health_permit_expires_on.isoformat()
        else:
            health_permit_expires_on = self.health_permit_expires_on

        health_permit_valid_until: Union[None, Unset, str]
        if isinstance(self.health_permit_valid_until, Unset):
            health_permit_valid_until = UNSET
        elif isinstance(self.health_permit_valid_until, datetime.date):
            health_permit_valid_until = self.health_permit_valid_until.isoformat()
        else:
            health_permit_valid_until = self.health_permit_valid_until

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if patronymic_name is not UNSET:
            field_dict["patronymicName"] = patronymic_name
        if sex is not UNSET:
            field_dict["sex"] = sex
        if business_id is not UNSET:
            field_dict["businessId"] = business_id
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if status is not UNSET:
            field_dict["status"] = status
        if dismissal_reason is not UNSET:
            field_dict["dismissalReason"] = dismissal_reason
        if dismissal_comment is not UNSET:
            field_dict["dismissalComment"] = dismissal_comment
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if hired_on is not UNSET:
            field_dict["hiredOn"] = hired_on
        if dismissed_on is not UNSET:
            field_dict["dismissedOn"] = dismissed_on
        if last_modified_at is not UNSET:
            field_dict["lastModifiedAt"] = last_modified_at
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if email is not UNSET:
            field_dict["email"] = email
        if taxpayer_identification_number is not UNSET:
            field_dict["taxpayerIdentificationNumber"] = taxpayer_identification_number
        if unit_id is not UNSET:
            field_dict["unitId"] = unit_id
        if unit_name is not UNSET:
            field_dict["unitName"] = unit_name
        if staff_type is not UNSET:
            field_dict["staffType"] = staff_type
        if position_id is not UNSET:
            field_dict["positionId"] = position_id
        if position_name is not UNSET:
            field_dict["positionName"] = position_name
        if employment_type_id is not UNSET:
            field_dict["employmentTypeId"] = employment_type_id
        if employment_type_name is not UNSET:
            field_dict["employmentTypeName"] = employment_type_name
        if is_health_permit_available is not UNSET:
            field_dict["isHealthPermitAvailable"] = is_health_permit_available
        if health_permit_issued_on is not UNSET:
            field_dict["healthPermitIssuedOn"] = health_permit_issued_on
        if health_permit_expires_on is not UNSET:
            field_dict["healthPermitExpiresOn"] = health_permit_expires_on
        if health_permit_valid_until is not UNSET:
            field_dict["healthPermitValidUntil"] = health_permit_valid_until

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        user_id = d.pop("userId", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        def _parse_patronymic_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        patronymic_name = _parse_patronymic_name(d.pop("patronymicName", UNSET))

        _sex = d.pop("sex", UNSET)
        sex: Union[Unset, StaffMemberSex]
        if isinstance(_sex, Unset):
            sex = UNSET
        else:
            sex = StaffMemberSex(_sex)

        _business_id = d.pop("businessId", UNSET)
        business_id: Union[Unset, StaffMemberBusinessId]
        if isinstance(_business_id, Unset):
            business_id = UNSET
        else:
            business_id = StaffMemberBusinessId(_business_id)

        country_code = d.pop("countryCode", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, StaffMemberStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StaffMemberStatus(_status)

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

        _date_of_birth = d.pop("dateOfBirth", UNSET)
        date_of_birth: Union[Unset, datetime.date]
        if isinstance(_date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = isoparse(_date_of_birth).date()

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

        _last_modified_at = d.pop("lastModifiedAt", UNSET)
        last_modified_at: Union[Unset, datetime.datetime]
        if isinstance(_last_modified_at, Unset):
            last_modified_at = UNSET
        else:
            last_modified_at = isoparse(_last_modified_at)

        phone_number = d.pop("phoneNumber", UNSET)

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_taxpayer_identification_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        taxpayer_identification_number = _parse_taxpayer_identification_number(
            d.pop("taxpayerIdentificationNumber", UNSET)
        )

        unit_id = d.pop("unitId", UNSET)

        unit_name = d.pop("unitName", UNSET)

        _staff_type = d.pop("staffType", UNSET)
        staff_type: Union[Unset, StaffMemberStaffType]
        if isinstance(_staff_type, Unset):
            staff_type = UNSET
        else:
            staff_type = StaffMemberStaffType(_staff_type)

        def _parse_position_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        position_id = _parse_position_id(d.pop("positionId", UNSET))

        def _parse_position_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        position_name = _parse_position_name(d.pop("positionName", UNSET))

        employment_type_id = d.pop("employmentTypeId", UNSET)

        employment_type_name = d.pop("employmentTypeName", UNSET)

        is_health_permit_available = d.pop("isHealthPermitAvailable", UNSET)

        def _parse_health_permit_issued_on(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                health_permit_issued_on_type_0 = isoparse(data).date()

                return health_permit_issued_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        health_permit_issued_on = _parse_health_permit_issued_on(d.pop("healthPermitIssuedOn", UNSET))

        def _parse_health_permit_expires_on(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                health_permit_expires_on_type_0 = isoparse(data).date()

                return health_permit_expires_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        health_permit_expires_on = _parse_health_permit_expires_on(d.pop("healthPermitExpiresOn", UNSET))

        def _parse_health_permit_valid_until(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                health_permit_valid_until_type_0 = isoparse(data).date()

                return health_permit_valid_until_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        health_permit_valid_until = _parse_health_permit_valid_until(d.pop("healthPermitValidUntil", UNSET))

        staff_member = cls(
            id=id,
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            patronymic_name=patronymic_name,
            sex=sex,
            business_id=business_id,
            country_code=country_code,
            status=status,
            dismissal_reason=dismissal_reason,
            dismissal_comment=dismissal_comment,
            date_of_birth=date_of_birth,
            hired_on=hired_on,
            dismissed_on=dismissed_on,
            last_modified_at=last_modified_at,
            phone_number=phone_number,
            email=email,
            taxpayer_identification_number=taxpayer_identification_number,
            unit_id=unit_id,
            unit_name=unit_name,
            staff_type=staff_type,
            position_id=position_id,
            position_name=position_name,
            employment_type_id=employment_type_id,
            employment_type_name=employment_type_name,
            is_health_permit_available=is_health_permit_available,
            health_permit_issued_on=health_permit_issued_on,
            health_permit_expires_on=health_permit_expires_on,
            health_permit_valid_until=health_permit_valid_until,
        )

        staff_member.additional_properties = d
        return staff_member

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
