import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_stock_transfers_response_200 import GetStockTransfersResponse200
from ...models.get_stock_transfers_response_400 import GetStockTransfersResponse400
from ...models.get_stock_transfers_statuses import GetStockTransfersStatuses
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    units: str,
    statuses: Union[Unset, GetStockTransfersStatuses] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    shipped_from: Union[Unset, datetime.datetime] = UNSET,
    shipped_to: Union[Unset, datetime.datetime] = UNSET,
    received_from: Union[Unset, datetime.datetime] = UNSET,
    received_to: Union[Unset, datetime.datetime] = UNSET,
    created_from: Union[Unset, datetime.datetime] = UNSET,
    created_to: Union[Unset, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["units"] = units

    json_statuses: Union[Unset, str] = UNSET
    if not isinstance(statuses, Unset):
        json_statuses = statuses.value

    params["statuses"] = json_statuses

    params["skip"] = skip

    params["take"] = take

    json_shipped_from: Union[Unset, str] = UNSET
    if not isinstance(shipped_from, Unset):
        json_shipped_from = shipped_from.isoformat()
    params["shippedFrom"] = json_shipped_from

    json_shipped_to: Union[Unset, str] = UNSET
    if not isinstance(shipped_to, Unset):
        json_shipped_to = shipped_to.isoformat()
    params["shippedTo"] = json_shipped_to

    json_received_from: Union[Unset, str] = UNSET
    if not isinstance(received_from, Unset):
        json_received_from = received_from.isoformat()
    params["receivedFrom"] = json_received_from

    json_received_to: Union[Unset, str] = UNSET
    if not isinstance(received_to, Unset):
        json_received_to = received_to.isoformat()
    params["receivedTo"] = json_received_to

    json_created_from: Union[Unset, str] = UNSET
    if not isinstance(created_from, Unset):
        json_created_from = created_from.isoformat()
    params["createdFrom"] = json_created_from

    json_created_to: Union[Unset, str] = UNSET
    if not isinstance(created_to, Unset):
        json_created_to = created_to.isoformat()
    params["createdTo"] = json_created_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/accounting/stock-transfers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetStockTransfersResponse200, GetStockTransfersResponse400]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetStockTransfersResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetStockTransfersResponse400.from_dict(response.json())

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
) -> Response[Union[Any, GetStockTransfersResponse200, GetStockTransfersResponse400]]:
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
    statuses: Union[Unset, GetStockTransfersStatuses] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    shipped_from: Union[Unset, datetime.datetime] = UNSET,
    shipped_to: Union[Unset, datetime.datetime] = UNSET,
    received_from: Union[Unset, datetime.datetime] = UNSET,
    received_to: Union[Unset, datetime.datetime] = UNSET,
    created_from: Union[Unset, datetime.datetime] = UNSET,
    created_to: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[Any, GetStockTransfersResponse200, GetStockTransfersResponse400]]:
    """Учёт → Перемещения сырья

     Возвращает список перемещений сырья за указанный период (включительно), отсортированный по дате
    создания перемещения.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. `shippedFrom` должен быть меньше `shippedTo`;
    4. `receivedFrom` должен быть меньше `receivedTo`;
    5. `createdFrom` должен быть меньше `createdTo`;
    6. В `statuses` следует перечислять статусы перемещений через запятую без пробелов;

    Статусы перемещений:
    <code>
    Created: 1 (Новая заявка на перемещение)
    Ordered:2 (Заказанная заявка на перемещение)
    Shipped: 3 (Отгруженная заявка на перемещение)
    Received: 4 (Полученная заявка на перемещение)
    Cancelled: 5 (Отмененная заявка на перемещение)
    </code>

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        statuses (Union[Unset, GetStockTransfersStatuses]):  Example: Ordered,Shipped.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        shipped_from (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:21:53.
        shipped_to (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:22:53.
        received_from (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:21:53.
        received_to (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:22:53.
        created_from (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:21:53.
        created_to (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:22:53.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetStockTransfersResponse200, GetStockTransfersResponse400]]
    """

    kwargs = _get_kwargs(
        units=units,
        statuses=statuses,
        skip=skip,
        take=take,
        shipped_from=shipped_from,
        shipped_to=shipped_to,
        received_from=received_from,
        received_to=received_to,
        created_from=created_from,
        created_to=created_to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    units: str,
    statuses: Union[Unset, GetStockTransfersStatuses] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    shipped_from: Union[Unset, datetime.datetime] = UNSET,
    shipped_to: Union[Unset, datetime.datetime] = UNSET,
    received_from: Union[Unset, datetime.datetime] = UNSET,
    received_to: Union[Unset, datetime.datetime] = UNSET,
    created_from: Union[Unset, datetime.datetime] = UNSET,
    created_to: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[Any, GetStockTransfersResponse200, GetStockTransfersResponse400]]:
    """Учёт → Перемещения сырья

     Возвращает список перемещений сырья за указанный период (включительно), отсортированный по дате
    создания перемещения.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. `shippedFrom` должен быть меньше `shippedTo`;
    4. `receivedFrom` должен быть меньше `receivedTo`;
    5. `createdFrom` должен быть меньше `createdTo`;
    6. В `statuses` следует перечислять статусы перемещений через запятую без пробелов;

    Статусы перемещений:
    <code>
    Created: 1 (Новая заявка на перемещение)
    Ordered:2 (Заказанная заявка на перемещение)
    Shipped: 3 (Отгруженная заявка на перемещение)
    Received: 4 (Полученная заявка на перемещение)
    Cancelled: 5 (Отмененная заявка на перемещение)
    </code>

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        statuses (Union[Unset, GetStockTransfersStatuses]):  Example: Ordered,Shipped.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        shipped_from (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:21:53.
        shipped_to (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:22:53.
        received_from (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:21:53.
        received_to (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:22:53.
        created_from (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:21:53.
        created_to (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:22:53.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetStockTransfersResponse200, GetStockTransfersResponse400]
    """

    return sync_detailed(
        client=client,
        units=units,
        statuses=statuses,
        skip=skip,
        take=take,
        shipped_from=shipped_from,
        shipped_to=shipped_to,
        received_from=received_from,
        received_to=received_to,
        created_from=created_from,
        created_to=created_to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    units: str,
    statuses: Union[Unset, GetStockTransfersStatuses] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    shipped_from: Union[Unset, datetime.datetime] = UNSET,
    shipped_to: Union[Unset, datetime.datetime] = UNSET,
    received_from: Union[Unset, datetime.datetime] = UNSET,
    received_to: Union[Unset, datetime.datetime] = UNSET,
    created_from: Union[Unset, datetime.datetime] = UNSET,
    created_to: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[Any, GetStockTransfersResponse200, GetStockTransfersResponse400]]:
    """Учёт → Перемещения сырья

     Возвращает список перемещений сырья за указанный период (включительно), отсортированный по дате
    создания перемещения.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. `shippedFrom` должен быть меньше `shippedTo`;
    4. `receivedFrom` должен быть меньше `receivedTo`;
    5. `createdFrom` должен быть меньше `createdTo`;
    6. В `statuses` следует перечислять статусы перемещений через запятую без пробелов;

    Статусы перемещений:
    <code>
    Created: 1 (Новая заявка на перемещение)
    Ordered:2 (Заказанная заявка на перемещение)
    Shipped: 3 (Отгруженная заявка на перемещение)
    Received: 4 (Полученная заявка на перемещение)
    Cancelled: 5 (Отмененная заявка на перемещение)
    </code>

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        statuses (Union[Unset, GetStockTransfersStatuses]):  Example: Ordered,Shipped.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        shipped_from (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:21:53.
        shipped_to (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:22:53.
        received_from (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:21:53.
        received_to (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:22:53.
        created_from (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:21:53.
        created_to (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:22:53.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetStockTransfersResponse200, GetStockTransfersResponse400]]
    """

    kwargs = _get_kwargs(
        units=units,
        statuses=statuses,
        skip=skip,
        take=take,
        shipped_from=shipped_from,
        shipped_to=shipped_to,
        received_from=received_from,
        received_to=received_to,
        created_from=created_from,
        created_to=created_to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    units: str,
    statuses: Union[Unset, GetStockTransfersStatuses] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    shipped_from: Union[Unset, datetime.datetime] = UNSET,
    shipped_to: Union[Unset, datetime.datetime] = UNSET,
    received_from: Union[Unset, datetime.datetime] = UNSET,
    received_to: Union[Unset, datetime.datetime] = UNSET,
    created_from: Union[Unset, datetime.datetime] = UNSET,
    created_to: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[Any, GetStockTransfersResponse200, GetStockTransfersResponse400]]:
    """Учёт → Перемещения сырья

     Возвращает список перемещений сырья за указанный период (включительно), отсортированный по дате
    создания перемещения.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. `shippedFrom` должен быть меньше `shippedTo`;
    4. `receivedFrom` должен быть меньше `receivedTo`;
    5. `createdFrom` должен быть меньше `createdTo`;
    6. В `statuses` следует перечислять статусы перемещений через запятую без пробелов;

    Статусы перемещений:
    <code>
    Created: 1 (Новая заявка на перемещение)
    Ordered:2 (Заказанная заявка на перемещение)
    Shipped: 3 (Отгруженная заявка на перемещение)
    Received: 4 (Полученная заявка на перемещение)
    Cancelled: 5 (Отмененная заявка на перемещение)
    </code>

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        statuses (Union[Unset, GetStockTransfersStatuses]):  Example: Ordered,Shipped.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        shipped_from (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:21:53.
        shipped_to (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:22:53.
        received_from (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:21:53.
        received_to (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:22:53.
        created_from (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:21:53.
        created_to (Union[Unset, datetime.datetime]):  Example: 2011-09-02T19:22:53.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetStockTransfersResponse200, GetStockTransfersResponse400]
    """

    return (
        await asyncio_detailed(
            client=client,
            units=units,
            statuses=statuses,
            skip=skip,
            take=take,
            shipped_from=shipped_from,
            shipped_to=shipped_to,
            received_from=received_from,
            received_to=received_to,
            created_from=created_from,
            created_to=created_to,
        )
    ).parsed
