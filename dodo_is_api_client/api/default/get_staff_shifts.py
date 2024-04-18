import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_staff_shifts_response_200 import GetStaffShiftsResponse200
from ...models.get_staff_shifts_staff_type_name import GetStaffShiftsStaffTypeName
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    units: str,
    clock_in_from: datetime.datetime,
    clock_in_to: datetime.date,
    staff_type_name: Union[Unset, GetStaffShiftsStaffTypeName] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["units"] = units

    json_clock_in_from = clock_in_from.isoformat()
    params["clockInFrom"] = json_clock_in_from

    json_clock_in_to = clock_in_to.isoformat()
    params["clockInTo"] = json_clock_in_to

    json_staff_type_name: Union[Unset, str] = UNSET
    if not isinstance(staff_type_name, Unset):
        json_staff_type_name = staff_type_name.value

    params["staffTypeName"] = json_staff_type_name

    params["skip"] = skip

    params["take"] = take

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/staff/shifts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetStaffShiftsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetStaffShiftsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = cast(Any, None)
        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetStaffShiftsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    units: str,
    clock_in_from: datetime.datetime,
    clock_in_to: datetime.date,
    staff_type_name: Union[Unset, GetStaffShiftsStaffTypeName] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
) -> Response[Union[Any, GetStaffShiftsResponse200]]:
    """Команда → Смены сотрудников

     Смены сотрудников (рабочее время, рабочие часы, фактические часы): отработанное время с детализацией
    по дневным, ночным и праздничным часам (в минутах), данные о доставленных заказах, расстоянии, стаже
    сотрудника на момент смены.

    Смены выбираются по времени начала. Также есть фильтр по типу сотрудника. Время смен не обрезается
    по фильтру. Если начало смены попало в диапазон `clockInFrom` – `clockInTo` (отметки времени начала
    смены), то смена вернётся целиком.
    Для получения всех часов по каждому сотруднику нужно выкачать все смены за период и сгруппировать у
    себя по staffId.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        clock_in_from (datetime.datetime):  Example: 2022-01-01T11:00:00.
        clock_in_to (datetime.date):  Example: 2022-01-02.
        staff_type_name (Union[Unset, GetStaffShiftsStaffTypeName]):  Example: KitchenMember.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetStaffShiftsResponse200]]
    """

    kwargs = _get_kwargs(
        units=units,
        clock_in_from=clock_in_from,
        clock_in_to=clock_in_to,
        staff_type_name=staff_type_name,
        skip=skip,
        take=take,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    units: str,
    clock_in_from: datetime.datetime,
    clock_in_to: datetime.date,
    staff_type_name: Union[Unset, GetStaffShiftsStaffTypeName] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
) -> Optional[Union[Any, GetStaffShiftsResponse200]]:
    """Команда → Смены сотрудников

     Смены сотрудников (рабочее время, рабочие часы, фактические часы): отработанное время с детализацией
    по дневным, ночным и праздничным часам (в минутах), данные о доставленных заказах, расстоянии, стаже
    сотрудника на момент смены.

    Смены выбираются по времени начала. Также есть фильтр по типу сотрудника. Время смен не обрезается
    по фильтру. Если начало смены попало в диапазон `clockInFrom` – `clockInTo` (отметки времени начала
    смены), то смена вернётся целиком.
    Для получения всех часов по каждому сотруднику нужно выкачать все смены за период и сгруппировать у
    себя по staffId.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        clock_in_from (datetime.datetime):  Example: 2022-01-01T11:00:00.
        clock_in_to (datetime.date):  Example: 2022-01-02.
        staff_type_name (Union[Unset, GetStaffShiftsStaffTypeName]):  Example: KitchenMember.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetStaffShiftsResponse200]
    """

    return sync_detailed(
        client=client,
        units=units,
        clock_in_from=clock_in_from,
        clock_in_to=clock_in_to,
        staff_type_name=staff_type_name,
        skip=skip,
        take=take,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    units: str,
    clock_in_from: datetime.datetime,
    clock_in_to: datetime.date,
    staff_type_name: Union[Unset, GetStaffShiftsStaffTypeName] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
) -> Response[Union[Any, GetStaffShiftsResponse200]]:
    """Команда → Смены сотрудников

     Смены сотрудников (рабочее время, рабочие часы, фактические часы): отработанное время с детализацией
    по дневным, ночным и праздничным часам (в минутах), данные о доставленных заказах, расстоянии, стаже
    сотрудника на момент смены.

    Смены выбираются по времени начала. Также есть фильтр по типу сотрудника. Время смен не обрезается
    по фильтру. Если начало смены попало в диапазон `clockInFrom` – `clockInTo` (отметки времени начала
    смены), то смена вернётся целиком.
    Для получения всех часов по каждому сотруднику нужно выкачать все смены за период и сгруппировать у
    себя по staffId.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        clock_in_from (datetime.datetime):  Example: 2022-01-01T11:00:00.
        clock_in_to (datetime.date):  Example: 2022-01-02.
        staff_type_name (Union[Unset, GetStaffShiftsStaffTypeName]):  Example: KitchenMember.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetStaffShiftsResponse200]]
    """

    kwargs = _get_kwargs(
        units=units,
        clock_in_from=clock_in_from,
        clock_in_to=clock_in_to,
        staff_type_name=staff_type_name,
        skip=skip,
        take=take,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    units: str,
    clock_in_from: datetime.datetime,
    clock_in_to: datetime.date,
    staff_type_name: Union[Unset, GetStaffShiftsStaffTypeName] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
) -> Optional[Union[Any, GetStaffShiftsResponse200]]:
    """Команда → Смены сотрудников

     Смены сотрудников (рабочее время, рабочие часы, фактические часы): отработанное время с детализацией
    по дневным, ночным и праздничным часам (в минутах), данные о доставленных заказах, расстоянии, стаже
    сотрудника на момент смены.

    Смены выбираются по времени начала. Также есть фильтр по типу сотрудника. Время смен не обрезается
    по фильтру. Если начало смены попало в диапазон `clockInFrom` – `clockInTo` (отметки времени начала
    смены), то смена вернётся целиком.
    Для получения всех часов по каждому сотруднику нужно выкачать все смены за период и сгруппировать у
    себя по staffId.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        clock_in_from (datetime.datetime):  Example: 2022-01-01T11:00:00.
        clock_in_to (datetime.date):  Example: 2022-01-02.
        staff_type_name (Union[Unset, GetStaffShiftsStaffTypeName]):  Example: KitchenMember.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetStaffShiftsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            units=units,
            clock_in_from=clock_in_from,
            clock_in_to=clock_in_to,
            staff_type_name=staff_type_name,
            skip=skip,
            take=take,
        )
    ).parsed
