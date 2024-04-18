from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_product_ids_response_200_ids_item import GetProductIdsResponse200IdsItem


T = TypeVar("T", bound="GetProductIdsResponse200")


@_attrs_define
class GetProductIdsResponse200:
    """
    Attributes:
        is_end_of_list_reached (bool): Индикатор того, что достигнут конец списка. Выдаёт true, если достигнут конец
            списка.
        ids (Union[Unset, List['GetProductIdsResponse200IdsItem']]):
    """

    is_end_of_list_reached: bool
    ids: Union[Unset, List["GetProductIdsResponse200IdsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_end_of_list_reached = self.is_end_of_list_reached

        ids: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = []
            for ids_item_data in self.ids:
                ids_item = ids_item_data.to_dict()
                ids.append(ids_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEndOfListReached": is_end_of_list_reached,
            }
        )
        if ids is not UNSET:
            field_dict["ids"] = ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_product_ids_response_200_ids_item import GetProductIdsResponse200IdsItem

        d = src_dict.copy()
        is_end_of_list_reached = d.pop("isEndOfListReached")

        ids = []
        _ids = d.pop("ids", UNSET)
        for ids_item_data in _ids or []:
            ids_item = GetProductIdsResponse200IdsItem.from_dict(ids_item_data)

            ids.append(ids_item)

        get_product_ids_response_200 = cls(
            is_end_of_list_reached=is_end_of_list_reached,
            ids=ids,
        )

        get_product_ids_response_200.additional_properties = d
        return get_product_ids_response_200

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
