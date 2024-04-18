from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.product_defect import ProductDefect


T = TypeVar("T", bound="GetDefectiveProductsResponse200")


@_attrs_define
class GetDefectiveProductsResponse200:
    """
    Attributes:
        defects (List['ProductDefect']):
        is_end_of_list_reached (bool): Индикатор того, что достигнут конец списка. Выдаёт true, если достигнут конец
            списка.
    """

    defects: List["ProductDefect"]
    is_end_of_list_reached: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        defects = []
        for defects_item_data in self.defects:
            defects_item = defects_item_data.to_dict()
            defects.append(defects_item)

        is_end_of_list_reached = self.is_end_of_list_reached

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "defects": defects,
                "isEndOfListReached": is_end_of_list_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_defect import ProductDefect

        d = src_dict.copy()
        defects = []
        _defects = d.pop("defects")
        for defects_item_data in _defects:
            defects_item = ProductDefect.from_dict(defects_item_data)

            defects.append(defects_item)

        is_end_of_list_reached = d.pop("isEndOfListReached")

        get_defective_products_response_200 = cls(
            defects=defects,
            is_end_of_list_reached=is_end_of_list_reached,
        )

        get_defective_products_response_200.additional_properties = d
        return get_defective_products_response_200

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
