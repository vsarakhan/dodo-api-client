from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProductSalesAddedIngredient")


@_attrs_define
class ProductSalesAddedIngredient:
    """
    Attributes:
        id (str): Идентификатор добавленного ингредиента Example: 000d3a240c719a8711e68aba13f7fe13.
        name (str): Название добавленного ингредиента Example: Халапеньо консерв..
        price (float): Цена добавленного ингредиента в формате #.## Example: 79.
    """

    id: str
    name: str
    price: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        price = self.price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "price": price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        price = d.pop("price")

        product_sales_added_ingredient = cls(
            id=id,
            name=name,
            price=price,
        )

        product_sales_added_ingredient.additional_properties = d
        return product_sales_added_ingredient

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
