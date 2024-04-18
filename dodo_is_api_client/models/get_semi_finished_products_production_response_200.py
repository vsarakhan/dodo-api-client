from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.semifinished_product_production import SemifinishedProductProduction


T = TypeVar("T", bound="GetSemiFinishedProductsProductionResponse200")


@_attrs_define
class GetSemiFinishedProductsProductionResponse200:
    """
    Attributes:
        productions (List['SemifinishedProductProduction']):
        is_end_of_list_reached (bool): Индикатор того, что достигнут конец списка. Выдаёт true, если достигнут конец
            списка.
    """

    productions: List["SemifinishedProductProduction"]
    is_end_of_list_reached: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        productions = []
        for productions_item_data in self.productions:
            productions_item = productions_item_data.to_dict()
            productions.append(productions_item)

        is_end_of_list_reached = self.is_end_of_list_reached

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "productions": productions,
                "isEndOfListReached": is_end_of_list_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.semifinished_product_production import SemifinishedProductProduction

        d = src_dict.copy()
        productions = []
        _productions = d.pop("productions")
        for productions_item_data in _productions:
            productions_item = SemifinishedProductProduction.from_dict(productions_item_data)

            productions.append(productions_item)

        is_end_of_list_reached = d.pop("isEndOfListReached")

        get_semi_finished_products_production_response_200 = cls(
            productions=productions,
            is_end_of_list_reached=is_end_of_list_reached,
        )

        get_semi_finished_products_production_response_200.additional_properties = d
        return get_semi_finished_products_production_response_200

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
