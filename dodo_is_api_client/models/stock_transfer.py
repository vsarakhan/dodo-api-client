import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.measurement_unit import MeasurementUnit
from ..models.stock_transfer_status import StockTransferStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="StockTransfer")


@_attrs_define
class StockTransfer:
    """Перемещение сырья

    Статусы перемещений:
    <code>
    Created: 1 (Новая заявка на перемещение)
    Ordered:2 (Заказанная заявка на перемещение)
    Shipped: 3 (Отгруженная заявка на перемещение)
    Received: 4 (Полученная заявка на перемещение)
    Cancelled: 5 (Отмененная заявка на перемещение)
    </code>

    Значения единиц измерения продуктов:
    <code>
    Quantity: 1
    Kilogram: 4
    Liter: 6
    Meter: 8
    </code>

        Attributes:
            transfer_order_number (str): Номер заявки Example: П-17/23.
            transfer_order_id (str): Идентификатор заявки Example: 000d3a240c719a8711e68aba13f7f862.
            origin_unit_id (str): Идентификатор заведения отгрузки Example: 000d3a240c719a8711e68aba13f7f862.
            origin_unit_name (str): Название заведения отгрузки Example: Сыктывкар-1.
            origin_legal_entity_id (str): Идентификатор юрлица отгрузки Example: 000d3a240c719a8711e68aba13f7f862.
            origin_legal_entity_name (str): Название юрлица отгрузки Example: Dodo.
            destination_unit_id (str): Идентификатор заведения получателя Example: 000d3a240c719a8711e68aba13f7f862.
            destination_unit_name (str): Название заведения получателя Example: Сыктывкар-2.
            destination_legal_entity_id (str): Идентификатор юрлица получателя Example: 000d3a240c719a8711e68aba13f7f862.
            destination_legal_entity_name (str): Название юрлица получателя Example: Dodo.
            status (StockTransferStatus): Статус перемещения Example: Shipped.
            created_at_local (datetime.datetime): Дата создания (локальное время) Example: 2011-08-01T18:31:42.
            expected_at_local (datetime.datetime): Ожидаемая дата получения (локальное время) Example: 2011-08-01T18:31:42.
            stock_item_id (str): Идентификатор отгруженного сырья Example: 000d3a240c719a8711e68aba13f7f862.
            stock_item_name (str): Наименование отгруженного сырья Example: Бекон.
            ordered_quantity (float): Заказанное количество Example: 0.352.
            measurement_unit (MeasurementUnit): Наименование единицы измерения Example: Quantity.
            price_per_unit_with_vat (float): Цена за единицу измерения с НДС Example: 120.
            price_per_unit_without_vat (float): Цена за единицу измерения без НДС Example: 100.
            sum_price_with_vat (float): Сумма с НДС Example: 42.24.
            sum_price_without_vat (float): Сумма без НДС Example: 35.1.
            tax_rate (float): Ставка НДС Example: 20.
            vat_value (float): Сумма НДС Example: 7.14.
            shipped_at_local (Union[Unset, datetime.datetime]): Дата отгрузки (локальное время) Example:
                2011-08-01T18:31:42.
            received_at_local (Union[Unset, datetime.datetime]): Дата получения (локальное время) Example:
                2011-08-01T18:31:42.
            shipped_quantity (Union[Unset, float]): Отгруженное количество Example: 0.352.
            received_quantity (Union[Unset, float]): Полученное количество Example: 0.352.
            created_at (Union[Unset, datetime.datetime]): Дата создания (Возвращает локальное время вместо UTC) Example:
                2011-08-01T18:31:42.
            expected_at (Union[Unset, datetime.datetime]): Ожидаемая дата получения (Возвращает локальное время вместо UTC)
                Example: 2011-08-01T18:31:42.
            shipped_at (Union[Unset, datetime.datetime]): Дата отгрузки (Возвращает локальное время вместо UTC) Example:
                2011-08-01T18:31:42.
            received_at (Union[Unset, datetime.datetime]): Дата получения (Возвращает локальное время вместо UTC) Example:
                2011-08-01T18:31:42.
    """

    transfer_order_number: str
    transfer_order_id: str
    origin_unit_id: str
    origin_unit_name: str
    origin_legal_entity_id: str
    origin_legal_entity_name: str
    destination_unit_id: str
    destination_unit_name: str
    destination_legal_entity_id: str
    destination_legal_entity_name: str
    status: StockTransferStatus
    created_at_local: datetime.datetime
    expected_at_local: datetime.datetime
    stock_item_id: str
    stock_item_name: str
    ordered_quantity: float
    measurement_unit: MeasurementUnit
    price_per_unit_with_vat: float
    price_per_unit_without_vat: float
    sum_price_with_vat: float
    sum_price_without_vat: float
    tax_rate: float
    vat_value: float
    shipped_at_local: Union[Unset, datetime.datetime] = UNSET
    received_at_local: Union[Unset, datetime.datetime] = UNSET
    shipped_quantity: Union[Unset, float] = UNSET
    received_quantity: Union[Unset, float] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    expected_at: Union[Unset, datetime.datetime] = UNSET
    shipped_at: Union[Unset, datetime.datetime] = UNSET
    received_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transfer_order_number = self.transfer_order_number

        transfer_order_id = self.transfer_order_id

        origin_unit_id = self.origin_unit_id

        origin_unit_name = self.origin_unit_name

        origin_legal_entity_id = self.origin_legal_entity_id

        origin_legal_entity_name = self.origin_legal_entity_name

        destination_unit_id = self.destination_unit_id

        destination_unit_name = self.destination_unit_name

        destination_legal_entity_id = self.destination_legal_entity_id

        destination_legal_entity_name = self.destination_legal_entity_name

        status = self.status.value

        created_at_local = self.created_at_local.isoformat()

        expected_at_local = self.expected_at_local.isoformat()

        stock_item_id = self.stock_item_id

        stock_item_name = self.stock_item_name

        ordered_quantity = self.ordered_quantity

        measurement_unit = self.measurement_unit.value

        price_per_unit_with_vat = self.price_per_unit_with_vat

        price_per_unit_without_vat = self.price_per_unit_without_vat

        sum_price_with_vat = self.sum_price_with_vat

        sum_price_without_vat = self.sum_price_without_vat

        tax_rate = self.tax_rate

        vat_value = self.vat_value

        shipped_at_local: Union[Unset, str] = UNSET
        if not isinstance(self.shipped_at_local, Unset):
            shipped_at_local = self.shipped_at_local.isoformat()

        received_at_local: Union[Unset, str] = UNSET
        if not isinstance(self.received_at_local, Unset):
            received_at_local = self.received_at_local.isoformat()

        shipped_quantity = self.shipped_quantity

        received_quantity = self.received_quantity

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        expected_at: Union[Unset, str] = UNSET
        if not isinstance(self.expected_at, Unset):
            expected_at = self.expected_at.isoformat()

        shipped_at: Union[Unset, str] = UNSET
        if not isinstance(self.shipped_at, Unset):
            shipped_at = self.shipped_at.isoformat()

        received_at: Union[Unset, str] = UNSET
        if not isinstance(self.received_at, Unset):
            received_at = self.received_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transferOrderNumber": transfer_order_number,
                "transferOrderId": transfer_order_id,
                "originUnitId": origin_unit_id,
                "originUnitName": origin_unit_name,
                "originLegalEntityId": origin_legal_entity_id,
                "originLegalEntityName": origin_legal_entity_name,
                "destinationUnitId": destination_unit_id,
                "destinationUnitName": destination_unit_name,
                "destinationLegalEntityId": destination_legal_entity_id,
                "destinationLegalEntityName": destination_legal_entity_name,
                "status": status,
                "createdAtLocal": created_at_local,
                "expectedAtLocal": expected_at_local,
                "stockItemId": stock_item_id,
                "stockItemName": stock_item_name,
                "orderedQuantity": ordered_quantity,
                "measurementUnit": measurement_unit,
                "pricePerUnitWithVat": price_per_unit_with_vat,
                "pricePerUnitWithoutVat": price_per_unit_without_vat,
                "sumPriceWithVat": sum_price_with_vat,
                "sumPriceWithoutVat": sum_price_without_vat,
                "taxRate": tax_rate,
                "vatValue": vat_value,
            }
        )
        if shipped_at_local is not UNSET:
            field_dict["shippedAtLocal"] = shipped_at_local
        if received_at_local is not UNSET:
            field_dict["receivedAtLocal"] = received_at_local
        if shipped_quantity is not UNSET:
            field_dict["shippedQuantity"] = shipped_quantity
        if received_quantity is not UNSET:
            field_dict["receivedQuantity"] = received_quantity
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if expected_at is not UNSET:
            field_dict["expectedAt"] = expected_at
        if shipped_at is not UNSET:
            field_dict["shippedAt"] = shipped_at
        if received_at is not UNSET:
            field_dict["receivedAt"] = received_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        transfer_order_number = d.pop("transferOrderNumber")

        transfer_order_id = d.pop("transferOrderId")

        origin_unit_id = d.pop("originUnitId")

        origin_unit_name = d.pop("originUnitName")

        origin_legal_entity_id = d.pop("originLegalEntityId")

        origin_legal_entity_name = d.pop("originLegalEntityName")

        destination_unit_id = d.pop("destinationUnitId")

        destination_unit_name = d.pop("destinationUnitName")

        destination_legal_entity_id = d.pop("destinationLegalEntityId")

        destination_legal_entity_name = d.pop("destinationLegalEntityName")

        status = StockTransferStatus(d.pop("status"))

        created_at_local = isoparse(d.pop("createdAtLocal"))

        expected_at_local = isoparse(d.pop("expectedAtLocal"))

        stock_item_id = d.pop("stockItemId")

        stock_item_name = d.pop("stockItemName")

        ordered_quantity = d.pop("orderedQuantity")

        measurement_unit = MeasurementUnit(d.pop("measurementUnit"))

        price_per_unit_with_vat = d.pop("pricePerUnitWithVat")

        price_per_unit_without_vat = d.pop("pricePerUnitWithoutVat")

        sum_price_with_vat = d.pop("sumPriceWithVat")

        sum_price_without_vat = d.pop("sumPriceWithoutVat")

        tax_rate = d.pop("taxRate")

        vat_value = d.pop("vatValue")

        _shipped_at_local = d.pop("shippedAtLocal", UNSET)
        shipped_at_local: Union[Unset, datetime.datetime]
        if isinstance(_shipped_at_local, Unset):
            shipped_at_local = UNSET
        else:
            shipped_at_local = isoparse(_shipped_at_local)

        _received_at_local = d.pop("receivedAtLocal", UNSET)
        received_at_local: Union[Unset, datetime.datetime]
        if isinstance(_received_at_local, Unset):
            received_at_local = UNSET
        else:
            received_at_local = isoparse(_received_at_local)

        shipped_quantity = d.pop("shippedQuantity", UNSET)

        received_quantity = d.pop("receivedQuantity", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _expected_at = d.pop("expectedAt", UNSET)
        expected_at: Union[Unset, datetime.datetime]
        if isinstance(_expected_at, Unset):
            expected_at = UNSET
        else:
            expected_at = isoparse(_expected_at)

        _shipped_at = d.pop("shippedAt", UNSET)
        shipped_at: Union[Unset, datetime.datetime]
        if isinstance(_shipped_at, Unset):
            shipped_at = UNSET
        else:
            shipped_at = isoparse(_shipped_at)

        _received_at = d.pop("receivedAt", UNSET)
        received_at: Union[Unset, datetime.datetime]
        if isinstance(_received_at, Unset):
            received_at = UNSET
        else:
            received_at = isoparse(_received_at)

        stock_transfer = cls(
            transfer_order_number=transfer_order_number,
            transfer_order_id=transfer_order_id,
            origin_unit_id=origin_unit_id,
            origin_unit_name=origin_unit_name,
            origin_legal_entity_id=origin_legal_entity_id,
            origin_legal_entity_name=origin_legal_entity_name,
            destination_unit_id=destination_unit_id,
            destination_unit_name=destination_unit_name,
            destination_legal_entity_id=destination_legal_entity_id,
            destination_legal_entity_name=destination_legal_entity_name,
            status=status,
            created_at_local=created_at_local,
            expected_at_local=expected_at_local,
            stock_item_id=stock_item_id,
            stock_item_name=stock_item_name,
            ordered_quantity=ordered_quantity,
            measurement_unit=measurement_unit,
            price_per_unit_with_vat=price_per_unit_with_vat,
            price_per_unit_without_vat=price_per_unit_without_vat,
            sum_price_with_vat=sum_price_with_vat,
            sum_price_without_vat=sum_price_without_vat,
            tax_rate=tax_rate,
            vat_value=vat_value,
            shipped_at_local=shipped_at_local,
            received_at_local=received_at_local,
            shipped_quantity=shipped_quantity,
            received_quantity=received_quantity,
            created_at=created_at,
            expected_at=expected_at,
            shipped_at=shipped_at,
            received_at=received_at,
        )

        stock_transfer.additional_properties = d
        return stock_transfer

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
