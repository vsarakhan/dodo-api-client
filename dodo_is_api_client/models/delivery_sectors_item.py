from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delivery_sectors_item_geometry import DeliverySectorsItemGeometry


T = TypeVar("T", bound="DeliverySectorsItem")


@_attrs_define
class DeliverySectorsItem:
    """Сектор доставки

    Attributes:
        unit_id (Union[Unset, str]): Идентификатор пиццерии Example: 000d3a240c719a8711e68aba13f7fe13.
        unit_name (Union[Unset, str]): Название пиццерии в форматах Сыктывкар-1 или Москва 0-1 Example: Сыктывкар-1.
        sector_id (Union[Unset, str]): Id сектора доставки Example: 000d3a240c719a8711e68aba13f7fe13.
        sector_name (Union[Unset, str]): Название сектора Example: Водный Стадион за Смольной.
        is_deleted (Union[Unset, bool]): Сектор удален
        is_stopped (Union[Unset, bool]): Сектор находится в стопе
        is_sub_sector (Union[Unset, bool]): Является ли сектор под-сектором, созданным из менеджера смены
        geometry (Union[Unset, DeliverySectorsItemGeometry]): Объект в формате Geo-json, описывающий форму зоны доставки
            на карте Example: {"type":"Polygon","coordinates":[[[129.763343,62.032773],[129.751052,62.032828],[129.749372,62
            .028192],[129.763343,62.032773]]]}.
    """

    unit_id: Union[Unset, str] = UNSET
    unit_name: Union[Unset, str] = UNSET
    sector_id: Union[Unset, str] = UNSET
    sector_name: Union[Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET
    is_stopped: Union[Unset, bool] = UNSET
    is_sub_sector: Union[Unset, bool] = UNSET
    geometry: Union[Unset, "DeliverySectorsItemGeometry"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        unit_name = self.unit_name

        sector_id = self.sector_id

        sector_name = self.sector_name

        is_deleted = self.is_deleted

        is_stopped = self.is_stopped

        is_sub_sector = self.is_sub_sector

        geometry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.geometry, Unset):
            geometry = self.geometry.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit_id is not UNSET:
            field_dict["unitId"] = unit_id
        if unit_name is not UNSET:
            field_dict["unitName"] = unit_name
        if sector_id is not UNSET:
            field_dict["sectorId"] = sector_id
        if sector_name is not UNSET:
            field_dict["sectorName"] = sector_name
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if is_stopped is not UNSET:
            field_dict["isStopped"] = is_stopped
        if is_sub_sector is not UNSET:
            field_dict["isSubSector"] = is_sub_sector
        if geometry is not UNSET:
            field_dict["geometry"] = geometry

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.delivery_sectors_item_geometry import DeliverySectorsItemGeometry

        d = src_dict.copy()
        unit_id = d.pop("unitId", UNSET)

        unit_name = d.pop("unitName", UNSET)

        sector_id = d.pop("sectorId", UNSET)

        sector_name = d.pop("sectorName", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        is_stopped = d.pop("isStopped", UNSET)

        is_sub_sector = d.pop("isSubSector", UNSET)

        _geometry = d.pop("geometry", UNSET)
        geometry: Union[Unset, DeliverySectorsItemGeometry]
        if isinstance(_geometry, Unset):
            geometry = UNSET
        else:
            geometry = DeliverySectorsItemGeometry.from_dict(_geometry)

        delivery_sectors_item = cls(
            unit_id=unit_id,
            unit_name=unit_name,
            sector_id=sector_id,
            sector_name=sector_name,
            is_deleted=is_deleted,
            is_stopped=is_stopped,
            is_sub_sector=is_sub_sector,
            geometry=geometry,
        )

        delivery_sectors_item.additional_properties = d
        return delivery_sectors_item

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
