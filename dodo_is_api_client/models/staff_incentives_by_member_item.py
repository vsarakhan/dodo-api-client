from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.premium import Premium
    from ..models.staff_incentives_shifts_detalization_item import StaffIncentivesShiftsDetalizationItem


T = TypeVar("T", bound="StaffIncentivesByMemberItem")


@_attrs_define
class StaffIncentivesByMemberItem:
    """
    Attributes:
        staff_id (str): Идентификатор сотрудника
        phone_number (str): Номер телефона сотрудника
        taxpayer_identification_number (Union[None, str]): Код налогоплательщика сотрудника (для РФ - ИНН) Example:
            2524366131.
        shifts_detalization (List['StaffIncentivesShiftsDetalizationItem']): Детализация вознаграждений по сменам
        premiums (List['Premium']): Премии, назначенные вне смен (через Менеджер Офиса)
        total_incentives (float): Итоговое вознагражление для сотрудника за период
    """

    staff_id: str
    phone_number: str
    taxpayer_identification_number: Union[None, str]
    shifts_detalization: List["StaffIncentivesShiftsDetalizationItem"]
    premiums: List["Premium"]
    total_incentives: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        staff_id = self.staff_id

        phone_number = self.phone_number

        taxpayer_identification_number: Union[None, str]
        taxpayer_identification_number = self.taxpayer_identification_number

        shifts_detalization = []
        for shifts_detalization_item_data in self.shifts_detalization:
            shifts_detalization_item = shifts_detalization_item_data.to_dict()
            shifts_detalization.append(shifts_detalization_item)

        premiums = []
        for premiums_item_data in self.premiums:
            premiums_item = premiums_item_data.to_dict()
            premiums.append(premiums_item)

        total_incentives = self.total_incentives

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "staffId": staff_id,
                "phoneNumber": phone_number,
                "taxpayerIdentificationNumber": taxpayer_identification_number,
                "shiftsDetalization": shifts_detalization,
                "premiums": premiums,
                "totalIncentives": total_incentives,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.premium import Premium
        from ..models.staff_incentives_shifts_detalization_item import StaffIncentivesShiftsDetalizationItem

        d = src_dict.copy()
        staff_id = d.pop("staffId")

        phone_number = d.pop("phoneNumber")

        def _parse_taxpayer_identification_number(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        taxpayer_identification_number = _parse_taxpayer_identification_number(d.pop("taxpayerIdentificationNumber"))

        shifts_detalization = []
        _shifts_detalization = d.pop("shiftsDetalization")
        for shifts_detalization_item_data in _shifts_detalization:
            shifts_detalization_item = StaffIncentivesShiftsDetalizationItem.from_dict(shifts_detalization_item_data)

            shifts_detalization.append(shifts_detalization_item)

        premiums = []
        _premiums = d.pop("premiums")
        for premiums_item_data in _premiums:
            premiums_item = Premium.from_dict(premiums_item_data)

            premiums.append(premiums_item)

        total_incentives = d.pop("totalIncentives")

        staff_incentives_by_member_item = cls(
            staff_id=staff_id,
            phone_number=phone_number,
            taxpayer_identification_number=taxpayer_identification_number,
            shifts_detalization=shifts_detalization,
            premiums=premiums,
            total_incentives=total_incentives,
        )

        staff_incentives_by_member_item.additional_properties = d
        return staff_incentives_by_member_item

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
