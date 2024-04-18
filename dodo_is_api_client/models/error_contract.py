from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_contract_details import ErrorContractDetails


T = TypeVar("T", bound="ErrorContract")


@_attrs_define
class ErrorContract:
    """
    Attributes:
        code (str): Код ошибки Example: NoAccessToUnit.
        http_status (int): Http статус ответа Example: 403.
        request_id (str): Уникальный идентификатор запроса Example: 0HLEACIU86PT6:0000000D.
        message (Union[Unset, str]):  Example: No access to the requested unit.
        details (Union[Unset, ErrorContractDetails]): Детализация ошибки. Может содержать дополнительную информацию об
            ошибке. Формат зависит может отличаться в зависимости от кода ошибки.
    """

    code: str
    http_status: int
    request_id: str
    message: Union[Unset, str] = UNSET
    details: Union[Unset, "ErrorContractDetails"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        http_status = self.http_status

        request_id = self.request_id

        message = self.message

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "httpStatus": http_status,
                "requestId": request_id,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_contract_details import ErrorContractDetails

        d = src_dict.copy()
        code = d.pop("code")

        http_status = d.pop("httpStatus")

        request_id = d.pop("requestId")

        message = d.pop("message", UNSET)

        _details = d.pop("details", UNSET)
        details: Union[Unset, ErrorContractDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = ErrorContractDetails.from_dict(_details)

        error_contract = cls(
            code=code,
            http_status=http_status,
            request_id=request_id,
            message=message,
            details=details,
        )

        error_contract.additional_properties = d
        return error_contract

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
