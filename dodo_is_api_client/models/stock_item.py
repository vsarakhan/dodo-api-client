import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.measurement_unit import MeasurementUnit
from ..models.stock_item_category_name import StockItemCategoryName

T = TypeVar("T", bound="StockItem")


@_attrs_define
class StockItem:
    """Сырье в справочнике сырья

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
            measurement_unit (MeasurementUnit): Наименование единицы измерения Example: Quantity.
            category_name (StockItemCategoryName): Категория сырья Example: Ingredient.
            modified_at (datetime.datetime): Дата и время изменения в формате ISO 8601 Example: 2022-10-01T08:00:00.
    """

    id: str
    name: str
    measurement_unit: MeasurementUnit
    category_name: StockItemCategoryName
    modified_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        measurement_unit = self.measurement_unit.value

        category_name = self.category_name.value

        modified_at = self.modified_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "measurementUnit": measurement_unit,
                "categoryName": category_name,
                "modifiedAt": modified_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        measurement_unit = MeasurementUnit(d.pop("measurementUnit"))

        category_name = StockItemCategoryName(d.pop("categoryName"))

        modified_at = isoparse(d.pop("modifiedAt"))

        stock_item = cls(
            id=id,
            name=name,
            measurement_unit=measurement_unit,
            category_name=category_name,
            modified_at=modified_at,
        )

        stock_item.additional_properties = d
        return stock_item

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
