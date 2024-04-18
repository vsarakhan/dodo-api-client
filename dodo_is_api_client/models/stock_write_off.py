import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.measurement_unit import MeasurementUnit
from ..models.stock_write_off_reason import StockWriteOffReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="StockWriteOff")


@_attrs_define
class StockWriteOff:
    """Списание сырья

    Причины списаний:
    <code>
    Expired: 100 (Вышел срок годности)
    Defected: 200 (Порчи продукта)
    DamagedPackaging: 300 (Повреждение упаковки)
    HumanElement: 400 (Человеческий фактор)
    Marketing: 500 (Маркетинговые мероприятия)
    ExpiredShowcaseTime: 600 (Списания по времени с витрины)
    ShowcaseWriteOff: 700 (Списания кусочков)
    </code>

    Значения единиц измерения:
    <code>
    Quantity: 1
    Kilogram: 4
    Liter: 6
    Meter: 8
    </code>

        Attributes:
            unit_id (str): Идентификатор заведения Example: 000d3a240c719a8711e68aba13f7f862.
            unit_name (str): Название заведения Example: Сыктывкар-1.
            written_off_at_local (datetime.datetime): Дата и время списания (локальное время) Example: 2011-08-01T18:31:42.
            stock_item_id (str): Идентификатор сырья списания Example: 000d3a240c719a8711e68aba13f7f862.
            stock_item_name (str): Наименование списанного сырья Example: Бекон.
            quantity (float): Списанное количество Example: 0.352.
            measurement_unit (MeasurementUnit): Наименование единицы измерения Example: Quantity.
            reason (StockWriteOffReason): Причина списания Example: Marketing.
            written_off_at (Union[Unset, datetime.datetime]): Дата и время списания (Возвращает локальное время вместо UTC)
                Example: 2011-08-01T18:31:42.
    """

    unit_id: str
    unit_name: str
    written_off_at_local: datetime.datetime
    stock_item_id: str
    stock_item_name: str
    quantity: float
    measurement_unit: MeasurementUnit
    reason: StockWriteOffReason
    written_off_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        unit_name = self.unit_name

        written_off_at_local = self.written_off_at_local.isoformat()

        stock_item_id = self.stock_item_id

        stock_item_name = self.stock_item_name

        quantity = self.quantity

        measurement_unit = self.measurement_unit.value

        reason = self.reason.value

        written_off_at: Union[Unset, str] = UNSET
        if not isinstance(self.written_off_at, Unset):
            written_off_at = self.written_off_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitId": unit_id,
                "unitName": unit_name,
                "writtenOffAtLocal": written_off_at_local,
                "stockItemId": stock_item_id,
                "stockItemName": stock_item_name,
                "quantity": quantity,
                "measurementUnit": measurement_unit,
                "reason": reason,
            }
        )
        if written_off_at is not UNSET:
            field_dict["writtenOffAt"] = written_off_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        written_off_at_local = isoparse(d.pop("writtenOffAtLocal"))

        stock_item_id = d.pop("stockItemId")

        stock_item_name = d.pop("stockItemName")

        quantity = d.pop("quantity")

        measurement_unit = MeasurementUnit(d.pop("measurementUnit"))

        reason = StockWriteOffReason(d.pop("reason"))

        _written_off_at = d.pop("writtenOffAt", UNSET)
        written_off_at: Union[Unset, datetime.datetime]
        if isinstance(_written_off_at, Unset):
            written_off_at = UNSET
        else:
            written_off_at = isoparse(_written_off_at)

        stock_write_off = cls(
            unit_id=unit_id,
            unit_name=unit_name,
            written_off_at_local=written_off_at_local,
            stock_item_id=stock_item_id,
            stock_item_name=stock_item_name,
            quantity=quantity,
            measurement_unit=measurement_unit,
            reason=reason,
            written_off_at=written_off_at,
        )

        stock_write_off.additional_properties = d
        return stock_write_off

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
