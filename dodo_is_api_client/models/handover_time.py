from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.handover_time_order_source import HandoverTimeOrderSource
from ..models.handover_time_sales_channel import HandoverTimeSalesChannel
from ..types import UNSET, Unset

T = TypeVar("T", bound="HandoverTime")


@_attrs_define
class HandoverTime:
    """Время выдачи заказа

    Attributes:
        unit_id (str): Идентификатор пиццерии Example: 000d3a240c719a8711e68aba13f7fe13.
        unit_name (str): Название пиццерии в форматах Сыктывкар-1 или Москва 0-1 Example: Сыктывкар-1.
        order_id (str): Идентификатор заказа Example: 000d3a240c71aa2111e63dfb55766f19.
        order_number (str): Номер заказа Example: 56-2.
        sales_channel (HandoverTimeSalesChannel): Канал продажи
        order_tracking_start_at_local (str): Время заказа в формате ISO 8601 (локальное время) Example:
            2011-08-01T18:31:42.
        tracking_pending_time (int): Время ожидания на трекинге в секундах с округлением Example: 45.
        cooking_time (int): Время приготовления заказа в секундах с округлением Example: 189.
        heated_shelf_time (int): Время ожидания заказа на тепловой полке в секундах с округлением Example: 121.
        order_source (HandoverTimeOrderSource): Источник заказа Example: MobileApp.
        assembly_time (Union[None, Unset, int]): Время ожидания сборки заказа из приложения в ресторане в секундах с
            округлением. Заполняется только для заказов типа `Dine-in`, в других случаях - null Example: 55.
        order_tracking_start_at (Union[Unset, str]): Возвращает локальное время вместо UTC Example: 2011-08-01T18:31:42.
    """

    unit_id: str
    unit_name: str
    order_id: str
    order_number: str
    sales_channel: HandoverTimeSalesChannel
    order_tracking_start_at_local: str
    tracking_pending_time: int
    cooking_time: int
    heated_shelf_time: int
    order_source: HandoverTimeOrderSource
    assembly_time: Union[None, Unset, int] = UNSET
    order_tracking_start_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        unit_name = self.unit_name

        order_id = self.order_id

        order_number = self.order_number

        sales_channel = self.sales_channel.value

        order_tracking_start_at_local = self.order_tracking_start_at_local

        tracking_pending_time = self.tracking_pending_time

        cooking_time = self.cooking_time

        heated_shelf_time = self.heated_shelf_time

        order_source = self.order_source.value

        assembly_time: Union[None, Unset, int]
        if isinstance(self.assembly_time, Unset):
            assembly_time = UNSET
        else:
            assembly_time = self.assembly_time

        order_tracking_start_at = self.order_tracking_start_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitId": unit_id,
                "unitName": unit_name,
                "orderId": order_id,
                "orderNumber": order_number,
                "salesChannel": sales_channel,
                "orderTrackingStartAtLocal": order_tracking_start_at_local,
                "trackingPendingTime": tracking_pending_time,
                "cookingTime": cooking_time,
                "heatedShelfTime": heated_shelf_time,
                "orderSource": order_source,
            }
        )
        if assembly_time is not UNSET:
            field_dict["assemblyTime"] = assembly_time
        if order_tracking_start_at is not UNSET:
            field_dict["orderTrackingStartAt"] = order_tracking_start_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        order_id = d.pop("orderId")

        order_number = d.pop("orderNumber")

        sales_channel = HandoverTimeSalesChannel(d.pop("salesChannel"))

        order_tracking_start_at_local = d.pop("orderTrackingStartAtLocal")

        tracking_pending_time = d.pop("trackingPendingTime")

        cooking_time = d.pop("cookingTime")

        heated_shelf_time = d.pop("heatedShelfTime")

        order_source = HandoverTimeOrderSource(d.pop("orderSource"))

        def _parse_assembly_time(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        assembly_time = _parse_assembly_time(d.pop("assemblyTime", UNSET))

        order_tracking_start_at = d.pop("orderTrackingStartAt", UNSET)

        handover_time = cls(
            unit_id=unit_id,
            unit_name=unit_name,
            order_id=order_id,
            order_number=order_number,
            sales_channel=sales_channel,
            order_tracking_start_at_local=order_tracking_start_at_local,
            tracking_pending_time=tracking_pending_time,
            cooking_time=cooking_time,
            heated_shelf_time=heated_shelf_time,
            order_source=order_source,
            assembly_time=assembly_time,
            order_tracking_start_at=order_tracking_start_at,
        )

        handover_time.additional_properties = d
        return handover_time

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
