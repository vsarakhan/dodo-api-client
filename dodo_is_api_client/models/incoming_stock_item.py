import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.measurement_unit import MeasurementUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncomingStockItem")


@_attrs_define
class IncomingStockItem:
    """
    Attributes:
        unit_id (str): Идентификатор заведения Example: 000d3a240c719a8711e68aba13f7f862.
        unit_name (str): Название заведения Example: Сыктывкар-1.
        supplied_at_local (datetime.datetime): Дата и время поставки (локальное время) Example: 2011-08-01T18:31:42.
        supplier_id (str): Идентификатор поставщика Example: 000d3a240c719a8711e68aba13f7f862.
        invoice_date (datetime.date): Дата накладной Example: 2011-08-01.
        invoice_number (str): Номер накладной Example: 1-005.
        commercial_invoice_number (str): Номер счет фактуры Example: 1-005.
        stock_item_id (str): Идентификатор сырья Example: 000d3a240c719a8711e68aba13f7fe13.
        stock_item_name (str): Название сырья Example: Помидоры.
        quantity (float): Полученное количество в формате #.### Example: 30.521.
        measurement_unit (MeasurementUnit): Наименование единицы измерения Example: Quantity.
        total_price_without_vat (float): Цена без налога в формате #.## Example: 123.57.
        total_price_with_vat (float): Цена с НДС в формате #.## Example: 123.57.
        price_per_measurement_unit_with_vat (float): Цена за единицу измерения с учетом НДС в формате #.## Example:
            123.57.
        vat_rate (float): Ставка налога в % Example: 20.
        vat_value (float): Размер налога Example: 150.25.
        incoming_stock_order_id (str): Идентификатор заявки Example: 000d3a240c719a8711e68aba13f7f862.
        supplied_at (Union[Unset, datetime.datetime]): Дата и время поставки (Возвращает локальное время вместо UTC)
            Example: 2011-08-01T18:31:42.
    """

    unit_id: str
    unit_name: str
    supplied_at_local: datetime.datetime
    supplier_id: str
    invoice_date: datetime.date
    invoice_number: str
    commercial_invoice_number: str
    stock_item_id: str
    stock_item_name: str
    quantity: float
    measurement_unit: MeasurementUnit
    total_price_without_vat: float
    total_price_with_vat: float
    price_per_measurement_unit_with_vat: float
    vat_rate: float
    vat_value: float
    incoming_stock_order_id: str
    supplied_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        unit_name = self.unit_name

        supplied_at_local = self.supplied_at_local.isoformat()

        supplier_id = self.supplier_id

        invoice_date = self.invoice_date.isoformat()

        invoice_number = self.invoice_number

        commercial_invoice_number = self.commercial_invoice_number

        stock_item_id = self.stock_item_id

        stock_item_name = self.stock_item_name

        quantity = self.quantity

        measurement_unit = self.measurement_unit.value

        total_price_without_vat = self.total_price_without_vat

        total_price_with_vat = self.total_price_with_vat

        price_per_measurement_unit_with_vat = self.price_per_measurement_unit_with_vat

        vat_rate = self.vat_rate

        vat_value = self.vat_value

        incoming_stock_order_id = self.incoming_stock_order_id

        supplied_at: Union[Unset, str] = UNSET
        if not isinstance(self.supplied_at, Unset):
            supplied_at = self.supplied_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitId": unit_id,
                "unitName": unit_name,
                "suppliedAtLocal": supplied_at_local,
                "supplierId": supplier_id,
                "invoiceDate": invoice_date,
                "invoiceNumber": invoice_number,
                "commercialInvoiceNumber": commercial_invoice_number,
                "stockItemId": stock_item_id,
                "stockItemName": stock_item_name,
                "quantity": quantity,
                "measurementUnit": measurement_unit,
                "totalPriceWithoutVat": total_price_without_vat,
                "totalPriceWithVat": total_price_with_vat,
                "pricePerMeasurementUnitWithVat": price_per_measurement_unit_with_vat,
                "vatRate": vat_rate,
                "vatValue": vat_value,
                "incomingStockOrderId": incoming_stock_order_id,
            }
        )
        if supplied_at is not UNSET:
            field_dict["suppliedAt"] = supplied_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        supplied_at_local = isoparse(d.pop("suppliedAtLocal"))

        supplier_id = d.pop("supplierId")

        invoice_date = isoparse(d.pop("invoiceDate")).date()

        invoice_number = d.pop("invoiceNumber")

        commercial_invoice_number = d.pop("commercialInvoiceNumber")

        stock_item_id = d.pop("stockItemId")

        stock_item_name = d.pop("stockItemName")

        quantity = d.pop("quantity")

        measurement_unit = MeasurementUnit(d.pop("measurementUnit"))

        total_price_without_vat = d.pop("totalPriceWithoutVat")

        total_price_with_vat = d.pop("totalPriceWithVat")

        price_per_measurement_unit_with_vat = d.pop("pricePerMeasurementUnitWithVat")

        vat_rate = d.pop("vatRate")

        vat_value = d.pop("vatValue")

        incoming_stock_order_id = d.pop("incomingStockOrderId")

        _supplied_at = d.pop("suppliedAt", UNSET)
        supplied_at: Union[Unset, datetime.datetime]
        if isinstance(_supplied_at, Unset):
            supplied_at = UNSET
        else:
            supplied_at = isoparse(_supplied_at)

        incoming_stock_item = cls(
            unit_id=unit_id,
            unit_name=unit_name,
            supplied_at_local=supplied_at_local,
            supplier_id=supplier_id,
            invoice_date=invoice_date,
            invoice_number=invoice_number,
            commercial_invoice_number=commercial_invoice_number,
            stock_item_id=stock_item_id,
            stock_item_name=stock_item_name,
            quantity=quantity,
            measurement_unit=measurement_unit,
            total_price_without_vat=total_price_without_vat,
            total_price_with_vat=total_price_with_vat,
            price_per_measurement_unit_with_vat=price_per_measurement_unit_with_vat,
            vat_rate=vat_rate,
            vat_value=vat_value,
            incoming_stock_order_id=incoming_stock_order_id,
            supplied_at=supplied_at,
        )

        incoming_stock_item.additional_properties = d
        return incoming_stock_item

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
