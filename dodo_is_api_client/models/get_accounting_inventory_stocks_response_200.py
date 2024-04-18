import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.inventory_stock_item import InventoryStockItem


T = TypeVar("T", bound="GetAccountingInventoryStocksResponse200")


@_attrs_define
class GetAccountingInventoryStocksResponse200:
    """
    Attributes:
        stocks (List['InventoryStockItem']):
        calculation_date (datetime.datetime): Дата просчета остатков Example: 2000-01-01T12:00:00.
    """

    stocks: List["InventoryStockItem"]
    calculation_date: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stocks = []
        for stocks_item_data in self.stocks:
            stocks_item = stocks_item_data.to_dict()
            stocks.append(stocks_item)

        calculation_date = self.calculation_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stocks": stocks,
                "calculationDate": calculation_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inventory_stock_item import InventoryStockItem

        d = src_dict.copy()
        stocks = []
        _stocks = d.pop("stocks")
        for stocks_item_data in _stocks:
            stocks_item = InventoryStockItem.from_dict(stocks_item_data)

            stocks.append(stocks_item)

        calculation_date = isoparse(d.pop("calculationDate"))

        get_accounting_inventory_stocks_response_200 = cls(
            stocks=stocks,
            calculation_date=calculation_date,
        )

        get_accounting_inventory_stocks_response_200.additional_properties = d
        return get_accounting_inventory_stocks_response_200

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
