import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_stock_items_response_200 import GetStockItemsResponse200
from ...models.get_stock_items_response_400 import GetStockItemsResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    modified_at: Union[Unset, datetime.datetime] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_modified_at: Union[Unset, str] = UNSET
    if not isinstance(modified_at, Unset):
        json_modified_at = modified_at.isoformat()
    params["modifiedAt"] = json_modified_at

    params["skip"] = skip

    params["take"] = take

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/accounting/stock-items",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetStockItemsResponse200, GetStockItemsResponse400]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetStockItemsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetStockItemsResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetStockItemsResponse200, GetStockItemsResponse400]]:
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
) -> Response[Union[Any, GetStockItemsResponse200, GetStockItemsResponse400]]:
    """Учёт → Сырьё

     Возвращает список сырья, отсортированный по ID.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    Args:
        modified_at (Union[Unset, datetime.datetime]):  Example: 2022-10-01T08:00:00.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetStockItemsResponse200, GetStockItemsResponse400]]
    """

    kwargs = _get_kwargs(
        modified_at=modified_at,
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
    modified_at: Union[Unset, datetime.datetime] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
) -> Optional[Union[Any, GetStockItemsResponse200, GetStockItemsResponse400]]:
    """Учёт → Сырьё

     Возвращает список сырья, отсортированный по ID.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    Args:
        modified_at (Union[Unset, datetime.datetime]):  Example: 2022-10-01T08:00:00.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetStockItemsResponse200, GetStockItemsResponse400]
    """

    return sync_detailed(
        client=client,
        modified_at=modified_at,
        skip=skip,
        take=take,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    modified_at: Union[Unset, datetime.datetime] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
) -> Response[Union[Any, GetStockItemsResponse200, GetStockItemsResponse400]]:
    """Учёт → Сырьё

     Возвращает список сырья, отсортированный по ID.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    Args:
        modified_at (Union[Unset, datetime.datetime]):  Example: 2022-10-01T08:00:00.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetStockItemsResponse200, GetStockItemsResponse400]]
    """

    kwargs = _get_kwargs(
        modified_at=modified_at,
        skip=skip,
        take=take,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    modified_at: Union[Unset, datetime.datetime] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
) -> Optional[Union[Any, GetStockItemsResponse200, GetStockItemsResponse400]]:
    """Учёт → Сырьё

     Возвращает список сырья, отсортированный по ID.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    Args:
        modified_at (Union[Unset, datetime.datetime]):  Example: 2022-10-01T08:00:00.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetStockItemsResponse200, GetStockItemsResponse400]
    """

    return (
        await asyncio_detailed(
            client=client,
            modified_at=modified_at,
            skip=skip,
            take=take,
        )
    ).parsed
