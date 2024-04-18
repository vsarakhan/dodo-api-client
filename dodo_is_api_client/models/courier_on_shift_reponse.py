import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="CourierOnShiftReponse")


@_attrs_define
class CourierOnShiftReponse:
    """
    Attributes:
        id (str): Идентификатор сотрудника Example: 000d3a240c719a8711e68aba13f7fe16.
        clock_in_at (datetime.datetime): Дата и время начала смены Example: 2019-08-24T14:15:22Z.
        clock_in_at_local (datetime.datetime): Локальные дата и время начала смены Example: 2019-08-24T14:15:22.
        scheduled_clock_out_at (Union[None, datetime.datetime]): Дата и время планируемого окончания смены Example:
            2019-08-24T14:15:22Z.
        scheduled_clock_out_at_local (Union[None, datetime.datetime]): Локальные дата и время планируемого окончания
            смены Example: 2019-08-24T14:15:22.
        position_id (str): Идентификатор должности сотрудника на смене Example: 000d3a240c719a8711e68aba13f7fe16.
        position_name (str): Должность сотрудника на смене Example: Автомобильный.
        schedule_id (Union[None, str]): Идентификатор запланированной смены. Принимает значение `null` для
            незапланированной смены и для смен до 04.04.2024 Example: 000d3a38a8a3956a11e85cdf24610f83.
        unit_id (str): Идентификатор заведения (пиццерии) Example: 000d3a240c719a8711e68aba13f7fe16.
        unit_name (str): Название заведения Example: Сыктывкар-1.
        delivered_orders_count (int): Количество доставленных заказов
        late_orders_count (int): Количество доставленных заказов c опозданием
        cash_from_orders (float): Наличные от заказов Example: 699.
    """

    id: str
    clock_in_at: datetime.datetime
    clock_in_at_local: datetime.datetime
    scheduled_clock_out_at: Union[None, datetime.datetime]
    scheduled_clock_out_at_local: Union[None, datetime.datetime]
    position_id: str
    position_name: str
    schedule_id: Union[None, str]
    unit_id: str
    unit_name: str
    delivered_orders_count: int
    late_orders_count: int
    cash_from_orders: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        clock_in_at = self.clock_in_at.isoformat()

        clock_in_at_local = self.clock_in_at_local.isoformat()

        scheduled_clock_out_at: Union[None, str]
        if isinstance(self.scheduled_clock_out_at, datetime.datetime):
            scheduled_clock_out_at = self.scheduled_clock_out_at.isoformat()
        else:
            scheduled_clock_out_at = self.scheduled_clock_out_at

        scheduled_clock_out_at_local: Union[None, str]
        if isinstance(self.scheduled_clock_out_at_local, datetime.datetime):
            scheduled_clock_out_at_local = self.scheduled_clock_out_at_local.isoformat()
        else:
            scheduled_clock_out_at_local = self.scheduled_clock_out_at_local

        position_id = self.position_id

        position_name = self.position_name

        schedule_id: Union[None, str]
        schedule_id = self.schedule_id

        unit_id = self.unit_id

        unit_name = self.unit_name

        delivered_orders_count = self.delivered_orders_count

        late_orders_count = self.late_orders_count

        cash_from_orders = self.cash_from_orders

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "clockInAt": clock_in_at,
                "clockInAtLocal": clock_in_at_local,
                "scheduledClockOutAt": scheduled_clock_out_at,
                "scheduledClockOutAtLocal": scheduled_clock_out_at_local,
                "positionId": position_id,
                "positionName": position_name,
                "scheduleId": schedule_id,
                "unitId": unit_id,
                "unitName": unit_name,
                "deliveredOrdersCount": delivered_orders_count,
                "lateOrdersCount": late_orders_count,
                "cashFromOrders": cash_from_orders,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        clock_in_at = isoparse(d.pop("clockInAt"))

        clock_in_at_local = isoparse(d.pop("clockInAtLocal"))

        def _parse_scheduled_clock_out_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_clock_out_at_type_0 = isoparse(data)

                return scheduled_clock_out_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        scheduled_clock_out_at = _parse_scheduled_clock_out_at(d.pop("scheduledClockOutAt"))

        def _parse_scheduled_clock_out_at_local(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_clock_out_at_local_type_0 = isoparse(data)

                return scheduled_clock_out_at_local_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        scheduled_clock_out_at_local = _parse_scheduled_clock_out_at_local(d.pop("scheduledClockOutAtLocal"))

        position_id = d.pop("positionId")

        position_name = d.pop("positionName")

        def _parse_schedule_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        schedule_id = _parse_schedule_id(d.pop("scheduleId"))

        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        delivered_orders_count = d.pop("deliveredOrdersCount")

        late_orders_count = d.pop("lateOrdersCount")

        cash_from_orders = d.pop("cashFromOrders")

        courier_on_shift_reponse = cls(
            id=id,
            clock_in_at=clock_in_at,
            clock_in_at_local=clock_in_at_local,
            scheduled_clock_out_at=scheduled_clock_out_at,
            scheduled_clock_out_at_local=scheduled_clock_out_at_local,
            position_id=position_id,
            position_name=position_name,
            schedule_id=schedule_id,
            unit_id=unit_id,
            unit_name=unit_name,
            delivered_orders_count=delivered_orders_count,
            late_orders_count=late_orders_count,
            cash_from_orders=cash_from_orders,
        )

        courier_on_shift_reponse.additional_properties = d
        return courier_on_shift_reponse

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
