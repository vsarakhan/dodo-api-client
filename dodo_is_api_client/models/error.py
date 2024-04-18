from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_payload import ErrorPayload


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """Ошибка

    Attributes:
        message (Union[Unset, str]): Сообщение об ошибке
        payload (Union[Unset, ErrorPayload]): Дополнительная информация об ошибке
    """

    message: Union[Unset, str] = UNSET
    payload: Union[Unset, "ErrorPayload"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message

        payload: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_payload import ErrorPayload

        d = src_dict.copy()
        message = d.pop("message", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, ErrorPayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = ErrorPayload.from_dict(_payload)

        error = cls(
            message=message,
            payload=payload,
        )

        error.additional_properties = d
        return error

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
