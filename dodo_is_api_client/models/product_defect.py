import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_sales_added_ingredient import ProductSalesAddedIngredient
    from ..models.product_sales_pizza_half import ProductSalesPizzaHalf


T = TypeVar("T", bound="ProductDefect")


@_attrs_define
class ProductDefect:
    """Брак продукта

    Attributes:
        unit_id (str): Идентификатор заведения Example: 000d3a240c719a8711e68aba13f7f862.
        unit_name (str): Название заведения Example: Сыктывкар-1.
        product_id (str): Идентификатор продукта Example: 000d3a240c719a8711e68aba13f7f862.
        product_name (str): Наименование продукта Example: Пепперони Большая.
        sold_at_local (datetime.datetime): Дата и время продажи в формате ISO 8601 (локальное время) Example:
            2011-08-01T18:31:42.
        price_with_discount (float): Цена со скидкой в формате #.## Example: 360.
        added_ingredients (Union[Unset, List['ProductSalesAddedIngredient']]):
        pizza_halves (Union[Unset, List['ProductSalesPizzaHalf']]):
        sold_at (Union[Unset, datetime.datetime]): Дата и время продажи в формате ISO 8601 (Возвращает локальное время
            вместо UTC) Example: 2011-08-01T18:31:42.
    """

    unit_id: str
    unit_name: str
    product_id: str
    product_name: str
    sold_at_local: datetime.datetime
    price_with_discount: float
    added_ingredients: Union[Unset, List["ProductSalesAddedIngredient"]] = UNSET
    pizza_halves: Union[Unset, List["ProductSalesPizzaHalf"]] = UNSET
    sold_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        unit_name = self.unit_name

        product_id = self.product_id

        product_name = self.product_name

        sold_at_local = self.sold_at_local.isoformat()

        price_with_discount = self.price_with_discount

        added_ingredients: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.added_ingredients, Unset):
            added_ingredients = []
            for added_ingredients_item_data in self.added_ingredients:
                added_ingredients_item = added_ingredients_item_data.to_dict()
                added_ingredients.append(added_ingredients_item)

        pizza_halves: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pizza_halves, Unset):
            pizza_halves = []
            for pizza_halves_item_data in self.pizza_halves:
                pizza_halves_item = pizza_halves_item_data.to_dict()
                pizza_halves.append(pizza_halves_item)

        sold_at: Union[Unset, str] = UNSET
        if not isinstance(self.sold_at, Unset):
            sold_at = self.sold_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitId": unit_id,
                "unitName": unit_name,
                "productId": product_id,
                "productName": product_name,
                "soldAtLocal": sold_at_local,
                "priceWithDiscount": price_with_discount,
            }
        )
        if added_ingredients is not UNSET:
            field_dict["addedIngredients"] = added_ingredients
        if pizza_halves is not UNSET:
            field_dict["pizzaHalves"] = pizza_halves
        if sold_at is not UNSET:
            field_dict["soldAt"] = sold_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_sales_added_ingredient import ProductSalesAddedIngredient
        from ..models.product_sales_pizza_half import ProductSalesPizzaHalf

        d = src_dict.copy()
        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        product_id = d.pop("productId")

        product_name = d.pop("productName")

        sold_at_local = isoparse(d.pop("soldAtLocal"))

        price_with_discount = d.pop("priceWithDiscount")

        added_ingredients = []
        _added_ingredients = d.pop("addedIngredients", UNSET)
        for added_ingredients_item_data in _added_ingredients or []:
            added_ingredients_item = ProductSalesAddedIngredient.from_dict(added_ingredients_item_data)

            added_ingredients.append(added_ingredients_item)

        pizza_halves = []
        _pizza_halves = d.pop("pizzaHalves", UNSET)
        for pizza_halves_item_data in _pizza_halves or []:
            pizza_halves_item = ProductSalesPizzaHalf.from_dict(pizza_halves_item_data)

            pizza_halves.append(pizza_halves_item)

        _sold_at = d.pop("soldAt", UNSET)
        sold_at: Union[Unset, datetime.datetime]
        if isinstance(_sold_at, Unset):
            sold_at = UNSET
        else:
            sold_at = isoparse(_sold_at)

        product_defect = cls(
            unit_id=unit_id,
            unit_name=unit_name,
            product_id=product_id,
            product_name=product_name,
            sold_at_local=sold_at_local,
            price_with_discount=price_with_discount,
            added_ingredients=added_ingredients,
            pizza_halves=pizza_halves,
            sold_at=sold_at,
        )

        product_defect.additional_properties = d
        return product_defect

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
