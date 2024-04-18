import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.couriers_orders_item_delivery_transport_name import CouriersOrdersItemDeliveryTransportName
from ..types import UNSET, Unset

T = TypeVar("T", bound="CouriersOrdersItem")


@_attrs_define
class CouriersOrdersItem:
    """
    Attributes:
        order_id (str): идентификатор заказа
        order_number (str): Номер конкретного заказа. Первая цифра показыает порядковый номер заказа, вторая цифра
            показывает количество выпекаемых позиций в заказе. Example: 1-3.
        courier_staff_id (str): Идентификатор сотрудника-курьера Example: 000d3a240c719a8711e68aba13f7fe13.
        trip_id (str): уникальный идентификатор поездки (за одну поездку может доставляться несколько заказов) Example:
            000d3a240c719a8711e68aba13f7fe13.
        unit_id (str): Идентификатор заведения Example: 000d3a240c719a8711e68aba13f7fe13.
        unit_name (str): Название заведения Example: Сыктывкар-1.
        staff_shift_id (str): Идентификатор смены сотрудника Example: 000d3a240c719a8711e68aba13f7f862.
        handed_over_to_delivery_at (datetime.datetime): Время, когда заказ отмечен отправленным в доставку.
            Касса доставки: отправление происходит при отправке с кассы доставки.
            Курьерское приложение: при нажатии кнопки «Поехали» Example: 2011-08-01T18:31:42.
        predicted_delivery_time (int): Прогнозное время Яндекса или Google, за которое должен быть доставлен заказ + 4
            минуты на действия на адресе заказа: доехать, припарковаться, подняться к клиенту, передать заказ и так далее.
            Мы выбрали время 4 минуты на основе сравнения факта и прогноза поезди по всей сети.
            В секундах с округлением.
        delivery_time (int): Фактическое время, за которое был доставлен заказ
            В секундах с округлением.
        order_fulfilment_flag_at (Union[None, datetime.datetime]): Время отметки курьером в приложении успешной
            доставки.
            Возвращает null для заказов через КД Example: 2011-08-01T18:31:42.
        is_false_delivery (bool): Была ли доставка заказа некорректной.
            Причины некорректных заказов:

            Неверная отметка геолокации: если курьер отметился у клиента в радиусе более, чем 300 метров.

            Не реальное время поездки курьера:

            Заказ выдан через мобильное приложение: если время, когда курьер доставил заказ меньше трети прогноза, то заказ
            будет некорректным.
            Заказ выдан через кассу доставки: берется время из поездки, а не заказа:
            не было определено прогнозного времени — поездка короче 6 минут считается читом.
            есть прогнозное время поездки и реальная поездка меньше чем прогнозное время деленное пополам.
        delivery_transport_name (CouriersOrdersItemDeliveryTransportName): Вид транспорта курьера. Устанавливается во
            время отправки заказа через приложение или кассу доставки: авто, пеший, велосипед. Example: OnFoot.
        trip_orders_count (int): Количество заказов, которые взял курьер в одну поездку
        heated_shelf_time (int): Время ожидания заказа на тепловой полке в секундах с округлением
        order_assembly_avg_time (int): Время сборки заказа, в котором участвует курьер. В секундах с округлением.
            Возможны два случая:

            1. Курьер встал в очередь, и заказ появился после этого. Тогда для расчета метрики берется время которое заказ
            пролежал на полке. Так как курьер все это время мог собирать заказ.

            2. Курьер встал в очередь после того, как появился заказ. Тогда для расчета метрики берется время с момента
            постановки в курьера в очередь, до момента, когда заказ отправлен в поездку.
        is_problematic_delivery (bool): Были проблемы с доставкой
        problematic_delivery_reason (str): Причина проблемной доставки
        was_late_delivery_voucher_given (bool): Был выдан сертификат за опоздание
        sector_id (Union[None, str]): идентификатор сектора Example: 000d3a240c719a8711e68aba13f7fe13.
        sector_name (Union[None, str]): Название сектора Example: Ленинский-1.
        order_fulfilment_flag_at_local (Union[None, Unset, datetime.datetime]): Вовзращает UTC вместо локального времени
            Example: 2011-08-01T18:31:42.
        handed_over_to_delivery_at_local (Union[Unset, datetime.datetime]): Возвращает UTC вместо локального времени
            Example: 2011-08-01T18:31:42.
    """

    order_id: str
    order_number: str
    courier_staff_id: str
    trip_id: str
    unit_id: str
    unit_name: str
    staff_shift_id: str
    handed_over_to_delivery_at: datetime.datetime
    predicted_delivery_time: int
    delivery_time: int
    order_fulfilment_flag_at: Union[None, datetime.datetime]
    is_false_delivery: bool
    delivery_transport_name: CouriersOrdersItemDeliveryTransportName
    trip_orders_count: int
    heated_shelf_time: int
    order_assembly_avg_time: int
    is_problematic_delivery: bool
    problematic_delivery_reason: str
    was_late_delivery_voucher_given: bool
    sector_id: Union[None, str]
    sector_name: Union[None, str]
    order_fulfilment_flag_at_local: Union[None, Unset, datetime.datetime] = UNSET
    handed_over_to_delivery_at_local: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_id = self.order_id

        order_number = self.order_number

        courier_staff_id = self.courier_staff_id

        trip_id = self.trip_id

        unit_id = self.unit_id

        unit_name = self.unit_name

        staff_shift_id = self.staff_shift_id

        handed_over_to_delivery_at = self.handed_over_to_delivery_at.isoformat()

        predicted_delivery_time = self.predicted_delivery_time

        delivery_time = self.delivery_time

        order_fulfilment_flag_at: Union[None, str]
        if isinstance(self.order_fulfilment_flag_at, datetime.datetime):
            order_fulfilment_flag_at = self.order_fulfilment_flag_at.isoformat()
        else:
            order_fulfilment_flag_at = self.order_fulfilment_flag_at

        is_false_delivery = self.is_false_delivery

        delivery_transport_name = self.delivery_transport_name.value

        trip_orders_count = self.trip_orders_count

        heated_shelf_time = self.heated_shelf_time

        order_assembly_avg_time = self.order_assembly_avg_time

        is_problematic_delivery = self.is_problematic_delivery

        problematic_delivery_reason = self.problematic_delivery_reason

        was_late_delivery_voucher_given = self.was_late_delivery_voucher_given

        sector_id: Union[None, str]
        sector_id = self.sector_id

        sector_name: Union[None, str]
        sector_name = self.sector_name

        order_fulfilment_flag_at_local: Union[None, Unset, str]
        if isinstance(self.order_fulfilment_flag_at_local, Unset):
            order_fulfilment_flag_at_local = UNSET
        elif isinstance(self.order_fulfilment_flag_at_local, datetime.datetime):
            order_fulfilment_flag_at_local = self.order_fulfilment_flag_at_local.isoformat()
        else:
            order_fulfilment_flag_at_local = self.order_fulfilment_flag_at_local

        handed_over_to_delivery_at_local: Union[Unset, str] = UNSET
        if not isinstance(self.handed_over_to_delivery_at_local, Unset):
            handed_over_to_delivery_at_local = self.handed_over_to_delivery_at_local.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orderId": order_id,
                "orderNumber": order_number,
                "courierStaffId": courier_staff_id,
                "tripId": trip_id,
                "unitId": unit_id,
                "unitName": unit_name,
                "staffShiftId": staff_shift_id,
                "handedOverToDeliveryAt": handed_over_to_delivery_at,
                "predictedDeliveryTime": predicted_delivery_time,
                "deliveryTime": delivery_time,
                "orderFulfilmentFlagAt": order_fulfilment_flag_at,
                "isFalseDelivery": is_false_delivery,
                "deliveryTransportName": delivery_transport_name,
                "tripOrdersCount": trip_orders_count,
                "heatedShelfTime": heated_shelf_time,
                "orderAssemblyAvgTime": order_assembly_avg_time,
                "isProblematicDelivery": is_problematic_delivery,
                "problematicDeliveryReason": problematic_delivery_reason,
                "wasLateDeliveryVoucherGiven": was_late_delivery_voucher_given,
                "sectorId": sector_id,
                "sectorName": sector_name,
            }
        )
        if order_fulfilment_flag_at_local is not UNSET:
            field_dict["orderFulfilmentFlagAtLocal"] = order_fulfilment_flag_at_local
        if handed_over_to_delivery_at_local is not UNSET:
            field_dict["handedOverToDeliveryAtLocal"] = handed_over_to_delivery_at_local

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_id = d.pop("orderId")

        order_number = d.pop("orderNumber")

        courier_staff_id = d.pop("courierStaffId")

        trip_id = d.pop("tripId")

        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        staff_shift_id = d.pop("staffShiftId")

        handed_over_to_delivery_at = isoparse(d.pop("handedOverToDeliveryAt"))

        predicted_delivery_time = d.pop("predictedDeliveryTime")

        delivery_time = d.pop("deliveryTime")

        def _parse_order_fulfilment_flag_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_fulfilment_flag_at_type_0 = isoparse(data)

                return order_fulfilment_flag_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        order_fulfilment_flag_at = _parse_order_fulfilment_flag_at(d.pop("orderFulfilmentFlagAt"))

        is_false_delivery = d.pop("isFalseDelivery")

        delivery_transport_name = CouriersOrdersItemDeliveryTransportName(d.pop("deliveryTransportName"))

        trip_orders_count = d.pop("tripOrdersCount")

        heated_shelf_time = d.pop("heatedShelfTime")

        order_assembly_avg_time = d.pop("orderAssemblyAvgTime")

        is_problematic_delivery = d.pop("isProblematicDelivery")

        problematic_delivery_reason = d.pop("problematicDeliveryReason")

        was_late_delivery_voucher_given = d.pop("wasLateDeliveryVoucherGiven")

        def _parse_sector_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        sector_id = _parse_sector_id(d.pop("sectorId"))

        def _parse_sector_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        sector_name = _parse_sector_name(d.pop("sectorName"))

        def _parse_order_fulfilment_flag_at_local(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_fulfilment_flag_at_local_type_0 = isoparse(data)

                return order_fulfilment_flag_at_local_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        order_fulfilment_flag_at_local = _parse_order_fulfilment_flag_at_local(
            d.pop("orderFulfilmentFlagAtLocal", UNSET)
        )

        _handed_over_to_delivery_at_local = d.pop("handedOverToDeliveryAtLocal", UNSET)
        handed_over_to_delivery_at_local: Union[Unset, datetime.datetime]
        if isinstance(_handed_over_to_delivery_at_local, Unset):
            handed_over_to_delivery_at_local = UNSET
        else:
            handed_over_to_delivery_at_local = isoparse(_handed_over_to_delivery_at_local)

        couriers_orders_item = cls(
            order_id=order_id,
            order_number=order_number,
            courier_staff_id=courier_staff_id,
            trip_id=trip_id,
            unit_id=unit_id,
            unit_name=unit_name,
            staff_shift_id=staff_shift_id,
            handed_over_to_delivery_at=handed_over_to_delivery_at,
            predicted_delivery_time=predicted_delivery_time,
            delivery_time=delivery_time,
            order_fulfilment_flag_at=order_fulfilment_flag_at,
            is_false_delivery=is_false_delivery,
            delivery_transport_name=delivery_transport_name,
            trip_orders_count=trip_orders_count,
            heated_shelf_time=heated_shelf_time,
            order_assembly_avg_time=order_assembly_avg_time,
            is_problematic_delivery=is_problematic_delivery,
            problematic_delivery_reason=problematic_delivery_reason,
            was_late_delivery_voucher_given=was_late_delivery_voucher_given,
            sector_id=sector_id,
            sector_name=sector_name,
            order_fulfilment_flag_at_local=order_fulfilment_flag_at_local,
            handed_over_to_delivery_at_local=handed_over_to_delivery_at_local,
        )

        couriers_orders_item.additional_properties = d
        return couriers_orders_item

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
