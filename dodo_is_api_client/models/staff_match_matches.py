from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StaffMatchMatches")


@_attrs_define
class StaffMatchMatches:
    """
    Attributes:
        is_first_name_matched (Union[Unset, bool]):
        is_last_name_matched (Union[Unset, bool]):
        is_patronymic_name_matched (Union[Unset, bool]):
        is_taxpayer_identification_number_matched (Union[Unset, bool]):
        is_phone_number_matched (Union[Unset, bool]):
        is_date_of_birth_matched (Union[Unset, bool]):
    """

    is_first_name_matched: Union[Unset, bool] = UNSET
    is_last_name_matched: Union[Unset, bool] = UNSET
    is_patronymic_name_matched: Union[Unset, bool] = UNSET
    is_taxpayer_identification_number_matched: Union[Unset, bool] = UNSET
    is_phone_number_matched: Union[Unset, bool] = UNSET
    is_date_of_birth_matched: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_first_name_matched = self.is_first_name_matched

        is_last_name_matched = self.is_last_name_matched

        is_patronymic_name_matched = self.is_patronymic_name_matched

        is_taxpayer_identification_number_matched = self.is_taxpayer_identification_number_matched

        is_phone_number_matched = self.is_phone_number_matched

        is_date_of_birth_matched = self.is_date_of_birth_matched

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_first_name_matched is not UNSET:
            field_dict["isFirstNameMatched"] = is_first_name_matched
        if is_last_name_matched is not UNSET:
            field_dict["isLastNameMatched"] = is_last_name_matched
        if is_patronymic_name_matched is not UNSET:
            field_dict["isPatronymicNameMatched"] = is_patronymic_name_matched
        if is_taxpayer_identification_number_matched is not UNSET:
            field_dict["isTaxpayerIdentificationNumberMatched"] = is_taxpayer_identification_number_matched
        if is_phone_number_matched is not UNSET:
            field_dict["isPhoneNumberMatched"] = is_phone_number_matched
        if is_date_of_birth_matched is not UNSET:
            field_dict["isDateOfBirthMatched"] = is_date_of_birth_matched

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_first_name_matched = d.pop("isFirstNameMatched", UNSET)

        is_last_name_matched = d.pop("isLastNameMatched", UNSET)

        is_patronymic_name_matched = d.pop("isPatronymicNameMatched", UNSET)

        is_taxpayer_identification_number_matched = d.pop("isTaxpayerIdentificationNumberMatched", UNSET)

        is_phone_number_matched = d.pop("isPhoneNumberMatched", UNSET)

        is_date_of_birth_matched = d.pop("isDateOfBirthMatched", UNSET)

        staff_match_matches = cls(
            is_first_name_matched=is_first_name_matched,
            is_last_name_matched=is_last_name_matched,
            is_patronymic_name_matched=is_patronymic_name_matched,
            is_taxpayer_identification_number_matched=is_taxpayer_identification_number_matched,
            is_phone_number_matched=is_phone_number_matched,
            is_date_of_birth_matched=is_date_of_birth_matched,
        )

        staff_match_matches.additional_properties = d
        return staff_match_matches

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
