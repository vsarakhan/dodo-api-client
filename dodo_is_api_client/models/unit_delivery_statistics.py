from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UnitDeliveryStatistics")


@_attrs_define
class UnitDeliveryStatistics:
    """Основные метрики доставки

    Attributes:
        unit_id (str): Идентификатор пиццерии Example: 000d3a240c719a8711e68aba13f7fe13.
        unit_name (str): Название пиццерии в форматах Сыктывкар-1 или Москва 0-1 Example: Сыктывкар-1.
        delivery_sales (float): Выручка с доставки
        delivery_orders_count (int): Количество заказов на доставку Example: 130.
        avg_delivery_order_fulfillment_time (int): Среднее время доставки (от оформления заказа до вручения клиенту) в
            секундах
        avg_cooking_time (int): Среднее время приготовления в секундах
        avg_heated_shelf_time (int): Среднее время ожидания на тепловой полке в секундах
        avg_order_trip_time (int): Среднее время курьера с заказом в пути в секундах
        late_orders_count (int): Количество опоздавших заказов
        trips_count (int): Количество поездок курьеров Example: 154.
        trips_duration (int): Сумма времени всех поездок курьеров в секундах Example: 7920.
        couriers_shifts_duration (int): Сумма продолжительности смены всех курьеров в секундах Example: 828757.
        orders_with_courier_app_count (int): Количество доставок с курьерским приложением Example: 93.
    """

    unit_id: str
    unit_name: str
    delivery_sales: float
    delivery_orders_count: int
    avg_delivery_order_fulfillment_time: int
    avg_cooking_time: int
    avg_heated_shelf_time: int
    avg_order_trip_time: int
    late_orders_count: int
    trips_count: int
    trips_duration: int
    couriers_shifts_duration: int
    orders_with_courier_app_count: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        unit_name = self.unit_name

        delivery_sales = self.delivery_sales

        delivery_orders_count = self.delivery_orders_count

        avg_delivery_order_fulfillment_time = self.avg_delivery_order_fulfillment_time

        avg_cooking_time = self.avg_cooking_time

        avg_heated_shelf_time = self.avg_heated_shelf_time

        avg_order_trip_time = self.avg_order_trip_time

        late_orders_count = self.late_orders_count

        trips_count = self.trips_count

        trips_duration = self.trips_duration

        couriers_shifts_duration = self.couriers_shifts_duration

        orders_with_courier_app_count = self.orders_with_courier_app_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitId": unit_id,
                "unitName": unit_name,
                "deliverySales": delivery_sales,
                "deliveryOrdersCount": delivery_orders_count,
                "avgDeliveryOrderFulfillmentTime": avg_delivery_order_fulfillment_time,
                "avgCookingTime": avg_cooking_time,
                "avgHeatedShelfTime": avg_heated_shelf_time,
                "avgOrderTripTime": avg_order_trip_time,
                "lateOrdersCount": late_orders_count,
                "tripsCount": trips_count,
                "tripsDuration": trips_duration,
                "couriersShiftsDuration": couriers_shifts_duration,
                "ordersWithCourierAppCount": orders_with_courier_app_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        delivery_sales = d.pop("deliverySales")

        delivery_orders_count = d.pop("deliveryOrdersCount")

        avg_delivery_order_fulfillment_time = d.pop("avgDeliveryOrderFulfillmentTime")

        avg_cooking_time = d.pop("avgCookingTime")

        avg_heated_shelf_time = d.pop("avgHeatedShelfTime")

        avg_order_trip_time = d.pop("avgOrderTripTime")

        late_orders_count = d.pop("lateOrdersCount")

        trips_count = d.pop("tripsCount")

        trips_duration = d.pop("tripsDuration")

        couriers_shifts_duration = d.pop("couriersShiftsDuration")

        orders_with_courier_app_count = d.pop("ordersWithCourierAppCount")

        unit_delivery_statistics = cls(
            unit_id=unit_id,
            unit_name=unit_name,
            delivery_sales=delivery_sales,
            delivery_orders_count=delivery_orders_count,
            avg_delivery_order_fulfillment_time=avg_delivery_order_fulfillment_time,
            avg_cooking_time=avg_cooking_time,
            avg_heated_shelf_time=avg_heated_shelf_time,
            avg_order_trip_time=avg_order_trip_time,
            late_orders_count=late_orders_count,
            trips_count=trips_count,
            trips_duration=trips_duration,
            couriers_shifts_duration=couriers_shifts_duration,
            orders_with_courier_app_count=orders_with_courier_app_count,
        )

        unit_delivery_statistics.additional_properties = d
        return unit_delivery_statistics

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
