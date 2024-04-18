from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.measurement_unit import MeasurementUnit
from ..models.stock_consumption_consumption_type import StockConsumptionConsumptionType

T = TypeVar("T", bound="StockConsumption")


@_attrs_define
class StockConsumption:
    """Расход сырья

    Значения единиц измерения продуктов:
    <code>
    Quantity: 1
    Kilogram: 4
    Liter: 6
    Meter: 8
    </code>

    Значение типа расхода:
    <code>
    Defect: 10 (брак)
    StaffMeal: 20 (питание персонала)
    Sale: 30 (продажи)
    Cancel: 40 (отмена заказа)
    Production: 60 (производство)
    </code>

        Attributes:
            unit_id (str): Идентификатор заведения Example: 000d3a240c719a8711e68aba13f7fe13.
            unit_name (str): Наименование заведения Example: Сыктывкар-1.
            consumption_type (StockConsumptionConsumptionType): Тип расхода Example: Production.
            stock_item_id (str): Идентификатор сырья Example: 000d3a240c719a8711e68aba13f7fe13.
            stock_item_name (str): Наименование сырья Example: Ветчина.
            measurement_unit (MeasurementUnit): Наименование единицы измерения Example: Quantity.
            quantity (float): Количество расхода в формате #.### Example: 0.352.
    """

    unit_id: str
    unit_name: str
    consumption_type: StockConsumptionConsumptionType
    stock_item_id: str
    stock_item_name: str
    measurement_unit: MeasurementUnit
    quantity: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        unit_name = self.unit_name

        consumption_type = self.consumption_type.value

        stock_item_id = self.stock_item_id

        stock_item_name = self.stock_item_name

        measurement_unit = self.measurement_unit.value

        quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitId": unit_id,
                "unitName": unit_name,
                "consumptionType": consumption_type,
                "stockItemId": stock_item_id,
                "stockItemName": stock_item_name,
                "measurementUnit": measurement_unit,
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit_id = d.pop("unitId")

        unit_name = d.pop("unitName")

        consumption_type = StockConsumptionConsumptionType(d.pop("consumptionType"))

        stock_item_id = d.pop("stockItemId")

        stock_item_name = d.pop("stockItemName")

        measurement_unit = MeasurementUnit(d.pop("measurementUnit"))

        quantity = d.pop("quantity")

        stock_consumption = cls(
            unit_id=unit_id,
            unit_name=unit_name,
            consumption_type=consumption_type,
            stock_item_id=stock_item_id,
            stock_item_name=stock_item_name,
            measurement_unit=measurement_unit,
            quantity=quantity,
        )

        stock_consumption.additional_properties = d
        return stock_consumption

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
