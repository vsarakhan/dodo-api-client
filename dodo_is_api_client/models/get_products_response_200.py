from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product import Product


T = TypeVar("T", bound="GetProductsResponse200")


@_attrs_define
class GetProductsResponse200:
    """
    Attributes:
        taken_count (int): Получено записей
        total_count (int): Всего записей
        is_end_of_list_reached (bool): Индикатор того, что достигнут конец списка. Выдаёт true, если достигнут конец
            списка.
        products (Union[Unset, List['Product']]):
    """

    taken_count: int
    total_count: int
    is_end_of_list_reached: bool
    products: Union[Unset, List["Product"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        taken_count = self.taken_count

        total_count = self.total_count

        is_end_of_list_reached = self.is_end_of_list_reached

        products: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "takenCount": taken_count,
                "totalCount": total_count,
                "isEndOfListReached": is_end_of_list_reached,
            }
        )
        if products is not UNSET:
            field_dict["products"] = products

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product import Product

        d = src_dict.copy()
        taken_count = d.pop("takenCount")

        total_count = d.pop("totalCount")

        is_end_of_list_reached = d.pop("isEndOfListReached")

        products = []
        _products = d.pop("products", UNSET)
        for products_item_data in _products or []:
            products_item = Product.from_dict(products_item_data)

            products.append(products_item)

        get_products_response_200 = cls(
            taken_count=taken_count,
            total_count=total_count,
            is_end_of_list_reached=is_end_of_list_reached,
            products=products,
        )

        get_products_response_200.additional_properties = d
        return get_products_response_200

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
