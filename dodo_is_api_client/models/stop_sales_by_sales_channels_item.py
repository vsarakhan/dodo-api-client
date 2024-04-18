import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.stop_sales_by_sales_channels_item_channel_stop_type import StopSalesBySalesChannelsItemChannelStopType
from ..models.stop_sales_by_sales_channels_item_sales_channel_name import StopSalesBySalesChannelsItemSalesChannelName
from ..types import UNSET, Unset

T = TypeVar("T", bound="StopSalesBySalesChannelsItem")


@_attrs_define
class StopSalesBySalesChannelsItem:
    """Статистика стоп-продаж по каналам продаж

    Attributes:
        id (str): Id стопа Example: 000d3a240c719a8711e68aba13f7fe13.
        unit_id (str): Идентификатор пиццерии Example: 000d3a240c719a8711e68aba13f7fe13.
        unit_name (str): Название пиццерии в форматах Сыктывкар-1 или Москва 0-1 Example: Сыктывкар-1.
        sales_channel_name (StopSalesBySalesChannelsItemSalesChannelName): Канал продажи поставленный в стоп
        reason (str): Причина постановки в стоп Example: Нехватка курьеров.
        started_at_local (datetime.datetime): Время начала стопа в формате ISO 8601 (локальное время)
             Example: 2016-01-03T10:20:31.
        ended_at_local (Union[None, datetime.datetime]): Время возобновления продаж в формате ISO 8601 (локальное время)
            (null - если еще не возобновлено) Example: 2016-01-03T10:20:31.
        stopped_by_user_id (str): Id сотрудника, который инициировал стоп продаж Example:
            000d3a240c719a8711e68aba13f7fe13.
        resumed_by_user_id (Union[None, str]): Id сотрудника, который возобновил продажи (null - если еще не
            возобновлено) Example: 000d3a240c719a8711e68aba13f7fe13.
        channel_stop_type (StopSalesBySalesChannelsItemChannelStopType): Как были приостановлены продажи Example:
            Complete.
        started_at (Union[Unset, datetime.datetime]): Возвращает локальное время вместо UTC Example:
            2016-01-03T10:20:31.
        ended_at (Union[None, Unset, datetime.datetime]): Возвращает локальное время вместо UTC (null - если еще не
            возобновлено) Example: 2016-01-03T10:20:31.
    """

    id: str
    unit_id: str
    unit_name: str
    sales_channel_name: StopSalesBySalesChannelsItemSalesChannelName
    reason: str
    started_at_local: datetime.datetime
    ended_at_local: Union[None, datetime.datetime]
    stopped_by_user_id: str
    resumed_by_user_id: Union[None, str]
    channel_stop_type: StopSalesBySalesChannelsItemChannelStopType
    started_at: Union[Unset, datetime.datetime] = UNSET
    ended_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        unit_id = self.unit_id

        unit_name = self.unit_name

        sales_channel_name = self.sales_channel_name.value

        reason = self.reason

        started_at_local = self.started_at_local.isoformat()

        ended_at_local: Union[None, str]
        if isinstance(self.ended_at_local, datetime.datetime):
            ended_at_local = self.ended_at_local.isoformat()
        else:
            ended_at_local = self.ended_at_local

        stopped_by_user_id = self.stopped_by_user_id

        resumed_by_user_id: Union[None, str]
        resumed_by_user_id = self.resumed_by_user_id

        channel_stop_type = self.channel_stop_type.value

        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        ended_at: Union[None, Unset, str]
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "unitId": unit_id,
                "unitName": unit_name,
                "salesChannelName": sales_channel_name,
                "reason": reason,
                "startedAtLocal": started_at_local,
                "endedAtLocal": ended_at_local,
                "stoppedByUserId": stopped_by_user_id,
                "resumedByUserId": resumed_by_user_id,
                "channelStopType": channel_stop_type,
            }
        )
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        sales_channel_name = StopSalesBySalesChannelsItemSalesChannelName(d.pop("salesChannelName"))

        reason = d.pop("reason")

        started_at_local = isoparse(d.pop("startedAtLocal"))

        def _parse_ended_at_local(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_local_type_0 = isoparse(data)

                return ended_at_local_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        ended_at_local = _parse_ended_at_local(d.pop("endedAtLocal"))

        stopped_by_user_id = d.pop("stoppedByUserId")

        def _parse_resumed_by_user_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        resumed_by_user_id = _parse_resumed_by_user_id(d.pop("resumedByUserId"))

        channel_stop_type = StopSalesBySalesChannelsItemChannelStopType(d.pop("channelStopType"))

        _started_at = d.pop("startedAt", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        def _parse_ended_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = isoparse(data)

                return ended_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        ended_at = _parse_ended_at(d.pop("endedAt", UNSET))

        stop_sales_by_sales_channels_item = cls(
            id=id,
            unit_id=unit_id,
            unit_name=unit_name,
            sales_channel_name=sales_channel_name,
            reason=reason,
            started_at_local=started_at_local,
            ended_at_local=ended_at_local,
            stopped_by_user_id=stopped_by_user_id,
            resumed_by_user_id=resumed_by_user_id,
            channel_stop_type=channel_stop_type,
            started_at=started_at,
            ended_at=ended_at,
        )

        stop_sales_by_sales_channels_item.additional_properties = d
        return stop_sales_by_sales_channels_item

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
