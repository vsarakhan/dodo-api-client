from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProductSalesDiscount")


@_attrs_define
class ProductSalesDiscount:
    """
    Attributes:
        bonus_action_id (str): Идентификатор бонусной акции Example: 000d3a240c719a8711e68aba13f7fe13.
        bonus_action_name (str): Название бонусной акции Example: CVM. Скидка 30% при заказе от 999 ₽ пуш (отток).
        promo_code (str): Промокод Example: P18KVKG530.
    """

    bonus_action_id: str
    bonus_action_name: str
    promo_code: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bonus_action_id = self.bonus_action_id

        bonus_action_name = self.bonus_action_name

        promo_code = self.promo_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bonusActionId": bonus_action_id,
                "bonusActionName": bonus_action_name,
                "promoCode": promo_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bonus_action_id = d.pop("bonusActionId")

        bonus_action_name = d.pop("bonusActionName")

        promo_code = d.pop("promoCode")

        product_sales_discount = cls(
            bonus_action_id=bonus_action_id,
            bonus_action_name=bonus_action_name,
            promo_code=promo_code,
        )

        product_sales_discount.additional_properties = d
        return product_sales_discount

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
