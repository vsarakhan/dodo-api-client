import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_staff_meals_response_200 import GetStaffMealsResponse200
from ...models.get_staff_meals_response_400 import GetStaffMealsResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    units: str,
    from_: datetime.datetime,
    to: datetime.datetime,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["units"] = units

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to

    params["skip"] = skip

    params["take"] = take

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/accounting/staff-meals",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetStaffMealsResponse200, GetStaffMealsResponse400]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetStaffMealsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetStaffMealsResponse400.from_dict(response.json())

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
) -> Response[Union[Any, GetStaffMealsResponse200, GetStaffMealsResponse400]]:
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
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
) -> Response[Union[Any, GetStaffMealsResponse200, GetStaffMealsResponse400]]:
    """Учёт → Питание персонала

     Возвращает продукты за указанный период (включительно), израсходованные на питание персонала,
    отсортированные по дате принятия заказа и идентификатору продажи.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. `from` должен быть меньше, чем `to`.

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
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetStaffMealsResponse200, GetStaffMealsResponse400]]
    """

    kwargs = _get_kwargs(
        units=units,
        from_=from_,
        to=to,
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
    from_: datetime.datetime,
    to: datetime.datetime,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
) -> Optional[Union[Any, GetStaffMealsResponse200, GetStaffMealsResponse400]]:
    """Учёт → Питание персонала

     Возвращает продукты за указанный период (включительно), израсходованные на питание персонала,
    отсортированные по дате принятия заказа и идентификатору продажи.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. `from` должен быть меньше, чем `to`.

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
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetStaffMealsResponse200, GetStaffMealsResponse400]
    """

    return sync_detailed(
        client=client,
        units=units,
        from_=from_,
        to=to,
        skip=skip,
        take=take,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    units: str,
    from_: datetime.datetime,
    to: datetime.datetime,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
) -> Response[Union[Any, GetStaffMealsResponse200, GetStaffMealsResponse400]]:
    """Учёт → Питание персонала

     Возвращает продукты за указанный период (включительно), израсходованные на питание персонала,
    отсортированные по дате принятия заказа и идентификатору продажи.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. `from` должен быть меньше, чем `to`.

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
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetStaffMealsResponse200, GetStaffMealsResponse400]]
    """

    kwargs = _get_kwargs(
        units=units,
        from_=from_,
        to=to,
        skip=skip,
        take=take,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    units: str,
    from_: datetime.datetime,
    to: datetime.datetime,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
) -> Optional[Union[Any, GetStaffMealsResponse200, GetStaffMealsResponse400]]:
    """Учёт → Питание персонала

     Возвращает продукты за указанный период (включительно), израсходованные на питание персонала,
    отсортированные по дате принятия заказа и идентификатору продажи.

    Для получения данных необходимо указывать параметр `skip`, смещая его на количество уже полученных
    записей. Повторять до тех пор, пока не будет достигнут конец списка (`isEndOfListReached = true`).

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. `from` должен быть меньше, чем `to`.

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
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetStaffMealsResponse200, GetStaffMealsResponse400]
    """

    return (
        await asyncio_detailed(
            client=client,
            units=units,
            from_=from_,
            to=to,
            skip=skip,
            take=take,
        )
    ).parsed
