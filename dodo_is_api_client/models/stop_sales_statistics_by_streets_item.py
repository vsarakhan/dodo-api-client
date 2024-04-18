from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StopSalesStatisticsByStreetsItem")


@_attrs_define
class StopSalesStatisticsByStreetsItem:
    """Статистика стопов по улицам

    Attributes:
        id (str): Id стопа Example: 000d3a240c719a8711e68aba13f7fe13.
        unit_id (str): Идентификатор пиццерии Example: 000d3a240c719a8711e68aba13f7fe13.
        unit_name (str): Название пиццерии в форматах Сыктывкар-1 или Москва 0-1 Example: Сыктывкар-1.
        street_name (str): Улица поставленная в стоп продажи Example: Флотская.
        sector_name (str): Сектор, в которых входит улица Example: Водный Стадион за Смольной.
        reason (str): Причина постаавновки в стоп
        started_at (str): Время начала стопа в формате ISO 8601
        ended_at (Union[None, str]): Время возобновления продаж в формате ISO 8601 (null - если еще не возобновлено)
        stopped_by_user_id (str): Id пользователя, который инициировал стоп продаж Example:
            000d3a240c719a8711e68aba13f7fe13.
        resumed_by_user_id (Union[None, str]): Id пользователя, который возобновил продажи (null - если еще не
            возобновлено) Example: 000d3a240c719a8711e68aba13f7fe13.
    """

    id: str
    unit_id: str
    unit_name: str
    street_name: str
    sector_name: str
    reason: str
    started_at: str
    ended_at: Union[None, str]
    stopped_by_user_id: str
    resumed_by_user_id: Union[None, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        unit_id = self.unit_id

        unit_name = self.unit_name

        street_name = self.street_name

        sector_name = self.sector_name

        reason = self.reason

        started_at = self.started_at

        ended_at: Union[None, str]
        ended_at = self.ended_at

        stopped_by_user_id = self.stopped_by_user_id

        resumed_by_user_id: Union[None, str]
        resumed_by_user_id = self.resumed_by_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "unitId": unit_id,
                "unitName": unit_name,
                "streetName": street_name,
                "sectorName": sector_name,
                "reason": reason,
                "startedAt": started_at,
                "endedAt": ended_at,
                "stoppedByUserId": stopped_by_user_id,
                "resumedByUserId": resumed_by_user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        street_name = d.pop("streetName")

        sector_name = d.pop("sectorName")

        reason = d.pop("reason")

        started_at = d.pop("startedAt")

        def _parse_ended_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        ended_at = _parse_ended_at(d.pop("endedAt"))

        stopped_by_user_id = d.pop("stoppedByUserId")

        def _parse_resumed_by_user_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        resumed_by_user_id = _parse_resumed_by_user_id(d.pop("resumedByUserId"))

        stop_sales_statistics_by_streets_item = cls(
            id=id,
            unit_id=unit_id,
            unit_name=unit_name,
            street_name=street_name,
            sector_name=sector_name,
            reason=reason,
            started_at=started_at,
            ended_at=ended_at,
            stopped_by_user_id=stopped_by_user_id,
            resumed_by_user_id=resumed_by_user_id,
        )

        stop_sales_statistics_by_streets_item.additional_properties = d
        return stop_sales_statistics_by_streets_item

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
