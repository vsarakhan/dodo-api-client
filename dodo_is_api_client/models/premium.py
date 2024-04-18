import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Premium")


@_attrs_define
class Premium:
    """Единоразовая премия

    Attributes:
        id (str): Идентификатор премии Example: 497d3a398r765a7309e68aft13f7f176.
        unit_id (str): Идентификатор заведения Example: 000d3a240c719a8711e68aba13f7fe13.
        amount (float): Размер премии Example: 3980.82.
        at_local (datetime.datetime): Дата и время назначения в формате ISO 8601 (локальное время) Example:
            2016-01-03T10:20:31.
        comment (str): Комментарий
        at (Union[Unset, datetime.datetime]): Возвращает локальное время вместо UTC Example: 2016-01-03T10:20:31.
    """

    id: str
    unit_id: str
    amount: float
    at_local: datetime.datetime
    comment: str
    at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        unit_id = self.unit_id

        amount = self.amount

        at_local = self.at_local.isoformat()

        comment = self.comment

        at: Union[Unset, str] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "unitId": unit_id,
                "amount": amount,
                "atLocal": at_local,
                "comment": comment,
            }
        )
        if at is not UNSET:
            field_dict["at"] = at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        unit_id = d.pop("unitId")

        amount = d.pop("amount")

        at_local = isoparse(d.pop("atLocal"))

        comment = d.pop("comment")

        _at = d.pop("at", UNSET)
        at: Union[Unset, datetime.datetime]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = isoparse(_at)

        premium = cls(
            id=id,
            unit_id=unit_id,
            amount=amount,
            at_local=at_local,
            comment=comment,
            at=at,
        )

        premium.additional_properties = d
        return premium

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
