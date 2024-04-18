import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.staff_schedule_forecast_forecast_by_hour_item import StaffScheduleForecastForecastByHourItem


T = TypeVar("T", bound="StaffScheduleForecast")


@_attrs_define
class StaffScheduleForecast:
    """
    Attributes:
        unit_id (str): Идентификатор заведения (пиццерии) Example: 2a69836ab8f583ec11ed90098ae24dff.
        forecast_date (datetime.date): Дата построения прогноза в формате ISO 8601 Example: 2000-01-01T00:00:00.
        forecast_revenue (float): Прогнозная выручка на день в рублях Example: 250000.89.
        forecast_products_count (float): Прогнозное количество приготавливаемых продуктов на день Example: 150.
        forecast_courier_orders_count (float): Прогнозное количество заказов на доставку за день Example: 80.
        forecast_revenue_productivity (float): Прогнозная производительность в выручке на человека в час. Example:
            3799.67.
        forecast_products_productivity (float): Прогнозная производительность в продуктах на человека в час. Example:
            7.3.
        forecast_courier_productivity (float): Прогнозная производительность в заказах на курьера в час. Example: 1.76.
        scheduled_unit_labor_minutes (int): Назначено рабочих минут всех сотрудников заведения (пиццерии). Число кратно
            15-ти. Example: 2400.
        scheduled_courier_labor_minutes (int): Назначено рабочих минут курьеров. Число кратно 15-ти. Example: 2400.
        goal_revenue_productivity (float): Целевая производительность в выручке на человека в час. Example: 2500.
        goal_products_productivity (float): Целевая производительность в продуктах на человека в час. Example: 6.5.
        goal_courier_productivity (float): Целевая производительность в заказах на курьера в час. Example: 1.9.
        forecast_by_hour (List['StaffScheduleForecastForecastByHourItem']): Детализация прогноза по часам
    """

    unit_id: str
    forecast_date: datetime.date
    forecast_revenue: float
    forecast_products_count: float
    forecast_courier_orders_count: float
    forecast_revenue_productivity: float
    forecast_products_productivity: float
    forecast_courier_productivity: float
    scheduled_unit_labor_minutes: int
    scheduled_courier_labor_minutes: int
    goal_revenue_productivity: float
    goal_products_productivity: float
    goal_courier_productivity: float
    forecast_by_hour: List["StaffScheduleForecastForecastByHourItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        forecast_date = self.forecast_date.isoformat()

        forecast_revenue = self.forecast_revenue

        forecast_products_count = self.forecast_products_count

        forecast_courier_orders_count = self.forecast_courier_orders_count

        forecast_revenue_productivity = self.forecast_revenue_productivity

        forecast_products_productivity = self.forecast_products_productivity

        forecast_courier_productivity = self.forecast_courier_productivity

        scheduled_unit_labor_minutes = self.scheduled_unit_labor_minutes

        scheduled_courier_labor_minutes = self.scheduled_courier_labor_minutes

        goal_revenue_productivity = self.goal_revenue_productivity

        goal_products_productivity = self.goal_products_productivity

        goal_courier_productivity = self.goal_courier_productivity

        forecast_by_hour = []
        for forecast_by_hour_item_data in self.forecast_by_hour:
            forecast_by_hour_item = forecast_by_hour_item_data.to_dict()
            forecast_by_hour.append(forecast_by_hour_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitId": unit_id,
                "forecastDate": forecast_date,
                "forecastRevenue": forecast_revenue,
                "forecastProductsCount": forecast_products_count,
                "forecastCourierOrdersCount": forecast_courier_orders_count,
                "forecastRevenueProductivity": forecast_revenue_productivity,
                "forecastProductsProductivity": forecast_products_productivity,
                "forecastCourierProductivity": forecast_courier_productivity,
                "scheduledUnitLaborMinutes": scheduled_unit_labor_minutes,
                "scheduledCourierLaborMinutes": scheduled_courier_labor_minutes,
                "goalRevenueProductivity": goal_revenue_productivity,
                "goalProductsProductivity": goal_products_productivity,
                "goalCourierProductivity": goal_courier_productivity,
                "forecastByHour": forecast_by_hour,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.staff_schedule_forecast_forecast_by_hour_item import StaffScheduleForecastForecastByHourItem

        d = src_dict.copy()
        unit_id = d.pop("unitId")

        forecast_date = isoparse(d.pop("forecastDate")).date()

        forecast_revenue = d.pop("forecastRevenue")

        forecast_products_count = d.pop("forecastProductsCount")

        forecast_courier_orders_count = d.pop("forecastCourierOrdersCount")

        forecast_revenue_productivity = d.pop("forecastRevenueProductivity")

        forecast_products_productivity = d.pop("forecastProductsProductivity")

        forecast_courier_productivity = d.pop("forecastCourierProductivity")

        scheduled_unit_labor_minutes = d.pop("scheduledUnitLaborMinutes")

        scheduled_courier_labor_minutes = d.pop("scheduledCourierLaborMinutes")

        goal_revenue_productivity = d.pop("goalRevenueProductivity")

        goal_products_productivity = d.pop("goalProductsProductivity")

        goal_courier_productivity = d.pop("goalCourierProductivity")

        forecast_by_hour = []
        _forecast_by_hour = d.pop("forecastByHour")
        for forecast_by_hour_item_data in _forecast_by_hour:
            forecast_by_hour_item = StaffScheduleForecastForecastByHourItem.from_dict(forecast_by_hour_item_data)

            forecast_by_hour.append(forecast_by_hour_item)

        staff_schedule_forecast = cls(
            unit_id=unit_id,
            forecast_date=forecast_date,
            forecast_revenue=forecast_revenue,
            forecast_products_count=forecast_products_count,
            forecast_courier_orders_count=forecast_courier_orders_count,
            forecast_revenue_productivity=forecast_revenue_productivity,
            forecast_products_productivity=forecast_products_productivity,
            forecast_courier_productivity=forecast_courier_productivity,
            scheduled_unit_labor_minutes=scheduled_unit_labor_minutes,
            scheduled_courier_labor_minutes=scheduled_courier_labor_minutes,
            goal_revenue_productivity=goal_revenue_productivity,
            goal_products_productivity=goal_products_productivity,
            goal_courier_productivity=goal_courier_productivity,
            forecast_by_hour=forecast_by_hour,
        )

        staff_schedule_forecast.additional_properties = d
        return staff_schedule_forecast

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
