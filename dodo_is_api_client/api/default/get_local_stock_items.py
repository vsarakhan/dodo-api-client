import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_local_stock_items_response_200 import GetLocalStockItemsResponse200
from ...models.get_local_stock_items_response_400 import GetLocalStockItemsResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    modified_at: Union[Unset, datetime.datetime] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    units: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_modified_at: Union[Unset, str] = UNSET
    if not isinstance(modified_at, Unset):
        json_modified_at = modified_at.isoformat()
    params["modifiedAt"] = json_modified_at

    params["skip"] = skip

    params["take"] = take

    params["units"] = units

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/accounting/local-stock-items",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetLocalStockItemsResponse200, GetLocalStockItemsResponse400]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetLocalStockItemsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetLocalStockItemsResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetLocalStockItemsResponse200, GetLocalStockItemsResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    modified_at: Union[Unset, datetime.datetime] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    units: str,
) -> Response[Union[Any, GetLocalStockItemsResponse200, GetLocalStockItemsResponse400]]:
    """Учёт → Локальное сырьё

     Возвращает список локального сырья, отсортированный по ID.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;

    Args:
        modified_at (Union[Unset, datetime.datetime]):  Example: 2022-10-01T08:00:00.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetLocalStockItemsResponse200, GetLocalStockItemsResponse400]]
    """

    kwargs = _get_kwargs(
        modified_at=modified_at,
        skip=skip,
        take=take,
        units=units,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    modified_at: Union[Unset, datetime.datetime] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    units: str,
) -> Optional[Union[Any, GetLocalStockItemsResponse200, GetLocalStockItemsResponse400]]:
    """Учёт → Локальное сырьё

     Возвращает список локального сырья, отсортированный по ID.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;

    Args:
        modified_at (Union[Unset, datetime.datetime]):  Example: 2022-10-01T08:00:00.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetLocalStockItemsResponse200, GetLocalStockItemsResponse400]
    """

    return sync_detailed(
        client=client,
        modified_at=modified_at,
        skip=skip,
        take=take,
        units=units,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    modified_at: Union[Unset, datetime.datetime] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    units: str,
) -> Response[Union[Any, GetLocalStockItemsResponse200, GetLocalStockItemsResponse400]]:
    """Учёт → Локальное сырьё

     Возвращает список локального сырья, отсортированный по ID.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;

    Args:
        modified_at (Union[Unset, datetime.datetime]):  Example: 2022-10-01T08:00:00.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetLocalStockItemsResponse200, GetLocalStockItemsResponse400]]
    """

    kwargs = _get_kwargs(
        modified_at=modified_at,
        skip=skip,
        take=take,
        units=units,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    modified_at: Union[Unset, datetime.datetime] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    units: str,
) -> Optional[Union[Any, GetLocalStockItemsResponse200, GetLocalStockItemsResponse400]]:
    """Учёт → Локальное сырьё

     Возвращает список локального сырья, отсортированный по ID.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;

    Args:
        modified_at (Union[Unset, datetime.datetime]):  Example: 2022-10-01T08:00:00.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetLocalStockItemsResponse200, GetLocalStockItemsResponse400]
    """

    return (
        await asyncio_detailed(
            client=client,
            modified_at=modified_at,
            skip=skip,
            take=take,
            units=units,
        )
    ).parsed
