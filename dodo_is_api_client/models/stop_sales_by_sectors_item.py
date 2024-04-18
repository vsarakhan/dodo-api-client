import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StopSalesBySectorsItem")


@_attrs_define
class StopSalesBySectorsItem:
    """Статистика стоп-продаж по ссекторам

    Attributes:
        id (str): Id стопа Example: 000d3a240c719a8711e68aba13f7fe13.
        unit_id (str): Идентификатор пиццерии Example: 000d3a240c719a8711e68aba13f7fe13.
        unit_name (str): Название пиццерии в форматах Сыктывкар-1 или Москва 0-1 Example: Сыктывкар-1.
        sector_name (str): Сектор поставленный в стоп продажи Example: Водный Стадион за Смольной.
        is_sub_sector (bool): Является ли сектор под-сектором, созданным из менеджера смены
        started_at (datetime.datetime): Время начала стопа в UTC в формате ISO 8601
             Example: 2019-08-24T14:15:22Z.
        ended_at (Union[None, datetime.datetime]): Время возобновления продаж в UTC в формате ISO 8601 (null - если еще
            не возобновлено) Example: 2019-08-24T14:15:22Z.
        suspended_by_user_id (Union[None, str]): Id пользователя, который инициировал стоп продаж (null - если данные о
            пользователе отсутствуют) Example: 000d3a240c719a8711e68aba13f7fe13.
        resumed_user_id (Union[None, str]): Id пользователя, который возобновил продажи (null - если еще не
            возобновлено) Example: 000d3a240c719a8711e68aba13f7fe13.
        started_at_local (Union[Unset, datetime.datetime]): Время начала стопа в часовой зоне пиццерии в формате ISO
            8601
             Example: 2019-08-24T14:15:22.
        ended_at_local (Union[None, Unset, datetime.datetime]): Время возобновления продаж в часовой зоне пиццерии в
            формате ISO 8601 (null - если еще не возобновлено) Example: 2019-08-24T14:15:22.
    """

    id: str
    unit_id: str
    unit_name: str
    sector_name: str
    is_sub_sector: bool
    started_at: datetime.datetime
    ended_at: Union[None, datetime.datetime]
    suspended_by_user_id: Union[None, str]
    resumed_user_id: Union[None, str]
    started_at_local: Union[Unset, datetime.datetime] = UNSET
    ended_at_local: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        unit_id = self.unit_id

        unit_name = self.unit_name

        sector_name = self.sector_name

        is_sub_sector = self.is_sub_sector

        started_at = self.started_at.isoformat()

        ended_at: Union[None, str]
        if isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        suspended_by_user_id: Union[None, str]
        suspended_by_user_id = self.suspended_by_user_id

        resumed_user_id: Union[None, str]
        resumed_user_id = self.resumed_user_id

        started_at_local: Union[Unset, str] = UNSET
        if not isinstance(self.started_at_local, Unset):
            started_at_local = self.started_at_local.isoformat()

        ended_at_local: Union[None, Unset, str]
        if isinstance(self.ended_at_local, Unset):
            ended_at_local = UNSET
        elif isinstance(self.ended_at_local, datetime.datetime):
            ended_at_local = self.ended_at_local.isoformat()
        else:
            ended_at_local = self.ended_at_local

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "unitId": unit_id,
                "unitName": unit_name,
                "sectorName": sector_name,
                "isSubSector": is_sub_sector,
                "startedAt": started_at,
                "endedAt": ended_at,
                "suspendedByUserId": suspended_by_user_id,
                "resumedUserId": resumed_user_id,
            }
        )
        if started_at_local is not UNSET:
            field_dict["startedAtLocal"] = started_at_local
        if ended_at_local is not UNSET:
            field_dict["endedAtLocal"] = ended_at_local

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        sector_name = d.pop("sectorName")

        is_sub_sector = d.pop("isSubSector")

        started_at = isoparse(d.pop("startedAt"))

        def _parse_ended_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = isoparse(data)

                return ended_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        ended_at = _parse_ended_at(d.pop("endedAt"))

        def _parse_suspended_by_user_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        suspended_by_user_id = _parse_suspended_by_user_id(d.pop("suspendedByUserId"))

        def _parse_resumed_user_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        resumed_user_id = _parse_resumed_user_id(d.pop("resumedUserId"))

        _started_at_local = d.pop("startedAtLocal", UNSET)
        started_at_local: Union[Unset, datetime.datetime]
        if isinstance(_started_at_local, Unset):
            started_at_local = UNSET
        else:
            started_at_local = isoparse(_started_at_local)

        def _parse_ended_at_local(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_local_type_0 = isoparse(data)

                return ended_at_local_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        ended_at_local = _parse_ended_at_local(d.pop("endedAtLocal", UNSET))

        stop_sales_by_sectors_item = cls(
            id=id,
            unit_id=unit_id,
            unit_name=unit_name,
            sector_name=sector_name,
            is_sub_sector=is_sub_sector,
            started_at=started_at,
            ended_at=ended_at,
            suspended_by_user_id=suspended_by_user_id,
            resumed_user_id=resumed_user_id,
            started_at_local=started_at_local,
            ended_at_local=ended_at_local,
        )

        stop_sales_by_sectors_item.additional_properties = d
        return stop_sales_by_sectors_item

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
