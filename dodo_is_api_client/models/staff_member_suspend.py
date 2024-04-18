import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StaffMemberSuspend")


@_attrs_define
class StaffMemberSuspend:
    """Информация об отстранении

    Attributes:
        suspended_from (datetime.datetime): Дата и время начала отстранения. Не может быть датой в прошлом. Example:
            2023-04-20T13:35:20.000Z.
        reason_id (str): Причина отстранения
        suspended_to (Union[Unset, datetime.datetime]): Дата и время окончания отстранения. Должна быть больше, чем дата
            начала отстранения. Example: 2023-04-25T13:35:20.000Z.
        comment (Union[Unset, str]): Комменатрий к отстранению. Не больше, чем 255 символов.
    """

    suspended_from: datetime.datetime
    reason_id: str
    suspended_to: Union[Unset, datetime.datetime] = UNSET
    comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        suspended_from = self.suspended_from.isoformat()

        reason_id = self.reason_id

        suspended_to: Union[Unset, str] = UNSET
        if not isinstance(self.suspended_to, Unset):
            suspended_to = self.suspended_to.isoformat()

        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "suspendedFrom": suspended_from,
                "reasonId": reason_id,
            }
        )
        if suspended_to is not UNSET:
            field_dict["suspendedTo"] = suspended_to
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        suspended_from = isoparse(d.pop("suspendedFrom"))

        reason_id = d.pop("reasonId")

        _suspended_to = d.pop("suspendedTo", UNSET)
        suspended_to: Union[Unset, datetime.datetime]
        if isinstance(_suspended_to, Unset):
            suspended_to = UNSET
        else:
            suspended_to = isoparse(_suspended_to)

        comment = d.pop("comment", UNSET)

        staff_member_suspend = cls(
            suspended_from=suspended_from,
            reason_id=reason_id,
            suspended_to=suspended_to,
            comment=comment,
        )

        staff_member_suspend.additional_properties = d
        return staff_member_suspend

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
