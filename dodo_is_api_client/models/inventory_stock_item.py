from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.measurement_unit import MeasurementUnit
from ..models.stock_item_category_name import StockItemCategoryName

T = TypeVar("T", bound="InventoryStockItem")


@_attrs_define
class InventoryStockItem:
    """
    Attributes:
        id (str): Идентификатор материала/продукта Example: 2a69836ab8f583ec11ed90098ae24dff.
        name (str): Название материала/продукта Example: Ананасы.
        unit_id (str): Идентификатор заведения (пиццерии) Example: 2a69836ab8f583ec11ed90098ae24dff.
        category_name (StockItemCategoryName): Категория сырья Example: Ingredient.
        quantity (float): Количество Example: 0.123.
        measurement_unit (MeasurementUnit): Наименование единицы измерения Example: Quantity.
        balance_in_money (float): Остаток в деньгах Example: 10.26.
        currency (str): Валюта Example: RUB.
        avg_weekday_expense (float): Средний расход в будни Example: 0.123.
        avg_weekend_expense (float): Средний расход в выходные Example: 0.123.
        days_until_balance_runs_out (int): На сколько дней хватит запаса Example: 2.
    """

    id: str
    name: str
    unit_id: str
    category_name: StockItemCategoryName
    quantity: float
    measurement_unit: MeasurementUnit
    balance_in_money: float
    currency: str
    avg_weekday_expense: float
    avg_weekend_expense: float
    days_until_balance_runs_out: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        unit_id = self.unit_id

        category_name = self.category_name.value

        quantity = self.quantity

        measurement_unit = self.measurement_unit.value

        balance_in_money = self.balance_in_money

        currency = self.currency

        avg_weekday_expense = self.avg_weekday_expense

        avg_weekend_expense = self.avg_weekend_expense

        days_until_balance_runs_out = self.days_until_balance_runs_out

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "unitId": unit_id,
                "categoryName": category_name,
                "quantity": quantity,
                "measurementUnit": measurement_unit,
                "balanceInMoney": balance_in_money,
                "currency": currency,
                "avgWeekdayExpense": avg_weekday_expense,
                "avgWeekendExpense": avg_weekend_expense,
                "daysUntilBalanceRunsOut": days_until_balance_runs_out,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        unit_id = d.pop("unitId")

        category_name = StockItemCategoryName(d.pop("categoryName"))

        quantity = d.pop("quantity")

        measurement_unit = MeasurementUnit(d.pop("measurementUnit"))

        balance_in_money = d.pop("balanceInMoney")

        currency = d.pop("currency")

        avg_weekday_expense = d.pop("avgWeekdayExpense")

        avg_weekend_expense = d.pop("avgWeekendExpense")

        days_until_balance_runs_out = d.pop("daysUntilBalanceRunsOut")

        inventory_stock_item = cls(
            id=id,
            name=name,
            unit_id=unit_id,
            category_name=category_name,
            quantity=quantity,
            measurement_unit=measurement_unit,
            balance_in_money=balance_in_money,
            currency=currency,
            avg_weekday_expense=avg_weekday_expense,
            avg_weekend_expense=avg_weekend_expense,
            days_until_balance_runs_out=days_until_balance_runs_out,
        )

        inventory_stock_item.additional_properties = d
        return inventory_stock_item

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
