from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StaffScheduleForecastForecastByHourItem")


@_attrs_define
class StaffScheduleForecastForecastByHourItem:
    """
    Attributes:
        forecast_for_hour_local (int): час
        forecast_revenue (float): Прогнозная выручка за час в рублях Example: 1567.73.
        forecast_products_count (float): Прогнозное количество приготавливаемых продуктов за час Example: 30.2.
        forecast_courier_orders_count (float): Прогнозное количество заказов на доставку за час Example: 15.7.
        recommended_unit_labor_minutes (int): Рекомендованно рабочих минут сотрудников заведения. Число кратно 15-ти.
            Example: 1800.
        recommended_courier_labor_minutes (int): Рекомендованно рабочих минут курьеров. Число кратно 15-ти. Example:
            1800.
        scheduled_unit_labor_minutes (int): Запланированно рабочих минут сотрудников заведения. Число кратно 15-ти.
            Example: 1800.
        scheduled_courier_labor_minutes (int): Запланированно рабочих минут курьеров. Число кратно 15-ти. Example: 1800.
    """

    forecast_for_hour_local: int
    forecast_revenue: float
    forecast_products_count: float
    forecast_courier_orders_count: float
    recommended_unit_labor_minutes: int
    recommended_courier_labor_minutes: int
    scheduled_unit_labor_minutes: int
    scheduled_courier_labor_minutes: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        forecast_for_hour_local = self.forecast_for_hour_local

        forecast_revenue = self.forecast_revenue

        forecast_products_count = self.forecast_products_count

        forecast_courier_orders_count = self.forecast_courier_orders_count

        recommended_unit_labor_minutes = self.recommended_unit_labor_minutes

        recommended_courier_labor_minutes = self.recommended_courier_labor_minutes

        scheduled_unit_labor_minutes = self.scheduled_unit_labor_minutes

        scheduled_courier_labor_minutes = self.scheduled_courier_labor_minutes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "forecastForHourLocal": forecast_for_hour_local,
                "forecastRevenue": forecast_revenue,
                "forecastProductsCount": forecast_products_count,
                "forecastCourierOrdersCount": forecast_courier_orders_count,
                "recommendedUnitLaborMinutes": recommended_unit_labor_minutes,
                "recommendedCourierLaborMinutes": recommended_courier_labor_minutes,
                "scheduledUnitLaborMinutes": scheduled_unit_labor_minutes,
                "scheduledCourierLaborMinutes": scheduled_courier_labor_minutes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        forecast_for_hour_local = d.pop("forecastForHourLocal")

        forecast_revenue = d.pop("forecastRevenue")

        forecast_products_count = d.pop("forecastProductsCount")

        forecast_courier_orders_count = d.pop("forecastCourierOrdersCount")

        recommended_unit_labor_minutes = d.pop("recommendedUnitLaborMinutes")

        recommended_courier_labor_minutes = d.pop("recommendedCourierLaborMinutes")

        scheduled_unit_labor_minutes = d.pop("scheduledUnitLaborMinutes")

        scheduled_courier_labor_minutes = d.pop("scheduledCourierLaborMinutes")

        staff_schedule_forecast_forecast_by_hour_item = cls(
            forecast_for_hour_local=forecast_for_hour_local,
            forecast_revenue=forecast_revenue,
            forecast_products_count=forecast_products_count,
            forecast_courier_orders_count=forecast_courier_orders_count,
            recommended_unit_labor_minutes=recommended_unit_labor_minutes,
            recommended_courier_labor_minutes=recommended_courier_labor_minutes,
            scheduled_unit_labor_minutes=scheduled_unit_labor_minutes,
            scheduled_courier_labor_minutes=scheduled_courier_labor_minutes,
        )

        staff_schedule_forecast_forecast_by_hour_item.additional_properties = d
        return staff_schedule_forecast_forecast_by_hour_item

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
