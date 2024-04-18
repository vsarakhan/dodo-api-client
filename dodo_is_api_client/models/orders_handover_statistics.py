from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrdersHandoverStatistics")


@_attrs_define
class OrdersHandoverStatistics:
    """Агрегированная статистика выдачи заказов по юниту за период

    Attributes:
        unit_id (str): Идентификатор пиццерии Example: 000d3a240c719a8711e68aba13f7fe13.
        unit_name (str): Название пиццерии в форматах Сыктывкар-1 или Москва 0-1 Example: Сыктывкар-1.
        avg_tracking_pending_time (int): Средняя время ожидания на трекинге в секундах с округлением
        avg_cooking_time (int): Среднее время приготовления заказа в секундах с округлением
        avg_heated_shelf_time (int): Среднее время ожидания заказа на тепловой полке в секундах с округлением
        avg_order_handover_time (int): Среднее время до выдачи заказа в секундах с округлением
        orders_count (int): Количество заказов за запрашиваемый период с учётом исключений: в расчет не попадают заказы
            с временем приготовления выпекаемых продуктов меньше 1 минуты, заказы без выпекаемых продуктов (кусочки,
            напитки, фонданы и т.д.) и заказы с временем выдачи больше 1 часа.
        avg_order_assembly_time (Union[None, Unset, int]): Среднее время ожидания сборки заказа из приложения в
            ресторане в секундах с округлением. Заполняется если отчёт строится только для заказов типа `DineIn`, иначе -
            null Example: 30.
    """

    unit_id: str
    unit_name: str
    avg_tracking_pending_time: int
    avg_cooking_time: int
    avg_heated_shelf_time: int
    avg_order_handover_time: int
    orders_count: int
    avg_order_assembly_time: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        unit_name = self.unit_name

        avg_tracking_pending_time = self.avg_tracking_pending_time

        avg_cooking_time = self.avg_cooking_time

        avg_heated_shelf_time = self.avg_heated_shelf_time

        avg_order_handover_time = self.avg_order_handover_time

        orders_count = self.orders_count

        avg_order_assembly_time: Union[None, Unset, int]
        if isinstance(self.avg_order_assembly_time, Unset):
            avg_order_assembly_time = UNSET
        else:
            avg_order_assembly_time = self.avg_order_assembly_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitId": unit_id,
                "unitName": unit_name,
                "avgTrackingPendingTime": avg_tracking_pending_time,
                "avgCookingTime": avg_cooking_time,
                "avgHeatedShelfTime": avg_heated_shelf_time,
                "avgOrderHandoverTime": avg_order_handover_time,
                "ordersCount": orders_count,
            }
        )
        if avg_order_assembly_time is not UNSET:
            field_dict["avgOrderAssemblyTime"] = avg_order_assembly_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        avg_tracking_pending_time = d.pop("avgTrackingPendingTime")

        avg_cooking_time = d.pop("avgCookingTime")

        avg_heated_shelf_time = d.pop("avgHeatedShelfTime")

        avg_order_handover_time = d.pop("avgOrderHandoverTime")

        orders_count = d.pop("ordersCount")

        def _parse_avg_order_assembly_time(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        avg_order_assembly_time = _parse_avg_order_assembly_time(d.pop("avgOrderAssemblyTime", UNSET))

        orders_handover_statistics = cls(
            unit_id=unit_id,
            unit_name=unit_name,
            avg_tracking_pending_time=avg_tracking_pending_time,
            avg_cooking_time=avg_cooking_time,
            avg_heated_shelf_time=avg_heated_shelf_time,
            avg_order_handover_time=avg_order_handover_time,
            orders_count=orders_count,
            avg_order_assembly_time=avg_order_assembly_time,
        )

        orders_handover_statistics.additional_properties = d
        return orders_handover_statistics

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
