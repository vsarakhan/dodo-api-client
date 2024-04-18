from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetSuppliersResponse400")


@_attrs_define
class GetSuppliersResponse400:
    """
    Attributes:
        field (str): Поле, с которым связана ошибка
        message (str): Описание ошибки
    """

    field: str
    message: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field = self.field

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field = d.pop("field")

        message = d.pop("message")

        get_suppliers_response_400 = cls(
            field=field,
            message=message,
        )

        get_suppliers_response_400.additional_properties = d
        return get_suppliers_response_400

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
