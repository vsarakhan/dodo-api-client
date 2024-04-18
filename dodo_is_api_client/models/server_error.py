from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerError")


@_attrs_define
class ServerError:
    """
    Attributes:
        code (Union[None, str]): Код ошибки
        message (Union[None, str]):
        request_id (str): идентификатор запроса
    """

    code: Union[None, str]
    message: Union[None, str]
    request_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code: Union[None, str]
        code = self.code

        message: Union[None, str]
        message = self.message

        request_id = self.request_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
                "requestId": request_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_code(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        code = _parse_code(d.pop("code"))

        def _parse_message(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        message = _parse_message(d.pop("message"))

        request_id = d.pop("requestId")

        server_error = cls(
            code=code,
            message=message,
            request_id=request_id,
        )

        server_error.additional_properties = d
        return server_error

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
