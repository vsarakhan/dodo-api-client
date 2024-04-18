import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.measurement_unit import MeasurementUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="SemifinishedProductProduction")


@_attrs_define
class SemifinishedProductProduction:
    """Производство полуфабриката

    Attributes:
        unit_id (str): Идентификатор заведения Example: 000d3a240c719a8711e68aba13f7fe13.
        unit_name (str): Название заведения Example: Сыктывкар-1.
        stock_item_id (str): Идентификатор сырья Example: 000d3a240c719a8711e68aba13f7fe13.
        stock_item_name (str): Название сырья Example: Тесто 25.
        produced_at_local (datetime.datetime): Дата и время производства в формате ISO 8601 (локальное время) Example:
            2022-10-01T11:00.
        quantity (float): Кол-во произведенной продукции в формате #.### Example: 200.456.
        price (float): Цена за ед. в формате #.## Example: 2084.54.
        measurement_unit (Union[Unset, MeasurementUnit]): Наименование единицы измерения Example: Quantity.
        produced_at (Union[Unset, datetime.datetime]): Дата и время производства в формате ISO 8601 (Возвращает
            локальное время вместо UTC) Example: 2022-10-01T11:00.
    """

    unit_id: str
    unit_name: str
    stock_item_id: str
    stock_item_name: str
    produced_at_local: datetime.datetime
    quantity: float
    price: float
    measurement_unit: Union[Unset, MeasurementUnit] = UNSET
    produced_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        unit_name = self.unit_name

        stock_item_id = self.stock_item_id

        stock_item_name = self.stock_item_name

        produced_at_local = self.produced_at_local.isoformat()

        quantity = self.quantity

        price = self.price

        measurement_unit: Union[Unset, str] = UNSET
        if not isinstance(self.measurement_unit, Unset):
            measurement_unit = self.measurement_unit.value

        produced_at: Union[Unset, str] = UNSET
        if not isinstance(self.produced_at, Unset):
            produced_at = self.produced_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitId": unit_id,
                "unitName": unit_name,
                "stockItemId": stock_item_id,
                "stockItemName": stock_item_name,
                "producedAtLocal": produced_at_local,
                "quantity": quantity,
                "price": price,
            }
        )
        if measurement_unit is not UNSET:
            field_dict["measurementUnit"] = measurement_unit
        if produced_at is not UNSET:
            field_dict["producedAt"] = produced_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        stock_item_id = d.pop("stockItemId")

        stock_item_name = d.pop("stockItemName")

        produced_at_local = isoparse(d.pop("producedAtLocal"))

        quantity = d.pop("quantity")

        price = d.pop("price")

        _measurement_unit = d.pop("measurementUnit", UNSET)
        measurement_unit: Union[Unset, MeasurementUnit]
        if isinstance(_measurement_unit, Unset):
            measurement_unit = UNSET
        else:
            measurement_unit = MeasurementUnit(_measurement_unit)

        _produced_at = d.pop("producedAt", UNSET)
        produced_at: Union[Unset, datetime.datetime]
        if isinstance(_produced_at, Unset):
            produced_at = UNSET
        else:
            produced_at = isoparse(_produced_at)

        semifinished_product_production = cls(
            unit_id=unit_id,
            unit_name=unit_name,
            stock_item_id=stock_item_id,
            stock_item_name=stock_item_name,
            produced_at_local=produced_at_local,
            quantity=quantity,
            price=price,
            measurement_unit=measurement_unit,
            produced_at=produced_at,
        )

        semifinished_product_production.additional_properties = d
        return semifinished_product_production

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
