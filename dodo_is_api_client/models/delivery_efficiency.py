from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeliveryEfficiency")


@_attrs_define
class DeliveryEfficiency:
    """Эффективность доставки

    Attributes:
        unit_id (str): Идентификатор пиццерии Example: 000d3a240c719a8711e68aba13f7fe13.
        unit_name (str): Название пиццерии в форматах Сыктывкар-1 или Москва 0-1 Example: Сыктывкар-1.
        delivery_sales (float): Выручка с доставки Example: 569784.4.
        delivery_orders_count (int): Количество заказов на доставку Example: 132.
        orders_with_courier_app_count (int): Количество доставок с курьерским приложением Example: 98.
        stop_sales_count (int): Количество стопов Example: 1.
        stop_sales_duration (int): Продолжительность стопов (в секундах) Example: 674.
        late_orders_count (int): Количество опоздавших заказов Example: 12.
        forecast_hit_trips_percentage (float): Поездки попавшие в прогноз (в %) Example: 0.97.
        incorrect_trips_percentage (float): Некорректные поездки (в %)
            https://dodopizza.info/articles/692ec125-18c6-489e-ba30-955177601d4c Example: 0.1.
        trips_with_one_order_count (int): Количество поездок с одним заказом Example: 89.
        trips_with_two_orders_count (int): Количество поездок с двумя заказами Example: 11.
        trips_with_three_orders_count (int): Количество поездок с тремя заказами Example: 5.
        trips_with_four_orders_count (int): Количество поездок с четырьмя заказами Example: 1.
        trips_with_five_or_more_orders_count (int): Количество поездок с 5 или более заказами Example: 1.
    """

    unit_id: str
    unit_name: str
    delivery_sales: float
    delivery_orders_count: int
    orders_with_courier_app_count: int
    stop_sales_count: int
    stop_sales_duration: int
    late_orders_count: int
    forecast_hit_trips_percentage: float
    incorrect_trips_percentage: float
    trips_with_one_order_count: int
    trips_with_two_orders_count: int
    trips_with_three_orders_count: int
    trips_with_four_orders_count: int
    trips_with_five_or_more_orders_count: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        unit_name = self.unit_name

        delivery_sales = self.delivery_sales

        delivery_orders_count = self.delivery_orders_count

        orders_with_courier_app_count = self.orders_with_courier_app_count

        stop_sales_count = self.stop_sales_count

        stop_sales_duration = self.stop_sales_duration

        late_orders_count = self.late_orders_count

        forecast_hit_trips_percentage = self.forecast_hit_trips_percentage

        incorrect_trips_percentage = self.incorrect_trips_percentage

        trips_with_one_order_count = self.trips_with_one_order_count

        trips_with_two_orders_count = self.trips_with_two_orders_count

        trips_with_three_orders_count = self.trips_with_three_orders_count

        trips_with_four_orders_count = self.trips_with_four_orders_count

        trips_with_five_or_more_orders_count = self.trips_with_five_or_more_orders_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitId": unit_id,
                "unitName": unit_name,
                "deliverySales": delivery_sales,
                "deliveryOrdersCount": delivery_orders_count,
                "ordersWithCourierAppCount": orders_with_courier_app_count,
                "stopSalesCount": stop_sales_count,
                "stopSalesDuration": stop_sales_duration,
                "lateOrdersCount": late_orders_count,
                "forecastHitTripsPercentage": forecast_hit_trips_percentage,
                "incorrectTripsPercentage": incorrect_trips_percentage,
                "tripsWithOneOrderCount": trips_with_one_order_count,
                "tripsWithTwoOrdersCount": trips_with_two_orders_count,
                "tripsWithThreeOrdersCount": trips_with_three_orders_count,
                "tripsWithFourOrdersCount": trips_with_four_orders_count,
                "tripsWithFiveOrMoreOrdersCount": trips_with_five_or_more_orders_count,
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

        orders_with_courier_app_count = d.pop("ordersWithCourierAppCount")

        stop_sales_count = d.pop("stopSalesCount")

        stop_sales_duration = d.pop("stopSalesDuration")

        late_orders_count = d.pop("lateOrdersCount")

        forecast_hit_trips_percentage = d.pop("forecastHitTripsPercentage")

        incorrect_trips_percentage = d.pop("incorrectTripsPercentage")

        trips_with_one_order_count = d.pop("tripsWithOneOrderCount")

        trips_with_two_orders_count = d.pop("tripsWithTwoOrdersCount")

        trips_with_three_orders_count = d.pop("tripsWithThreeOrdersCount")

        trips_with_four_orders_count = d.pop("tripsWithFourOrdersCount")

        trips_with_five_or_more_orders_count = d.pop("tripsWithFiveOrMoreOrdersCount")

        delivery_efficiency = cls(
            unit_id=unit_id,
            unit_name=unit_name,
            delivery_sales=delivery_sales,
            delivery_orders_count=delivery_orders_count,
            orders_with_courier_app_count=orders_with_courier_app_count,
            stop_sales_count=stop_sales_count,
            stop_sales_duration=stop_sales_duration,
            late_orders_count=late_orders_count,
            forecast_hit_trips_percentage=forecast_hit_trips_percentage,
            incorrect_trips_percentage=incorrect_trips_percentage,
            trips_with_one_order_count=trips_with_one_order_count,
            trips_with_two_orders_count=trips_with_two_orders_count,
            trips_with_three_orders_count=trips_with_three_orders_count,
            trips_with_four_orders_count=trips_with_four_orders_count,
            trips_with_five_or_more_orders_count=trips_with_five_or_more_orders_count,
        )

        delivery_efficiency.additional_properties = d
        return delivery_efficiency

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
