import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StaffMeal")


@_attrs_define
class StaffMeal:
    """Питание персонала

    Attributes:
        unit_id (str): Идентификатор заведения Example: 000d3a240c719a8711e68aba13f7f862.
        unit_name (str): Название заведения Example: Сыктывкар-1.
        staff_id (str): Идентификатор сотрудника Example: 000d3a240c719a8711e68aba13f7f862.
        order_accepted_at_local (datetime.datetime): Дата и время принятия заказа в формате ISO 8601 (локальное время)
            Example: 2011-08-01T18:31:42.
        product_id (str): Идентификатор продукта Example: 000d3a240c719a8711e68aba13f7f862.
        product_name (str): Наименование продукта Example: Пепперони Большая.
        price (float): Цена без скидки в формате #.## Example: 123.57.
        order_accepted_at (Union[Unset, datetime.datetime]): Дата и время принятия заказа в формате ISO 8601 (Возвращает
            локальное время вместо UTC) Example: 2011-08-01T18:31:42.
    """

    unit_id: str
    unit_name: str
    staff_id: str
    order_accepted_at_local: datetime.datetime
    product_id: str
    product_name: str
    price: float
    order_accepted_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        unit_name = self.unit_name

        staff_id = self.staff_id

        order_accepted_at_local = self.order_accepted_at_local.isoformat()

        product_id = self.product_id

        product_name = self.product_name

        price = self.price

        order_accepted_at: Union[Unset, str] = UNSET
        if not isinstance(self.order_accepted_at, Unset):
            order_accepted_at = self.order_accepted_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitId": unit_id,
                "unitName": unit_name,
                "staffId": staff_id,
                "orderAcceptedAtLocal": order_accepted_at_local,
                "productId": product_id,
                "productName": product_name,
                "price": price,
            }
        )
        if order_accepted_at is not UNSET:
            field_dict["orderAcceptedAt"] = order_accepted_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        staff_id = d.pop("staffId")

        order_accepted_at_local = isoparse(d.pop("orderAcceptedAtLocal"))

        product_id = d.pop("productId")

        product_name = d.pop("productName")

        price = d.pop("price")

        _order_accepted_at = d.pop("orderAcceptedAt", UNSET)
        order_accepted_at: Union[Unset, datetime.datetime]
        if isinstance(_order_accepted_at, Unset):
            order_accepted_at = UNSET
        else:
            order_accepted_at = isoparse(_order_accepted_at)

        staff_meal = cls(
            unit_id=unit_id,
            unit_name=unit_name,
            staff_id=staff_id,
            order_accepted_at_local=order_accepted_at_local,
            product_id=product_id,
            product_name=product_name,
            price=price,
            order_accepted_at=order_accepted_at,
        )

        staff_meal.additional_properties = d
        return staff_meal

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
