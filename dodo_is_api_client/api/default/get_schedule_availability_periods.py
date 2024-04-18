import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_contract import ErrorContract
from ...models.error_contract_bad_request import ErrorContractBadRequest
from ...models.get_schedule_availability_periods_response_200 import GetScheduleAvailabilityPeriodsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    units: Union[Unset, str] = UNSET,
    from_: datetime.date,
    to: datetime.date,
    staff_members: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["units"] = units

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to

    params["staffMembers"] = staff_members

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/staff/schedules/availability-periods",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorContract, ErrorContractBadRequest, GetScheduleAvailabilityPeriodsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetScheduleAvailabilityPeriodsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorContractBadRequest.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorContract.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorContract.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorContract, ErrorContractBadRequest, GetScheduleAvailabilityPeriodsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    units: Union[Unset, str] = UNSET,
    from_: datetime.date,
    to: datetime.date,
    staff_members: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorContract, ErrorContractBadRequest, GetScheduleAvailabilityPeriodsResponse200]]:
    """Команда → Карта возможностей

     Получение карты возможностей сотрудников в заведении.

    ### Требования к входным параметрам:
     - В units можно перечислить до 5 заведений в одном запросе;
     - В units следует перечислять UUID-ы строго через запятую без пробелов;
     - В staffMembers ожно перечислить до 30 сотрудников в одном запросе;
     - В staffMembers следует перечислять UUID-ы строго через запятую без пробелов;
     - В запросе необходимо передать один из параметров: `units` или `staffMembers`
     - Максимальный диапазон выборки - 14 дней.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены
    >
    >   `Employee` - Сотрудник. Получение данных **только о самом себе**

    Args:
        units (Union[Unset, str]):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e6
            8aba13f7fc8a,000d3a240c719a8711e68aba13f7fe13.
        from_ (datetime.date):  Example: 2000-01-01.
        to (datetime.date):  Example: 2000-01-02.
        staff_members (Union[Unset, str]):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c71
            9a8711e68aba13f7fc8a,000d3a240c719a8711e68aba13f7fe13.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorContract, ErrorContractBadRequest, GetScheduleAvailabilityPeriodsResponse200]]
    """

    kwargs = _get_kwargs(
        units=units,
        from_=from_,
        to=to,
        staff_members=staff_members,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    units: Union[Unset, str] = UNSET,
    from_: datetime.date,
    to: datetime.date,
    staff_members: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorContract, ErrorContractBadRequest, GetScheduleAvailabilityPeriodsResponse200]]:
    """Команда → Карта возможностей

     Получение карты возможностей сотрудников в заведении.

    ### Требования к входным параметрам:
     - В units можно перечислить до 5 заведений в одном запросе;
     - В units следует перечислять UUID-ы строго через запятую без пробелов;
     - В staffMembers ожно перечислить до 30 сотрудников в одном запросе;
     - В staffMembers следует перечислять UUID-ы строго через запятую без пробелов;
     - В запросе необходимо передать один из параметров: `units` или `staffMembers`
     - Максимальный диапазон выборки - 14 дней.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены
    >
    >   `Employee` - Сотрудник. Получение данных **только о самом себе**

    Args:
        units (Union[Unset, str]):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e6
            8aba13f7fc8a,000d3a240c719a8711e68aba13f7fe13.
        from_ (datetime.date):  Example: 2000-01-01.
        to (datetime.date):  Example: 2000-01-02.
        staff_members (Union[Unset, str]):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c71
            9a8711e68aba13f7fc8a,000d3a240c719a8711e68aba13f7fe13.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorContract, ErrorContractBadRequest, GetScheduleAvailabilityPeriodsResponse200]
    """

    return sync_detailed(
        client=client,
        units=units,
        from_=from_,
        to=to,
        staff_members=staff_members,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    units: Union[Unset, str] = UNSET,
    from_: datetime.date,
    to: datetime.date,
    staff_members: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorContract, ErrorContractBadRequest, GetScheduleAvailabilityPeriodsResponse200]]:
    """Команда → Карта возможностей

     Получение карты возможностей сотрудников в заведении.

    ### Требования к входным параметрам:
     - В units можно перечислить до 5 заведений в одном запросе;
     - В units следует перечислять UUID-ы строго через запятую без пробелов;
     - В staffMembers ожно перечислить до 30 сотрудников в одном запросе;
     - В staffMembers следует перечислять UUID-ы строго через запятую без пробелов;
     - В запросе необходимо передать один из параметров: `units` или `staffMembers`
     - Максимальный диапазон выборки - 14 дней.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены
    >
    >   `Employee` - Сотрудник. Получение данных **только о самом себе**

    Args:
        units (Union[Unset, str]):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e6
            8aba13f7fc8a,000d3a240c719a8711e68aba13f7fe13.
        from_ (datetime.date):  Example: 2000-01-01.
        to (datetime.date):  Example: 2000-01-02.
        staff_members (Union[Unset, str]):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c71
            9a8711e68aba13f7fc8a,000d3a240c719a8711e68aba13f7fe13.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorContract, ErrorContractBadRequest, GetScheduleAvailabilityPeriodsResponse200]]
    """

    kwargs = _get_kwargs(
        units=units,
        from_=from_,
        to=to,
        staff_members=staff_members,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    units: Union[Unset, str] = UNSET,
    from_: datetime.date,
    to: datetime.date,
    staff_members: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorContract, ErrorContractBadRequest, GetScheduleAvailabilityPeriodsResponse200]]:
    """Команда → Карта возможностей

     Получение карты возможностей сотрудников в заведении.

    ### Требования к входным параметрам:
     - В units можно перечислить до 5 заведений в одном запросе;
     - В units следует перечислять UUID-ы строго через запятую без пробелов;
     - В staffMembers ожно перечислить до 30 сотрудников в одном запросе;
     - В staffMembers следует перечислять UUID-ы строго через запятую без пробелов;
     - В запросе необходимо передать один из параметров: `units` или `staffMembers`
     - Максимальный диапазон выборки - 14 дней.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены
    >
    >   `Employee` - Сотрудник. Получение данных **только о самом себе**

    Args:
        units (Union[Unset, str]):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e6
            8aba13f7fc8a,000d3a240c719a8711e68aba13f7fe13.
        from_ (datetime.date):  Example: 2000-01-01.
        to (datetime.date):  Example: 2000-01-02.
        staff_members (Union[Unset, str]):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c71
            9a8711e68aba13f7fc8a,000d3a240c719a8711e68aba13f7fe13.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorContract, ErrorContractBadRequest, GetScheduleAvailabilityPeriodsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            units=units,
            from_=from_,
            to=to,
            staff_members=staff_members,
        )
    ).parsed
