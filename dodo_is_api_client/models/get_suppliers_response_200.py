from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.supplier import Supplier


T = TypeVar("T", bound="GetSuppliersResponse200")


@_attrs_define
class GetSuppliersResponse200:
    """
    Attributes:
        suppliers (List['Supplier']):
        is_end_of_list_reached (bool): Индикатор того, что достигнут конец списка. Выдаёт true, если достигнут конец
            списка.
    """

    suppliers: List["Supplier"]
    is_end_of_list_reached: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        suppliers = []
        for suppliers_item_data in self.suppliers:
            suppliers_item = suppliers_item_data.to_dict()
            suppliers.append(suppliers_item)

        is_end_of_list_reached = self.is_end_of_list_reached

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "suppliers": suppliers,
                "isEndOfListReached": is_end_of_list_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.supplier import Supplier

        d = src_dict.copy()
        suppliers = []
        _suppliers = d.pop("suppliers")
        for suppliers_item_data in _suppliers:
            suppliers_item = Supplier.from_dict(suppliers_item_data)

            suppliers.append(suppliers_item)

        is_end_of_list_reached = d.pop("isEndOfListReached")

        get_suppliers_response_200 = cls(
            suppliers=suppliers,
            is_end_of_list_reached=is_end_of_list_reached,
        )

        get_suppliers_response_200.additional_properties = d
        return get_suppliers_response_200

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
