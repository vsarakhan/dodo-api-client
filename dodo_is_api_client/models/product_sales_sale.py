import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.product_sales_sale_cash_box_type import ProductSalesSaleCashBoxType
from ..models.product_sales_sale_order_source import ProductSalesSaleOrderSource
from ..models.product_sales_sale_payment_method import ProductSalesSalePaymentMethod
from ..models.product_sales_sale_sales_channel import ProductSalesSaleSalesChannel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_sales_product import ProductSalesProduct


T = TypeVar("T", bound="ProductSalesSale")


@_attrs_define
class ProductSalesSale:
    """
    Attributes:
        unit_id (str): Идентификатор заведения (пиццерии) Example: 000d3a240c719a8711e68aba13f7fe13.
        unit_name (str): Название заведения (пиццерии) Example: Сыктывкар-1.
        order_id (str): Идентификатор заказа Example: 000d3a240c719a8711e68aba13f7fe13.
        sold_at (datetime.datetime): Дата и время продажи в формате ISO 8601 Example: 2022-10-01T20:41:01.
        payment_method (ProductSalesSalePaymentMethod): Метод оплаты Example: Card.
        sales_channel (ProductSalesSaleSalesChannel): Канал продажи Example: Takeaway.
        order_source (ProductSalesSaleOrderSource): Источник заказа Example: CallCenter.
        products (List['ProductSalesProduct']):
        shift_id (Union[Unset, str]):  Example: 000d3a240c719a8711e68aba13f7fe13.
        shift_started_at_local (Union[Unset, datetime.datetime]): Дата и время начала смены в формате ISO 8601
            (локальное время) Example: 2022-10-01T08:00:00.
        shift_ended_at_local (Union[Unset, datetime.datetime]): Дата и время окончания смены в формате ISO 8601
            (локальное время) Example: 2022-10-01T23:00:00.
        cash_box_id (Union[Unset, str]): Номер кассы DodoIS Example: 000d3a240c719a8711e68aba13f7fe13.
        cash_box_session_id (Union[Unset, str]): Номер кассовой сессии Example: 000d3a240c719a8711e68aba13f7fe13.
        cash_box_session_started_at_local (Union[Unset, datetime.datetime]): Дата и время начала смены в формате ISO
            8601 (локальное время) Example: 2022-10-01T09:00:00.
        cash_box_session_ended_at_local (Union[Unset, datetime.datetime]): Дата и время окончания смены в формате ISO
            8601 (локальное время) Example: 2022-10-01T22:00:00.
        payment_provider_name (Union[Unset, str]): Название провайдера, который провёл оплату Example: Sberbank.
        check_number (Union[Unset, int]): Номер чека, который выдаст ККМ, показывает был ли распечатан чек для заказа
            Example: 6024.
        cash_box_type (Union[Unset, ProductSalesSaleCashBoxType]): Вид деятельности кассы Example: Delivery.
        cash_box_number (Union[Unset, float]): Номер кассы Example: 123.
        shift_started_at (Union[Unset, datetime.datetime]): Дата и время начала смены в формате ISO 8601 (Возвращает
            локальное время вместо UTC) Example: 2022-10-01T08:00:00.
        shift_ended_at (Union[Unset, datetime.datetime]): Дата и время окончания смены в формате ISO 8601 (Возвращает
            локальное время вместо UTC) Example: 2022-10-01T23:00:00.
        cash_box_session_started_at (Union[Unset, datetime.datetime]): Дата и время начала смены в формате ISO 8601
            (Возвращает локальное время вместо UTC) Example: 2022-10-01T09:00:00.
        cash_box_session_ended_at (Union[Unset, datetime.datetime]): Дата и время окончания смены в формате ISO 8601
            (Возвращает локальное время вместо UTC) Example: 2022-10-01T22:00:00.
    """

    unit_id: str
    unit_name: str
    order_id: str
    sold_at: datetime.datetime
    payment_method: ProductSalesSalePaymentMethod
    sales_channel: ProductSalesSaleSalesChannel
    order_source: ProductSalesSaleOrderSource
    products: List["ProductSalesProduct"]
    shift_id: Union[Unset, str] = UNSET
    shift_started_at_local: Union[Unset, datetime.datetime] = UNSET
    shift_ended_at_local: Union[Unset, datetime.datetime] = UNSET
    cash_box_id: Union[Unset, str] = UNSET
    cash_box_session_id: Union[Unset, str] = UNSET
    cash_box_session_started_at_local: Union[Unset, datetime.datetime] = UNSET
    cash_box_session_ended_at_local: Union[Unset, datetime.datetime] = UNSET
    payment_provider_name: Union[Unset, str] = UNSET
    check_number: Union[Unset, int] = UNSET
    cash_box_type: Union[Unset, ProductSalesSaleCashBoxType] = UNSET
    cash_box_number: Union[Unset, float] = UNSET
    shift_started_at: Union[Unset, datetime.datetime] = UNSET
    shift_ended_at: Union[Unset, datetime.datetime] = UNSET
    cash_box_session_started_at: Union[Unset, datetime.datetime] = UNSET
    cash_box_session_ended_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        unit_name = self.unit_name

        order_id = self.order_id

        sold_at = self.sold_at.isoformat()

        payment_method = self.payment_method.value

        sales_channel = self.sales_channel.value

        order_source = self.order_source.value

        products = []
        for products_item_data in self.products:
            products_item = products_item_data.to_dict()
            products.append(products_item)

        shift_id = self.shift_id

        shift_started_at_local: Union[Unset, str] = UNSET
        if not isinstance(self.shift_started_at_local, Unset):
            shift_started_at_local = self.shift_started_at_local.isoformat()

        shift_ended_at_local: Union[Unset, str] = UNSET
        if not isinstance(self.shift_ended_at_local, Unset):
            shift_ended_at_local = self.shift_ended_at_local.isoformat()

        cash_box_id = self.cash_box_id

        cash_box_session_id = self.cash_box_session_id

        cash_box_session_started_at_local: Union[Unset, str] = UNSET
        if not isinstance(self.cash_box_session_started_at_local, Unset):
            cash_box_session_started_at_local = self.cash_box_session_started_at_local.isoformat()

        cash_box_session_ended_at_local: Union[Unset, str] = UNSET
        if not isinstance(self.cash_box_session_ended_at_local, Unset):
            cash_box_session_ended_at_local = self.cash_box_session_ended_at_local.isoformat()

        payment_provider_name = self.payment_provider_name

        check_number = self.check_number

        cash_box_type: Union[Unset, str] = UNSET
        if not isinstance(self.cash_box_type, Unset):
            cash_box_type = self.cash_box_type.value

        cash_box_number = self.cash_box_number

        shift_started_at: Union[Unset, str] = UNSET
        if not isinstance(self.shift_started_at, Unset):
            shift_started_at = self.shift_started_at.isoformat()

        shift_ended_at: Union[Unset, str] = UNSET
        if not isinstance(self.shift_ended_at, Unset):
            shift_ended_at = self.shift_ended_at.isoformat()

        cash_box_session_started_at: Union[Unset, str] = UNSET
        if not isinstance(self.cash_box_session_started_at, Unset):
            cash_box_session_started_at = self.cash_box_session_started_at.isoformat()

        cash_box_session_ended_at: Union[Unset, str] = UNSET
        if not isinstance(self.cash_box_session_ended_at, Unset):
            cash_box_session_ended_at = self.cash_box_session_ended_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitId": unit_id,
                "unitName": unit_name,
                "orderId": order_id,
                "soldAt": sold_at,
                "paymentMethod": payment_method,
                "salesChannel": sales_channel,
                "orderSource": order_source,
                "products": products,
            }
        )
        if shift_id is not UNSET:
            field_dict["shiftId"] = shift_id
        if shift_started_at_local is not UNSET:
            field_dict["shiftStartedAtLocal"] = shift_started_at_local
        if shift_ended_at_local is not UNSET:
            field_dict["shiftEndedAtLocal"] = shift_ended_at_local
        if cash_box_id is not UNSET:
            field_dict["cashBoxId"] = cash_box_id
        if cash_box_session_id is not UNSET:
            field_dict["cashBoxSessionId"] = cash_box_session_id
        if cash_box_session_started_at_local is not UNSET:
            field_dict["cashBoxSessionStartedAtLocal"] = cash_box_session_started_at_local
        if cash_box_session_ended_at_local is not UNSET:
            field_dict["cashBoxSessionEndedAtLocal"] = cash_box_session_ended_at_local
        if payment_provider_name is not UNSET:
            field_dict["paymentProviderName"] = payment_provider_name
        if check_number is not UNSET:
            field_dict["checkNumber"] = check_number
        if cash_box_type is not UNSET:
            field_dict["cashBoxType"] = cash_box_type
        if cash_box_number is not UNSET:
            field_dict["cashBoxNumber"] = cash_box_number
        if shift_started_at is not UNSET:
            field_dict["shiftStartedAt"] = shift_started_at
        if shift_ended_at is not UNSET:
            field_dict["shiftEndedAt"] = shift_ended_at
        if cash_box_session_started_at is not UNSET:
            field_dict["cashBoxSessionStartedAt"] = cash_box_session_started_at
        if cash_box_session_ended_at is not UNSET:
            field_dict["cashBoxSessionEndedAt"] = cash_box_session_ended_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_sales_product import ProductSalesProduct

        d = src_dict.copy()
        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        order_id = d.pop("orderId")

        sold_at = isoparse(d.pop("soldAt"))

        payment_method = ProductSalesSalePaymentMethod(d.pop("paymentMethod"))

        sales_channel = ProductSalesSaleSalesChannel(d.pop("salesChannel"))

        order_source = ProductSalesSaleOrderSource(d.pop("orderSource"))

        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = ProductSalesProduct.from_dict(products_item_data)

            products.append(products_item)

        shift_id = d.pop("shiftId", UNSET)

        _shift_started_at_local = d.pop("shiftStartedAtLocal", UNSET)
        shift_started_at_local: Union[Unset, datetime.datetime]
        if isinstance(_shift_started_at_local, Unset):
            shift_started_at_local = UNSET
        else:
            shift_started_at_local = isoparse(_shift_started_at_local)

        _shift_ended_at_local = d.pop("shiftEndedAtLocal", UNSET)
        shift_ended_at_local: Union[Unset, datetime.datetime]
        if isinstance(_shift_ended_at_local, Unset):
            shift_ended_at_local = UNSET
        else:
            shift_ended_at_local = isoparse(_shift_ended_at_local)

        cash_box_id = d.pop("cashBoxId", UNSET)

        cash_box_session_id = d.pop("cashBoxSessionId", UNSET)

        _cash_box_session_started_at_local = d.pop("cashBoxSessionStartedAtLocal", UNSET)
        cash_box_session_started_at_local: Union[Unset, datetime.datetime]
        if isinstance(_cash_box_session_started_at_local, Unset):
            cash_box_session_started_at_local = UNSET
        else:
            cash_box_session_started_at_local = isoparse(_cash_box_session_started_at_local)

        _cash_box_session_ended_at_local = d.pop("cashBoxSessionEndedAtLocal", UNSET)
        cash_box_session_ended_at_local: Union[Unset, datetime.datetime]
        if isinstance(_cash_box_session_ended_at_local, Unset):
            cash_box_session_ended_at_local = UNSET
        else:
            cash_box_session_ended_at_local = isoparse(_cash_box_session_ended_at_local)

        payment_provider_name = d.pop("paymentProviderName", UNSET)

        check_number = d.pop("checkNumber", UNSET)

        _cash_box_type = d.pop("cashBoxType", UNSET)
        cash_box_type: Union[Unset, ProductSalesSaleCashBoxType]
        if isinstance(_cash_box_type, Unset):
            cash_box_type = UNSET
        else:
            cash_box_type = ProductSalesSaleCashBoxType(_cash_box_type)

        cash_box_number = d.pop("cashBoxNumber", UNSET)

        _shift_started_at = d.pop("shiftStartedAt", UNSET)
        shift_started_at: Union[Unset, datetime.datetime]
        if isinstance(_shift_started_at, Unset):
            shift_started_at = UNSET
        else:
            shift_started_at = isoparse(_shift_started_at)

        _shift_ended_at = d.pop("shiftEndedAt", UNSET)
        shift_ended_at: Union[Unset, datetime.datetime]
        if isinstance(_shift_ended_at, Unset):
            shift_ended_at = UNSET
        else:
            shift_ended_at = isoparse(_shift_ended_at)

        _cash_box_session_started_at = d.pop("cashBoxSessionStartedAt", UNSET)
        cash_box_session_started_at: Union[Unset, datetime.datetime]
        if isinstance(_cash_box_session_started_at, Unset):
            cash_box_session_started_at = UNSET
        else:
            cash_box_session_started_at = isoparse(_cash_box_session_started_at)

        _cash_box_session_ended_at = d.pop("cashBoxSessionEndedAt", UNSET)
        cash_box_session_ended_at: Union[Unset, datetime.datetime]
        if isinstance(_cash_box_session_ended_at, Unset):
            cash_box_session_ended_at = UNSET
        else:
            cash_box_session_ended_at = isoparse(_cash_box_session_ended_at)

        product_sales_sale = cls(
            unit_id=unit_id,
            unit_name=unit_name,
            order_id=order_id,
            sold_at=sold_at,
            payment_method=payment_method,
            sales_channel=sales_channel,
            order_source=order_source,
            products=products,
            shift_id=shift_id,
            shift_started_at_local=shift_started_at_local,
            shift_ended_at_local=shift_ended_at_local,
            cash_box_id=cash_box_id,
            cash_box_session_id=cash_box_session_id,
            cash_box_session_started_at_local=cash_box_session_started_at_local,
            cash_box_session_ended_at_local=cash_box_session_ended_at_local,
            payment_provider_name=payment_provider_name,
            check_number=check_number,
            cash_box_type=cash_box_type,
            cash_box_number=cash_box_number,
            shift_started_at=shift_started_at,
            shift_ended_at=shift_ended_at,
            cash_box_session_started_at=cash_box_session_started_at,
            cash_box_session_ended_at=cash_box_session_ended_at,
        )

        product_sales_sale.additional_properties = d
        return product_sales_sale

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
