import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sales_order_source import GetSalesOrderSource
from ...models.get_sales_response_200 import GetSalesResponse200
from ...models.get_sales_response_400 import GetSalesResponse400
from ...models.get_sales_sales_channel import GetSalesSalesChannel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    units: str,
    from_: datetime.datetime,
    to: datetime.datetime,
    sales_channel: Union[Unset, GetSalesSalesChannel] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    order_source: Union[Unset, GetSalesOrderSource] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["units"] = units

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to

    json_sales_channel: Union[Unset, str] = UNSET
    if not isinstance(sales_channel, Unset):
        json_sales_channel = sales_channel.value

    params["salesChannel"] = json_sales_channel

    params["skip"] = skip

    params["take"] = take

    json_order_source: Union[Unset, str] = UNSET
    if not isinstance(order_source, Unset):
        json_order_source = order_source.value

    params["orderSource"] = json_order_source

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/accounting/sales",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetSalesResponse200, GetSalesResponse400]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetSalesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetSalesResponse400.from_dict(response.json())

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
) -> Response[Union[Any, GetSalesResponse200, GetSalesResponse400]]:
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
    from_: datetime.datetime,
    to: datetime.datetime,
    sales_channel: Union[Unset, GetSalesSalesChannel] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    order_source: Union[Unset, GetSalesOrderSource] = UNSET,
) -> Response[Union[Any, GetSalesResponse200, GetSalesResponse400]]:
    """Учёт → Продажи

     Возвращает продажи за указанный период (включительно), отсортированные по дате и идентификатору
    продажи.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. `from` должен быть меньше, чем `to`;
    4. Диапазон дат между `to` и `from` параметрами не должен превышать 31 день.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        from_ (datetime.datetime):  Example: 2011-08-01T18:31:42.
        to (datetime.datetime):  Example: 2011-09-02T19:21:53.
        sales_channel (Union[Unset, GetSalesSalesChannel]):
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        order_source (Union[Unset, GetSalesOrderSource]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetSalesResponse200, GetSalesResponse400]]
    """

    kwargs = _get_kwargs(
        units=units,
        from_=from_,
        to=to,
        sales_channel=sales_channel,
        skip=skip,
        take=take,
        order_source=order_source,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    units: str,
    from_: datetime.datetime,
    to: datetime.datetime,
    sales_channel: Union[Unset, GetSalesSalesChannel] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    order_source: Union[Unset, GetSalesOrderSource] = UNSET,
) -> Optional[Union[Any, GetSalesResponse200, GetSalesResponse400]]:
    """Учёт → Продажи

     Возвращает продажи за указанный период (включительно), отсортированные по дате и идентификатору
    продажи.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. `from` должен быть меньше, чем `to`;
    4. Диапазон дат между `to` и `from` параметрами не должен превышать 31 день.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        from_ (datetime.datetime):  Example: 2011-08-01T18:31:42.
        to (datetime.datetime):  Example: 2011-09-02T19:21:53.
        sales_channel (Union[Unset, GetSalesSalesChannel]):
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        order_source (Union[Unset, GetSalesOrderSource]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetSalesResponse200, GetSalesResponse400]
    """

    return sync_detailed(
        client=client,
        units=units,
        from_=from_,
        to=to,
        sales_channel=sales_channel,
        skip=skip,
        take=take,
        order_source=order_source,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    units: str,
    from_: datetime.datetime,
    to: datetime.datetime,
    sales_channel: Union[Unset, GetSalesSalesChannel] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    order_source: Union[Unset, GetSalesOrderSource] = UNSET,
) -> Response[Union[Any, GetSalesResponse200, GetSalesResponse400]]:
    """Учёт → Продажи

     Возвращает продажи за указанный период (включительно), отсортированные по дате и идентификатору
    продажи.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. `from` должен быть меньше, чем `to`;
    4. Диапазон дат между `to` и `from` параметрами не должен превышать 31 день.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        from_ (datetime.datetime):  Example: 2011-08-01T18:31:42.
        to (datetime.datetime):  Example: 2011-09-02T19:21:53.
        sales_channel (Union[Unset, GetSalesSalesChannel]):
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        order_source (Union[Unset, GetSalesOrderSource]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetSalesResponse200, GetSalesResponse400]]
    """

    kwargs = _get_kwargs(
        units=units,
        from_=from_,
        to=to,
        sales_channel=sales_channel,
        skip=skip,
        take=take,
        order_source=order_source,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    units: str,
    from_: datetime.datetime,
    to: datetime.datetime,
    sales_channel: Union[Unset, GetSalesSalesChannel] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    order_source: Union[Unset, GetSalesOrderSource] = UNSET,
) -> Optional[Union[Any, GetSalesResponse200, GetSalesResponse400]]:
    """Учёт → Продажи

     Возвращает продажи за указанный период (включительно), отсортированные по дате и идентификатору
    продажи.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. `from` должен быть меньше, чем `to`;
    4. Диапазон дат между `to` и `from` параметрами не должен превышать 31 день.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        from_ (datetime.datetime):  Example: 2011-08-01T18:31:42.
        to (datetime.datetime):  Example: 2011-09-02T19:21:53.
        sales_channel (Union[Unset, GetSalesSalesChannel]):
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        order_source (Union[Unset, GetSalesOrderSource]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetSalesResponse200, GetSalesResponse400]
    """

    return (
        await asyncio_detailed(
            client=client,
            units=units,
            from_=from_,
            to=to,
            sales_channel=sales_channel,
            skip=skip,
            take=take,
            order_source=order_source,
        )
    ).parsed
