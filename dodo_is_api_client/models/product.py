import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.product_dough_type import ProductDoughType
from ..models.product_measurement_group import ProductMeasurementGroup
from ..models.product_measurement_unit import ProductMeasurementUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_stock_item import ProductStockItem


T = TypeVar("T", bound="Product")


@_attrs_define
class Product:
    """Продукт

    Значения единиц измерения продуктов
    <code>
    Gram: 1
    Kilogram: 2
    Ton: 3
    Pound: 4
    Ounce: 5
    Milliliter: 11
    Liter: 12
    FluidOunce: 13,
    Gallon: 14
    Item: 21
    Millimeter: 31
    Centimeter: 32
    Meter: 33
    Inch: 34
    Foot: 35
    Piece: 41
    PartOfSalad: 42
    PartOfSauce: 43
    ChinaItem: 44
    Portion: 45
    </code>

        Attributes:
            id (str): Идентификатор продукта Example: 000d3a240c719a8711e68aba13f7fe13.
            is_producible (bool): Производимый (false - товар, true - продукт, который производим сами) Default: False.
            default_name (str): Название, построенное с учётом признаков продукта Example: Ветчина и грибы Т Средняя.
            name (str): Название, без учёта признаков продукта Example: Ветчина и грибы.
            measurement_value (float): Значение измерения Example: 30.
            measurement_unit (ProductMeasurementUnit): Единица измерения продукта Example: Gram.
            modified_at (datetime.datetime): Дата и время изменения продукта в формате ISO 8601 Example:
                2022-10-01T08:00:00.
            measurement_group (Union[Unset, ProductMeasurementGroup]): Группа измерения Example: Medium.
            dough_type (Union[Unset, ProductDoughType]): Тип теста Example: Traditional.
            stock_items (Union[Unset, List['ProductStockItem']]):
    """

    id: str
    default_name: str
    name: str
    measurement_value: float
    measurement_unit: ProductMeasurementUnit
    modified_at: datetime.datetime
    is_producible: bool = False
    measurement_group: Union[Unset, ProductMeasurementGroup] = UNSET
    dough_type: Union[Unset, ProductDoughType] = UNSET
    stock_items: Union[Unset, List["ProductStockItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        is_producible = self.is_producible

        default_name = self.default_name

        name = self.name

        measurement_value = self.measurement_value

        measurement_unit = self.measurement_unit.value

        modified_at = self.modified_at.isoformat()

        measurement_group: Union[Unset, str] = UNSET
        if not isinstance(self.measurement_group, Unset):
            measurement_group = self.measurement_group.value

        dough_type: Union[Unset, str] = UNSET
        if not isinstance(self.dough_type, Unset):
            dough_type = self.dough_type.value

        stock_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stock_items, Unset):
            stock_items = []
            for stock_items_item_data in self.stock_items:
                stock_items_item = stock_items_item_data.to_dict()
                stock_items.append(stock_items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "isProducible": is_producible,
                "defaultName": default_name,
                "name": name,
                "measurementValue": measurement_value,
                "measurementUnit": measurement_unit,
                "modifiedAt": modified_at,
            }
        )
        if measurement_group is not UNSET:
            field_dict["measurementGroup"] = measurement_group
        if dough_type is not UNSET:
            field_dict["doughType"] = dough_type
        if stock_items is not UNSET:
            field_dict["stockItems"] = stock_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_stock_item import ProductStockItem

        d = src_dict.copy()
        id = d.pop("id")

        is_producible = d.pop("isProducible")

        default_name = d.pop("defaultName")

        name = d.pop("name")

        measurement_value = d.pop("measurementValue")

        measurement_unit = ProductMeasurementUnit(d.pop("measurementUnit"))

        modified_at = isoparse(d.pop("modifiedAt"))

        _measurement_group = d.pop("measurementGroup", UNSET)
        measurement_group: Union[Unset, ProductMeasurementGroup]
        if isinstance(_measurement_group, Unset):
            measurement_group = UNSET
        else:
            measurement_group = ProductMeasurementGroup(_measurement_group)

        _dough_type = d.pop("doughType", UNSET)
        dough_type: Union[Unset, ProductDoughType]
        if isinstance(_dough_type, Unset):
            dough_type = UNSET
        else:
            dough_type = ProductDoughType(_dough_type)

        stock_items = []
        _stock_items = d.pop("stockItems", UNSET)
        for stock_items_item_data in _stock_items or []:
            stock_items_item = ProductStockItem.from_dict(stock_items_item_data)

            stock_items.append(stock_items_item)

        product = cls(
            id=id,
            is_producible=is_producible,
            default_name=default_name,
            name=name,
            measurement_value=measurement_value,
            measurement_unit=measurement_unit,
            modified_at=modified_at,
            measurement_group=measurement_group,
            dough_type=dough_type,
            stock_items=stock_items,
        )

        product.additional_properties = d
        return product

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
