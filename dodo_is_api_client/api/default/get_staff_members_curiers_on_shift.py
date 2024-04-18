import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_contract import ErrorContract
from ...models.error_contract_bad_request import ErrorContractBadRequest
from ...models.get_staff_members_curiers_on_shift_response_200 import GetStaffMembersCuriersOnShiftResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    units: str,
    on: Union[Unset, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["units"] = units

    json_on: Union[Unset, str] = UNSET
    if not isinstance(on, Unset):
        json_on = on.isoformat()
    params["on"] = json_on

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/staff/couriers-on-shift",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorContract, ErrorContractBadRequest, GetStaffMembersCuriersOnShiftResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetStaffMembersCuriersOnShiftResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorContractBadRequest.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
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
) -> Response[Union[Any, ErrorContract, ErrorContractBadRequest, GetStaffMembersCuriersOnShiftResponse200]]:
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
    on: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[Any, ErrorContract, ErrorContractBadRequest, GetStaffMembersCuriersOnShiftResponse200]]:
    """Команда → Курьеры на смене

     Возвращает список курьеров на смене на момент отправки запроса.

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. Дата `on` должна быть в прошлом.

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
        on (Union[Unset, datetime.datetime]):  Example: 2000-01-01T00:00:00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorContract, ErrorContractBadRequest, GetStaffMembersCuriersOnShiftResponse200]]
    """

    kwargs = _get_kwargs(
        units=units,
        on=on,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    units: str,
    on: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[Any, ErrorContract, ErrorContractBadRequest, GetStaffMembersCuriersOnShiftResponse200]]:
    """Команда → Курьеры на смене

     Возвращает список курьеров на смене на момент отправки запроса.

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. Дата `on` должна быть в прошлом.

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
        on (Union[Unset, datetime.datetime]):  Example: 2000-01-01T00:00:00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorContract, ErrorContractBadRequest, GetStaffMembersCuriersOnShiftResponse200]
    """

    return sync_detailed(
        client=client,
        units=units,
        on=on,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    units: str,
    on: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[Any, ErrorContract, ErrorContractBadRequest, GetStaffMembersCuriersOnShiftResponse200]]:
    """Команда → Курьеры на смене

     Возвращает список курьеров на смене на момент отправки запроса.

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. Дата `on` должна быть в прошлом.

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
        on (Union[Unset, datetime.datetime]):  Example: 2000-01-01T00:00:00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorContract, ErrorContractBadRequest, GetStaffMembersCuriersOnShiftResponse200]]
    """

    kwargs = _get_kwargs(
        units=units,
        on=on,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    units: str,
    on: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[Any, ErrorContract, ErrorContractBadRequest, GetStaffMembersCuriersOnShiftResponse200]]:
    """Команда → Курьеры на смене

     Возвращает список курьеров на смене на момент отправки запроса.

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. Дата `on` должна быть в прошлом.

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
        on (Union[Unset, datetime.datetime]):  Example: 2000-01-01T00:00:00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorContract, ErrorContractBadRequest, GetStaffMembersCuriersOnShiftResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            units=units,
            on=on,
        )
    ).parsed
