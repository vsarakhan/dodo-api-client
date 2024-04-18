from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_sales_added_ingredient import ProductSalesAddedIngredient
    from ..models.product_sales_combo import ProductSalesCombo
    from ..models.product_sales_discount import ProductSalesDiscount
    from ..models.product_sales_pizza_half import ProductSalesPizzaHalf


T = TypeVar("T", bound="ProductSalesProduct")


@_attrs_define
class ProductSalesProduct:
    """
    Attributes:
        product_id (str): Идентификатор продукта Example: 000d3a240c719a8711e68aba13f7fe13.
        is_producible (bool): Производимый (false - товар, true - продукт, который производим сами) Default: False.
        default_product_name (str): Название, построенное с учётом признаков продукта Example: Четыре сыра Маленькая.
        price (float): Цена без скидки в формате #.## Example: 469.
        price_with_discount (float): Цена со скидкой в формате #.## Example: 360.
        tax_rate (float): Налоговая ставка в формате #.##
        tax_value (float): Сумма налога в формате #.##
        combo (Union[Unset, ProductSalesCombo]):
        discount (Union[Unset, ProductSalesDiscount]):
        added_ingredients (Union[Unset, List['ProductSalesAddedIngredient']]):
        pizza_halves (Union[Unset, List['ProductSalesPizzaHalf']]):
    """

    product_id: str
    default_product_name: str
    price: float
    price_with_discount: float
    tax_rate: float
    tax_value: float
    is_producible: bool = False
    combo: Union[Unset, "ProductSalesCombo"] = UNSET
    discount: Union[Unset, "ProductSalesDiscount"] = UNSET
    added_ingredients: Union[Unset, List["ProductSalesAddedIngredient"]] = UNSET
    pizza_halves: Union[Unset, List["ProductSalesPizzaHalf"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_id = self.product_id

        is_producible = self.is_producible

        default_product_name = self.default_product_name

        price = self.price

        price_with_discount = self.price_with_discount

        tax_rate = self.tax_rate

        tax_value = self.tax_value

        combo: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.combo, Unset):
            combo = self.combo.to_dict()

        discount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "productId": product_id,
                "isProducible": is_producible,
                "defaultProductName": default_product_name,
                "price": price,
                "priceWithDiscount": price_with_discount,
                "taxRate": tax_rate,
                "taxValue": tax_value,
            }
        )
        if combo is not UNSET:
            field_dict["combo"] = combo
        if discount is not UNSET:
            field_dict["discount"] = discount
        if added_ingredients is not UNSET:
            field_dict["addedIngredients"] = added_ingredients
        if pizza_halves is not UNSET:
            field_dict["pizzaHalves"] = pizza_halves

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_sales_added_ingredient import ProductSalesAddedIngredient
        from ..models.product_sales_combo import ProductSalesCombo
        from ..models.product_sales_discount import ProductSalesDiscount
        from ..models.product_sales_pizza_half import ProductSalesPizzaHalf

        d = src_dict.copy()
        product_id = d.pop("productId")

        is_producible = d.pop("isProducible")

        default_product_name = d.pop("defaultProductName")

        price = d.pop("price")

        price_with_discount = d.pop("priceWithDiscount")

        tax_rate = d.pop("taxRate")

        tax_value = d.pop("taxValue")

        _combo = d.pop("combo", UNSET)
        combo: Union[Unset, ProductSalesCombo]
        if isinstance(_combo, Unset):
            combo = UNSET
        else:
            combo = ProductSalesCombo.from_dict(_combo)

        _discount = d.pop("discount", UNSET)
        discount: Union[Unset, ProductSalesDiscount]
        if isinstance(_discount, Unset):
            discount = UNSET
        else:
            discount = ProductSalesDiscount.from_dict(_discount)

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

        product_sales_product = cls(
            product_id=product_id,
            is_producible=is_producible,
            default_product_name=default_product_name,
            price=price,
            price_with_discount=price_with_discount,
            tax_rate=tax_rate,
            tax_value=tax_value,
            combo=combo,
            discount=discount,
            added_ingredients=added_ingredients,
            pizza_halves=pizza_halves,
        )

        product_sales_product.additional_properties = d
        return product_sales_product

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
