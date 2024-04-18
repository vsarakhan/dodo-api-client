import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_staff_productivity_response_200 import GetStaffProductivityResponse200
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
        "url": "/production/productivity",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetStaffProductivityResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetStaffProductivityResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetStaffProductivityResponse200]]:
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
) -> Response[Union[Any, GetStaffProductivityResponse200]]:
    """Производство → Производительность

     Возвращает метрики производительности за выбранный период и указанным пиццериям (`units`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    1. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    1. Диапазон дат между `from` и `to` параметрами не должен превышать 31 день;
    1. Даты `from` и `to` должны быть округлены до часов.


    Как расчитывается показатель «Скорость»

    Скорость — процент продуктов, изготовленных быстрее установленного стандартного времени. Для расчета
    скорости количество продуктов, приготовленных вовремя за период, делится на общее количество
    продуктов за этот период.<br />
    ⚠️ Скорость за день не считается, как средняя скоростей за смены.

    *Смена 1: вовремя приготовили 10 продуктов, всего — 100. Скорость за смену 10 / 100 = 10%.*<br />
    *Смена 2: вовремя приготовили 50 продуктов, всего — 150. Скорость за смену 50 /150 = 30%.*<br />
    *Показатель скорость будет = (10 + 50) / (100 + 150) = 24. Если вы посчитаете среднее по сменам, то
    результат будет некорректный (10 + 30) / 2 = 20.*

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        from_ (datetime.datetime):  Example: 2011-08-01T18:00:00.
        to (datetime.datetime):  Example: 2011-09-02T19:00:00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetStaffProductivityResponse200]]
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
) -> Optional[Union[Any, GetStaffProductivityResponse200]]:
    """Производство → Производительность

     Возвращает метрики производительности за выбранный период и указанным пиццериям (`units`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    1. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    1. Диапазон дат между `from` и `to` параметрами не должен превышать 31 день;
    1. Даты `from` и `to` должны быть округлены до часов.


    Как расчитывается показатель «Скорость»

    Скорость — процент продуктов, изготовленных быстрее установленного стандартного времени. Для расчета
    скорости количество продуктов, приготовленных вовремя за период, делится на общее количество
    продуктов за этот период.<br />
    ⚠️ Скорость за день не считается, как средняя скоростей за смены.

    *Смена 1: вовремя приготовили 10 продуктов, всего — 100. Скорость за смену 10 / 100 = 10%.*<br />
    *Смена 2: вовремя приготовили 50 продуктов, всего — 150. Скорость за смену 50 /150 = 30%.*<br />
    *Показатель скорость будет = (10 + 50) / (100 + 150) = 24. Если вы посчитаете среднее по сменам, то
    результат будет некорректный (10 + 30) / 2 = 20.*

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        from_ (datetime.datetime):  Example: 2011-08-01T18:00:00.
        to (datetime.datetime):  Example: 2011-09-02T19:00:00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetStaffProductivityResponse200]
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
) -> Response[Union[Any, GetStaffProductivityResponse200]]:
    """Производство → Производительность

     Возвращает метрики производительности за выбранный период и указанным пиццериям (`units`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    1. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    1. Диапазон дат между `from` и `to` параметрами не должен превышать 31 день;
    1. Даты `from` и `to` должны быть округлены до часов.


    Как расчитывается показатель «Скорость»

    Скорость — процент продуктов, изготовленных быстрее установленного стандартного времени. Для расчета
    скорости количество продуктов, приготовленных вовремя за период, делится на общее количество
    продуктов за этот период.<br />
    ⚠️ Скорость за день не считается, как средняя скоростей за смены.

    *Смена 1: вовремя приготовили 10 продуктов, всего — 100. Скорость за смену 10 / 100 = 10%.*<br />
    *Смена 2: вовремя приготовили 50 продуктов, всего — 150. Скорость за смену 50 /150 = 30%.*<br />
    *Показатель скорость будет = (10 + 50) / (100 + 150) = 24. Если вы посчитаете среднее по сменам, то
    результат будет некорректный (10 + 30) / 2 = 20.*

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        from_ (datetime.datetime):  Example: 2011-08-01T18:00:00.
        to (datetime.datetime):  Example: 2011-09-02T19:00:00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetStaffProductivityResponse200]]
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
) -> Optional[Union[Any, GetStaffProductivityResponse200]]:
    """Производство → Производительность

     Возвращает метрики производительности за выбранный период и указанным пиццериям (`units`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    1. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    1. Диапазон дат между `from` и `to` параметрами не должен превышать 31 день;
    1. Даты `from` и `to` должны быть округлены до часов.


    Как расчитывается показатель «Скорость»

    Скорость — процент продуктов, изготовленных быстрее установленного стандартного времени. Для расчета
    скорости количество продуктов, приготовленных вовремя за период, делится на общее количество
    продуктов за этот период.<br />
    ⚠️ Скорость за день не считается, как средняя скоростей за смены.

    *Смена 1: вовремя приготовили 10 продуктов, всего — 100. Скорость за смену 10 / 100 = 10%.*<br />
    *Смена 2: вовремя приготовили 50 продуктов, всего — 150. Скорость за смену 50 /150 = 30%.*<br />
    *Показатель скорость будет = (10 + 50) / (100 + 150) = 24. Если вы посчитаете среднее по сменам, то
    результат будет некорректный (10 + 30) / 2 = 20.*

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        from_ (datetime.datetime):  Example: 2011-08-01T18:00:00.
        to (datetime.datetime):  Example: 2011-09-02T19:00:00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetStaffProductivityResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            units=units,
            from_=from_,
            to=to,
        )
    ).parsed
