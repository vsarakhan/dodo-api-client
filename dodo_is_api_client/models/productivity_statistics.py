from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProductivityStatistics")


@_attrs_define
class ProductivityStatistics:
    """Статистика производительности

    Attributes:
        unit_id (str): Идентификатор пиццерии Example: 000d3a240c719a8711e68aba13f7fe13.
        unit_name (str): Название пиццерии в форматах Сыктывкар-1 или Москва 0-1 Example: Москва 0-1.
        labor_hours (float): Отработано часов Example: 17.
        sales (float): Выручка Example: 78493.13.
        sales_per_labor_hour (float): Выручка на человека в час Example: 1352.9.
        products_per_labor_hour (float): Продуктов на человека в час Example: 4.7.
        avg_heated_shelf_time (int): Время ожидания доставки на тепловой полке в секундах Example: 176.
        orders_per_courier_labour_hour (float): Количество заказов на курьера в час Example: 6.3.
        kitchen_speed_percentage (float): Скорость в % (описание расчёта есть выше) Example: 0.69.
    """

    unit_id: str
    unit_name: str
    labor_hours: float
    sales: float
    sales_per_labor_hour: float
    products_per_labor_hour: float
    avg_heated_shelf_time: int
    orders_per_courier_labour_hour: float
    kitchen_speed_percentage: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        unit_name = self.unit_name

        labor_hours = self.labor_hours

        sales = self.sales

        sales_per_labor_hour = self.sales_per_labor_hour

        products_per_labor_hour = self.products_per_labor_hour

        avg_heated_shelf_time = self.avg_heated_shelf_time

        orders_per_courier_labour_hour = self.orders_per_courier_labour_hour

        kitchen_speed_percentage = self.kitchen_speed_percentage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitId": unit_id,
                "unitName": unit_name,
                "laborHours": labor_hours,
                "sales": sales,
                "salesPerLaborHour": sales_per_labor_hour,
                "productsPerLaborHour": products_per_labor_hour,
                "avgHeatedShelfTime": avg_heated_shelf_time,
                "ordersPerCourierLabourHour": orders_per_courier_labour_hour,
                "kitchenSpeedPercentage": kitchen_speed_percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        labor_hours = d.pop("laborHours")

        sales = d.pop("sales")

        sales_per_labor_hour = d.pop("salesPerLaborHour")

        products_per_labor_hour = d.pop("productsPerLaborHour")

        avg_heated_shelf_time = d.pop("avgHeatedShelfTime")

        orders_per_courier_labour_hour = d.pop("ordersPerCourierLabourHour")

        kitchen_speed_percentage = d.pop("kitchenSpeedPercentage")

        productivity_statistics = cls(
            unit_id=unit_id,
            unit_name=unit_name,
            labor_hours=labor_hours,
            sales=sales,
            sales_per_labor_hour=sales_per_labor_hour,
            products_per_labor_hour=products_per_labor_hour,
            avg_heated_shelf_time=avg_heated_shelf_time,
            orders_per_courier_labour_hour=orders_per_courier_labour_hour,
            kitchen_speed_percentage=kitchen_speed_percentage,
        )

        productivity_statistics.additional_properties = d
        return productivity_statistics

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
