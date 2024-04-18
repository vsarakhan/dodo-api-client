import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_staff_schedules_response_200 import GetStaffSchedulesResponse200
from ...models.get_staff_schedules_staff_type import GetStaffSchedulesStaffType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    begin_from: datetime.datetime,
    begin_to: datetime.datetime,
    units: str,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    staff_type: Union[Unset, GetStaffSchedulesStaffType] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_begin_from = begin_from.isoformat()
    params["beginFrom"] = json_begin_from

    json_begin_to = begin_to.isoformat()
    params["beginTo"] = json_begin_to

    params["units"] = units

    params["skip"] = skip

    params["take"] = take

    json_staff_type: Union[Unset, str] = UNSET
    if not isinstance(staff_type, Unset):
        json_staff_type = staff_type.value

    params["staffType"] = json_staff_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/staff/schedules",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetStaffSchedulesResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetStaffSchedulesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetStaffSchedulesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    begin_from: datetime.datetime,
    begin_to: datetime.datetime,
    units: str,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    staff_type: Union[Unset, GetStaffSchedulesStaffType] = UNSET,
) -> Response[Union[Any, GetStaffSchedulesResponse200]]:
    """Команда → Расписания

     Расписания смен сотрудников

    Период выборки учитывает только начало смены в расписании, то есть конец смены может выходить за
    пределы периода выборки.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены

    Args:
        begin_from (datetime.datetime):  Example: 2022-01-01T11:00:00.
        begin_to (datetime.datetime):  Example: 2022-01-01T12:00:00.
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        staff_type (Union[Unset, GetStaffSchedulesStaffType]):  Example: KitchenMember.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetStaffSchedulesResponse200]]
    """

    kwargs = _get_kwargs(
        begin_from=begin_from,
        begin_to=begin_to,
        units=units,
        skip=skip,
        take=take,
        staff_type=staff_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    begin_from: datetime.datetime,
    begin_to: datetime.datetime,
    units: str,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    staff_type: Union[Unset, GetStaffSchedulesStaffType] = UNSET,
) -> Optional[Union[Any, GetStaffSchedulesResponse200]]:
    """Команда → Расписания

     Расписания смен сотрудников

    Период выборки учитывает только начало смены в расписании, то есть конец смены может выходить за
    пределы периода выборки.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены

    Args:
        begin_from (datetime.datetime):  Example: 2022-01-01T11:00:00.
        begin_to (datetime.datetime):  Example: 2022-01-01T12:00:00.
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        staff_type (Union[Unset, GetStaffSchedulesStaffType]):  Example: KitchenMember.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetStaffSchedulesResponse200]
    """

    return sync_detailed(
        client=client,
        begin_from=begin_from,
        begin_to=begin_to,
        units=units,
        skip=skip,
        take=take,
        staff_type=staff_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    begin_from: datetime.datetime,
    begin_to: datetime.datetime,
    units: str,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    staff_type: Union[Unset, GetStaffSchedulesStaffType] = UNSET,
) -> Response[Union[Any, GetStaffSchedulesResponse200]]:
    """Команда → Расписания

     Расписания смен сотрудников

    Период выборки учитывает только начало смены в расписании, то есть конец смены может выходить за
    пределы периода выборки.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены

    Args:
        begin_from (datetime.datetime):  Example: 2022-01-01T11:00:00.
        begin_to (datetime.datetime):  Example: 2022-01-01T12:00:00.
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        staff_type (Union[Unset, GetStaffSchedulesStaffType]):  Example: KitchenMember.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetStaffSchedulesResponse200]]
    """

    kwargs = _get_kwargs(
        begin_from=begin_from,
        begin_to=begin_to,
        units=units,
        skip=skip,
        take=take,
        staff_type=staff_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    begin_from: datetime.datetime,
    begin_to: datetime.datetime,
    units: str,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    staff_type: Union[Unset, GetStaffSchedulesStaffType] = UNSET,
) -> Optional[Union[Any, GetStaffSchedulesResponse200]]:
    """Команда → Расписания

     Расписания смен сотрудников

    Период выборки учитывает только начало смены в расписании, то есть конец смены может выходить за
    пределы периода выборки.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены

    Args:
        begin_from (datetime.datetime):  Example: 2022-01-01T11:00:00.
        begin_to (datetime.datetime):  Example: 2022-01-01T12:00:00.
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        staff_type (Union[Unset, GetStaffSchedulesStaffType]):  Example: KitchenMember.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetStaffSchedulesResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            begin_from=begin_from,
            begin_to=begin_to,
            units=units,
            skip=skip,
            take=take,
            staff_type=staff_type,
        )
    ).parsed
