import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_production_ordershandovertime_response_200 import GetProductionOrdershandovertimeResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    units: str,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["units"] = units

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/production/orders-handover-time",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetProductionOrdershandovertimeResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetProductionOrdershandovertimeResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
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
) -> Response[Union[Any, GetProductionOrdershandovertimeResponse200]]:
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
) -> Response[Union[Any, GetProductionOrdershandovertimeResponse200]]:
    """Производство → Время выдачи заказа

     Возвращает время выдачи заказов за выбранный период по пиццериям (`units`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. Диапазон дат между `to` и `from` параметрами не должен превышать 31 день.

    ### Округление до целых секунд:
    Длительность событий (например, `cookingTime`) представлена целыми числами и округляется до целых
    секунд.
    0.5 и больше секунд округляется вверх, 0.4 и меньше - вниз.

    ### Исключенные данные:
    Напитки и неприготовляемые продукты исключаются из выборки.
    В расчет не попадают заказы с временем приготовления выпекаемых продуктов меньше 1 минуты, заказы
    без выпекаемых продуктов (кусочки, напитки, фонданы и т.д.) и заказы с временем выдачи больше 1
    часа.

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetProductionOrdershandovertimeResponse200]]
    """

    kwargs = _get_kwargs(
        units=units,
        from_=from_,
        to=to,
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
) -> Optional[Union[Any, GetProductionOrdershandovertimeResponse200]]:
    """Производство → Время выдачи заказа

     Возвращает время выдачи заказов за выбранный период по пиццериям (`units`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. Диапазон дат между `to` и `from` параметрами не должен превышать 31 день.

    ### Округление до целых секунд:
    Длительность событий (например, `cookingTime`) представлена целыми числами и округляется до целых
    секунд.
    0.5 и больше секунд округляется вверх, 0.4 и меньше - вниз.

    ### Исключенные данные:
    Напитки и неприготовляемые продукты исключаются из выборки.
    В расчет не попадают заказы с временем приготовления выпекаемых продуктов меньше 1 минуты, заказы
    без выпекаемых продуктов (кусочки, напитки, фонданы и т.д.) и заказы с временем выдачи больше 1
    часа.

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetProductionOrdershandovertimeResponse200]
    """

    return sync_detailed(
        client=client,
        units=units,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    units: str,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> Response[Union[Any, GetProductionOrdershandovertimeResponse200]]:
    """Производство → Время выдачи заказа

     Возвращает время выдачи заказов за выбранный период по пиццериям (`units`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. Диапазон дат между `to` и `from` параметрами не должен превышать 31 день.

    ### Округление до целых секунд:
    Длительность событий (например, `cookingTime`) представлена целыми числами и округляется до целых
    секунд.
    0.5 и больше секунд округляется вверх, 0.4 и меньше - вниз.

    ### Исключенные данные:
    Напитки и неприготовляемые продукты исключаются из выборки.
    В расчет не попадают заказы с временем приготовления выпекаемых продуктов меньше 1 минуты, заказы
    без выпекаемых продуктов (кусочки, напитки, фонданы и т.д.) и заказы с временем выдачи больше 1
    часа.

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetProductionOrdershandovertimeResponse200]]
    """

    kwargs = _get_kwargs(
        units=units,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    units: str,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> Optional[Union[Any, GetProductionOrdershandovertimeResponse200]]:
    """Производство → Время выдачи заказа

     Возвращает время выдачи заказов за выбранный период по пиццериям (`units`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. Диапазон дат между `to` и `from` параметрами не должен превышать 31 день.

    ### Округление до целых секунд:
    Длительность событий (например, `cookingTime`) представлена целыми числами и округляется до целых
    секунд.
    0.5 и больше секунд округляется вверх, 0.4 и меньше - вниз.

    ### Исключенные данные:
    Напитки и неприготовляемые продукты исключаются из выборки.
    В расчет не попадают заказы с временем приготовления выпекаемых продуктов меньше 1 минуты, заказы
    без выпекаемых продуктов (кусочки, напитки, фонданы и т.д.) и заказы с временем выдачи больше 1
    часа.

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetProductionOrdershandovertimeResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            units=units,
            from_=from_,
            to=to,
        )
    ).parsed
