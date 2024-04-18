from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.work_stantion_with_unit_item_work_stantions_item import WorkStantionWithUnitItemWorkStantionsItem


T = TypeVar("T", bound="WorkStantionWithUnitItem")


@_attrs_define
class WorkStantionWithUnitItem:
    """
    Attributes:
        unit_id (Union[Unset, str]): Идентификатор заведения (пиццерии) Example: 2a69836ab8f583ec11ed90098ae24dff.
        work_stantions (Union[Unset, List['WorkStantionWithUnitItemWorkStantionsItem']]):
    """

    unit_id: Union[Unset, str] = UNSET
    work_stantions: Union[Unset, List["WorkStantionWithUnitItemWorkStantionsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_id = self.unit_id

        work_stantions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.work_stantions, Unset):
            work_stantions = []
            for work_stantions_item_data in self.work_stantions:
                work_stantions_item = work_stantions_item_data.to_dict()
                work_stantions.append(work_stantions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit_id is not UNSET:
            field_dict["unitId"] = unit_id
        if work_stantions is not UNSET:
            field_dict["workStantions"] = work_stantions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.work_stantion_with_unit_item_work_stantions_item import WorkStantionWithUnitItemWorkStantionsItem

        d = src_dict.copy()
        unit_id = d.pop("unitId", UNSET)

        work_stantions = []
        _work_stantions = d.pop("workStantions", UNSET)
        for work_stantions_item_data in _work_stantions or []:
            work_stantions_item = WorkStantionWithUnitItemWorkStantionsItem.from_dict(work_stantions_item_data)

            work_stantions.append(work_stantions_item)

        work_stantion_with_unit_item = cls(
            unit_id=unit_id,
            work_stantions=work_stantions,
        )

        work_stantion_with_unit_item.additional_properties = d
        return work_stantion_with_unit_item

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
