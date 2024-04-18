from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.measurement_unit import MeasurementUnit

T = TypeVar("T", bound="ProductStockItemWriteOff")


@_attrs_define
class ProductStockItemWriteOff:
    """Сырье в составе списанного продукта

    Значения единиц измерения продуктов
    <code>
    Quantity: 1
    Kilogram: 4
    Liter: 6
    Meter: 8
    </code>

        Attributes:
            id (str): Идентификатор сырья Example: 000d3a240c719a8711e68aba13f7f862.
            name (str): Название сырья Example: Ананасы.
            quantity (float): Списанное количество в формате #.### Example: 0.352.
            measurement_unit (MeasurementUnit): Наименование единицы измерения Example: Quantity.
    """

    id: str
    name: str
    quantity: float
    measurement_unit: MeasurementUnit
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        quantity = self.quantity

        measurement_unit = self.measurement_unit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "quantity": quantity,
                "measurementUnit": measurement_unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        quantity = d.pop("quantity")

        measurement_unit = MeasurementUnit(d.pop("measurementUnit"))

        product_stock_item_write_off = cls(
            id=id,
            name=name,
            quantity=quantity,
            measurement_unit=measurement_unit,
        )

        product_stock_item_write_off.additional_properties = d
        return product_stock_item_write_off

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
