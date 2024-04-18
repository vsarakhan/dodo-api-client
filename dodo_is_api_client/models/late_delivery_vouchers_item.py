import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.late_delivery_vouchers_item_issuer_name import LateDeliveryVouchersItemIssuerName

T = TypeVar("T", bound="LateDeliveryVouchersItem")


@_attrs_define
class LateDeliveryVouchersItem:
    """
    Attributes:
        order_id (str): Id заказа
        order_number (str): Номер заказа Example: 241.
        order_accepted_at_local (str): Дата и время приёма заказа (локальное время)
        unit_id (str): Id юнита (заведения)
        predicted_delivery_time_local (datetime.datetime): Предполагаемое время доставки (локальное время)
        order_fulfilment_flag_at_local (Union[None, datetime.datetime]): Время отметки курьером в приложении успешной
            доставки (время локальное)
        delivery_deadline_local (datetime.datetime): Крайний срок доставки (локальное время)
        issuer_name (LateDeliveryVouchersItemIssuerName): Кем выдан сертификат Example: System.
        courier_staff_id (Union[None, str]): Id сотрудника-курьера
    """

    order_id: str
    order_number: str
    order_accepted_at_local: str
    unit_id: str
    predicted_delivery_time_local: datetime.datetime
    order_fulfilment_flag_at_local: Union[None, datetime.datetime]
    delivery_deadline_local: datetime.datetime
    issuer_name: LateDeliveryVouchersItemIssuerName
    courier_staff_id: Union[None, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_id = self.order_id

        order_number = self.order_number

        order_accepted_at_local = self.order_accepted_at_local

        unit_id = self.unit_id

        predicted_delivery_time_local = self.predicted_delivery_time_local.isoformat()

        order_fulfilment_flag_at_local: Union[None, str]
        if isinstance(self.order_fulfilment_flag_at_local, datetime.datetime):
            order_fulfilment_flag_at_local = self.order_fulfilment_flag_at_local.isoformat()
        else:
            order_fulfilment_flag_at_local = self.order_fulfilment_flag_at_local

        delivery_deadline_local = self.delivery_deadline_local.isoformat()

        issuer_name = self.issuer_name.value

        courier_staff_id: Union[None, str]
        courier_staff_id = self.courier_staff_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orderId": order_id,
                "orderNumber": order_number,
                "orderAcceptedAtLocal": order_accepted_at_local,
                "unitId": unit_id,
                "predictedDeliveryTimeLocal": predicted_delivery_time_local,
                "orderFulfilmentFlagAtLocal": order_fulfilment_flag_at_local,
                "deliveryDeadlineLocal": delivery_deadline_local,
                "issuerName": issuer_name,
                "courierStaffId": courier_staff_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_id = d.pop("orderId")

        order_number = d.pop("orderNumber")

        order_accepted_at_local = d.pop("orderAcceptedAtLocal")

        unit_id = d.pop("unitId")

        predicted_delivery_time_local = isoparse(d.pop("predictedDeliveryTimeLocal"))

        def _parse_order_fulfilment_flag_at_local(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_fulfilment_flag_at_local_type_0 = isoparse(data)

                return order_fulfilment_flag_at_local_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        order_fulfilment_flag_at_local = _parse_order_fulfilment_flag_at_local(d.pop("orderFulfilmentFlagAtLocal"))

        delivery_deadline_local = isoparse(d.pop("deliveryDeadlineLocal"))

        issuer_name = LateDeliveryVouchersItemIssuerName(d.pop("issuerName"))

        def _parse_courier_staff_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        courier_staff_id = _parse_courier_staff_id(d.pop("courierStaffId"))

        late_delivery_vouchers_item = cls(
            order_id=order_id,
            order_number=order_number,
            order_accepted_at_local=order_accepted_at_local,
            unit_id=unit_id,
            predicted_delivery_time_local=predicted_delivery_time_local,
            order_fulfilment_flag_at_local=order_fulfilment_flag_at_local,
            delivery_deadline_local=delivery_deadline_local,
            issuer_name=issuer_name,
            courier_staff_id=courier_staff_id,
        )

        late_delivery_vouchers_item.additional_properties = d
        return late_delivery_vouchers_item

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
