import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_production_orders_handover_time_statistics_response_200 import (
    GetProductionOrdersHandoverTimeStatisticsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    units: str,
    from_: datetime.datetime,
    to: datetime.datetime,
    sales_channels: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["units"] = units

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to

    params["salesChannels"] = sales_channels

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/production/orders-handover-statistics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetProductionOrdersHandoverTimeStatisticsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetProductionOrdersHandoverTimeStatisticsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetProductionOrdersHandoverTimeStatisticsResponse200]]:
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
    sales_channels: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetProductionOrdersHandoverTimeStatisticsResponse200]]:
    """Производство → Статистика выдачи заказов

     Возвращает агрегированные данные по выдаче заказов за выбранный период по пиццериям (`units`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    1. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    1. В `salesChannels` следует перечислять каналы продаж (Delivery,DineIn,TakeAway) строго через
    запятую без пробелов;
    1. Диапазон дат между `to` и `from` параметрами не должен превышать 31 день.

    ### Округление до целых секунд:
    Длительность событий (например, `avgCookingTime`) представлена целыми числами и округляется до целых
    секунд.
    0.5 и больше секунд округляется вверх, 0.4 и меньше - вниз.

    ### Исключенные данные:
    Напитки и неприготовляемые продукты исключаются из выборки.
    В расчет не попадают заказы с временем приготовления выпекаемых продуктов меньше 1 минуты, заказы
    без выпекаемых продуктов (кусочки, напитки, фонданы и т.д.) и заказы с временем выдачи больше 1
    часа.

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        from_ (datetime.datetime):  Example: 2011-08-01T18:31:42.
        to (datetime.datetime):  Example: 2011-09-02T19:21:53.
        sales_channels (Union[Unset, str]):  Example: Delivery,DineIn,TakeAway.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetProductionOrdersHandoverTimeStatisticsResponse200]]
    """

    kwargs = _get_kwargs(
        units=units,
        from_=from_,
        to=to,
        sales_channels=sales_channels,
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
    sales_channels: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetProductionOrdersHandoverTimeStatisticsResponse200]]:
    """Производство → Статистика выдачи заказов

     Возвращает агрегированные данные по выдаче заказов за выбранный период по пиццериям (`units`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    1. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    1. В `salesChannels` следует перечислять каналы продаж (Delivery,DineIn,TakeAway) строго через
    запятую без пробелов;
    1. Диапазон дат между `to` и `from` параметрами не должен превышать 31 день.

    ### Округление до целых секунд:
    Длительность событий (например, `avgCookingTime`) представлена целыми числами и округляется до целых
    секунд.
    0.5 и больше секунд округляется вверх, 0.4 и меньше - вниз.

    ### Исключенные данные:
    Напитки и неприготовляемые продукты исключаются из выборки.
    В расчет не попадают заказы с временем приготовления выпекаемых продуктов меньше 1 минуты, заказы
    без выпекаемых продуктов (кусочки, напитки, фонданы и т.д.) и заказы с временем выдачи больше 1
    часа.

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        from_ (datetime.datetime):  Example: 2011-08-01T18:31:42.
        to (datetime.datetime):  Example: 2011-09-02T19:21:53.
        sales_channels (Union[Unset, str]):  Example: Delivery,DineIn,TakeAway.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetProductionOrdersHandoverTimeStatisticsResponse200]
    """

    return sync_detailed(
        client=client,
        units=units,
        from_=from_,
        to=to,
        sales_channels=sales_channels,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    units: str,
    from_: datetime.datetime,
    to: datetime.datetime,
    sales_channels: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetProductionOrdersHandoverTimeStatisticsResponse200]]:
    """Производство → Статистика выдачи заказов

     Возвращает агрегированные данные по выдаче заказов за выбранный период по пиццериям (`units`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    1. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    1. В `salesChannels` следует перечислять каналы продаж (Delivery,DineIn,TakeAway) строго через
    запятую без пробелов;
    1. Диапазон дат между `to` и `from` параметрами не должен превышать 31 день.

    ### Округление до целых секунд:
    Длительность событий (например, `avgCookingTime`) представлена целыми числами и округляется до целых
    секунд.
    0.5 и больше секунд округляется вверх, 0.4 и меньше - вниз.

    ### Исключенные данные:
    Напитки и неприготовляемые продукты исключаются из выборки.
    В расчет не попадают заказы с временем приготовления выпекаемых продуктов меньше 1 минуты, заказы
    без выпекаемых продуктов (кусочки, напитки, фонданы и т.д.) и заказы с временем выдачи больше 1
    часа.

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        from_ (datetime.datetime):  Example: 2011-08-01T18:31:42.
        to (datetime.datetime):  Example: 2011-09-02T19:21:53.
        sales_channels (Union[Unset, str]):  Example: Delivery,DineIn,TakeAway.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetProductionOrdersHandoverTimeStatisticsResponse200]]
    """

    kwargs = _get_kwargs(
        units=units,
        from_=from_,
        to=to,
        sales_channels=sales_channels,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    units: str,
    from_: datetime.datetime,
    to: datetime.datetime,
    sales_channels: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetProductionOrdersHandoverTimeStatisticsResponse200]]:
    """Производство → Статистика выдачи заказов

     Возвращает агрегированные данные по выдаче заказов за выбранный период по пиццериям (`units`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    1. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    1. В `salesChannels` следует перечислять каналы продаж (Delivery,DineIn,TakeAway) строго через
    запятую без пробелов;
    1. Диапазон дат между `to` и `from` параметрами не должен превышать 31 день.

    ### Округление до целых секунд:
    Длительность событий (например, `avgCookingTime`) представлена целыми числами и округляется до целых
    секунд.
    0.5 и больше секунд округляется вверх, 0.4 и меньше - вниз.

    ### Исключенные данные:
    Напитки и неприготовляемые продукты исключаются из выборки.
    В расчет не попадают заказы с временем приготовления выпекаемых продуктов меньше 1 минуты, заказы
    без выпекаемых продуктов (кусочки, напитки, фонданы и т.д.) и заказы с временем выдачи больше 1
    часа.

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        from_ (datetime.datetime):  Example: 2011-08-01T18:31:42.
        to (datetime.datetime):  Example: 2011-09-02T19:21:53.
        sales_channels (Union[Unset, str]):  Example: Delivery,DineIn,TakeAway.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetProductionOrdersHandoverTimeStatisticsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            units=units,
            from_=from_,
            to=to,
            sales_channels=sales_channels,
        )
    ).parsed
