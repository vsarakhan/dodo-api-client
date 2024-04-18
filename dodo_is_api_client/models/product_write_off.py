import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.product_write_off_reason import ProductWriteOffReason
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_stock_item_write_off import ProductStockItemWriteOff


T = TypeVar("T", bound="ProductWriteOff")


@_attrs_define
class ProductWriteOff:
    """Списание продукта

    Причины списаний:
    <code>
    Expired: 100 (Вышел срок годности)
    Defected: 200 (Порчи продукта)
    DamagedPackaging: 300 (Повреждение упаковки)
    HumanElement: 400 (Человеческий фактор)
    Marketing: 500 (Маркетинговые мероприятия)
    ExpiredShowcaseTime: 600 (Списания по времени с витрины)
    ShowcaseWriteOff: 700 (Списания кусочков)
    </code>

        Attributes:
            unit_id (str): Идентификатор заведения Example: 000d3a240c719a8711e68aba13f7f862.
            unit_name (str): Название заведения Example: Сыктывкар-1.
            written_off_at_local (datetime.datetime): Дата и время списания (локальное время) Example: 2011-08-01T18:31:42.
            reason (ProductWriteOffReason): Причина списания Example: Marketing.
            product_id (str): Идентификатор продукта Example: 000d3a240c719a8711e68aba13f7f862.
            product_name (str): Наименование продукта Example: Пепперони Большая.
            quantity (float): Списанное количество Example: 5.3.
            stock_items (List['ProductStockItemWriteOff']):
            price_per_piece (Union[Unset, float]): Цена без скидки за 1 шт. в формате #.## Example: 123.57.
            written_off_at (Union[Unset, datetime.datetime]): Дата и время списания (Возвращает локальное время вместо UTC)
                Example: 2011-08-01T18:31:42.
    """

    unit_id: str
    unit_name: str
    written_off_at_local: datetime.datetime
    reason: ProductWriteOffReason
    product_id: str
    product_name: str
    quantity: float
    stock_items: List["ProductStockItemWriteOff"]
    price_per_piece: Union[Unset, float] = UNSET
    written_off_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        unit_name = self.unit_name

        written_off_at_local = self.written_off_at_local.isoformat()

        reason = self.reason.value

        product_id = self.product_id

        product_name = self.product_name

        quantity = self.quantity

        stock_items = []
        for stock_items_item_data in self.stock_items:
            stock_items_item = stock_items_item_data.to_dict()
            stock_items.append(stock_items_item)

        price_per_piece = self.price_per_piece

        written_off_at: Union[Unset, str] = UNSET
        if not isinstance(self.written_off_at, Unset):
            written_off_at = self.written_off_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitId": unit_id,
                "unitName": unit_name,
                "writtenOffAtLocal": written_off_at_local,
                "reason": reason,
                "productId": product_id,
                "productName": product_name,
                "quantity": quantity,
                "stockItems": stock_items,
            }
        )
        if price_per_piece is not UNSET:
            field_dict["pricePerPiece"] = price_per_piece
        if written_off_at is not UNSET:
            field_dict["writtenOffAt"] = written_off_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_stock_item_write_off import ProductStockItemWriteOff

        d = src_dict.copy()
        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        written_off_at_local = isoparse(d.pop("writtenOffAtLocal"))

        reason = ProductWriteOffReason(d.pop("reason"))

        product_id = d.pop("productId")

        product_name = d.pop("productName")

        quantity = d.pop("quantity")

        stock_items = []
        _stock_items = d.pop("stockItems")
        for stock_items_item_data in _stock_items:
            stock_items_item = ProductStockItemWriteOff.from_dict(stock_items_item_data)

            stock_items.append(stock_items_item)

        price_per_piece = d.pop("pricePerPiece", UNSET)

        _written_off_at = d.pop("writtenOffAt", UNSET)
        written_off_at: Union[Unset, datetime.datetime]
        if isinstance(_written_off_at, Unset):
            written_off_at = UNSET
        else:
            written_off_at = isoparse(_written_off_at)

        product_write_off = cls(
            unit_id=unit_id,
            unit_name=unit_name,
            written_off_at_local=written_off_at_local,
            reason=reason,
            product_id=product_id,
            product_name=product_name,
            quantity=quantity,
            stock_items=stock_items,
            price_per_piece=price_per_piece,
            written_off_at=written_off_at,
        )

        product_write_off.additional_properties = d
        return product_write_off

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
