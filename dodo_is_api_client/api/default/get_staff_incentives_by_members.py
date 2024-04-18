import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_staff_incentives_by_members_response_200 import GetStaffIncentivesByMembersResponse200
from ...models.get_staff_incentives_by_members_staff_type import GetStaffIncentivesByMembersStaffType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    units: str,
    from_: datetime.datetime,
    to: datetime.datetime,
    staff_type: Union[Unset, GetStaffIncentivesByMembersStaffType] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["units"] = units

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to

    json_staff_type: Union[Unset, str] = UNSET
    if not isinstance(staff_type, Unset):
        json_staff_type = staff_type.value

    params["staffType"] = json_staff_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/staff/incentives-by-members",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetStaffIncentivesByMembersResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetStaffIncentivesByMembersResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetStaffIncentivesByMembersResponse200]]:
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
    staff_type: Union[Unset, GetStaffIncentivesByMembersStaffType] = UNSET,
) -> Response[Union[Any, GetStaffIncentivesByMembersResponse200]]:
    """Команда → Вознаграждения (новое)

     Возвращает вознаграждения за период для набора заведений (`units`).
    Вознаграждения сгруппированы по сотруднику с детализацией: смены, премии.
    Вознаграждения считаются для сотрудников, которые отработали хотя бы одну смену в указанных
    заведения за указанный период времени, а также сведения о премии.

    Из-за возможного изменения ставки и коэффициентов в течение времени смены, она разбивается на
    интервалы по 15 минут. Затем к каждому интервалу применяются все коэффициенты и ставки. Остаток от
    разбиения не учитывается. Например, смена длительностью 65 минут будет разбита на 4 интервала и 5
    оставшихся минут не будут учитываться.

    Примеры:

    *Пример 1: Инструктор отработал смену с 08:00 до 16:00. Его ставка 150 рублей/час. В итоге он
    получит вознаграждение: 8 × 150 = 1200 рублей.*

    *Пример 2: Стажер отработал вечернюю смену с 16:00 до 00:00. С 22:00 установлен ночной коэффициент —
    2. Ставка сотрудника 60 рублей/час. За смену он получит вознаграждение: 6 × 60 + 2 × 2 × 60 = 360 +
    240 = 600 рублей.*

    *Пример 3: Пиццамейкер работал с 08:00 до 14:00. Его ставка 100 рублей/час. С 08:00 до 12:00
    ожидался огромный наплыв посетителей, поэтому за работу в это время установлен коэффициент особого
    дня — 1,5. Сотрудник получит такое вознаграждение: 4 × 1,5 × 100 +2 × 100 = 600 + 200 = 800 рублей.*

    *Пример 4: Кандидат отработал 4 часа. Его ставка 70 рублей в час + премия за стаж 15 рублей за час.
    Он получит вознаграждение: (70 + 15) × 4 = 340 рублей.*

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. Диапазон дат между `to` и `from` параметрами не должен превышать 31 день.
    4. Фильтр по типу должности `staffType` применяется только по одному значению

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
        from_ (datetime.datetime):  Example: 2011-08-01T18:31:42.
        to (datetime.datetime):  Example: 2011-09-02T19:21:53.
        staff_type (Union[Unset, GetStaffIncentivesByMembersStaffType]):  Example: KitchenMember.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetStaffIncentivesByMembersResponse200]]
    """

    kwargs = _get_kwargs(
        units=units,
        from_=from_,
        to=to,
        staff_type=staff_type,
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
    staff_type: Union[Unset, GetStaffIncentivesByMembersStaffType] = UNSET,
) -> Optional[Union[Any, GetStaffIncentivesByMembersResponse200]]:
    """Команда → Вознаграждения (новое)

     Возвращает вознаграждения за период для набора заведений (`units`).
    Вознаграждения сгруппированы по сотруднику с детализацией: смены, премии.
    Вознаграждения считаются для сотрудников, которые отработали хотя бы одну смену в указанных
    заведения за указанный период времени, а также сведения о премии.

    Из-за возможного изменения ставки и коэффициентов в течение времени смены, она разбивается на
    интервалы по 15 минут. Затем к каждому интервалу применяются все коэффициенты и ставки. Остаток от
    разбиения не учитывается. Например, смена длительностью 65 минут будет разбита на 4 интервала и 5
    оставшихся минут не будут учитываться.

    Примеры:

    *Пример 1: Инструктор отработал смену с 08:00 до 16:00. Его ставка 150 рублей/час. В итоге он
    получит вознаграждение: 8 × 150 = 1200 рублей.*

    *Пример 2: Стажер отработал вечернюю смену с 16:00 до 00:00. С 22:00 установлен ночной коэффициент —
    2. Ставка сотрудника 60 рублей/час. За смену он получит вознаграждение: 6 × 60 + 2 × 2 × 60 = 360 +
    240 = 600 рублей.*

    *Пример 3: Пиццамейкер работал с 08:00 до 14:00. Его ставка 100 рублей/час. С 08:00 до 12:00
    ожидался огромный наплыв посетителей, поэтому за работу в это время установлен коэффициент особого
    дня — 1,5. Сотрудник получит такое вознаграждение: 4 × 1,5 × 100 +2 × 100 = 600 + 200 = 800 рублей.*

    *Пример 4: Кандидат отработал 4 часа. Его ставка 70 рублей в час + премия за стаж 15 рублей за час.
    Он получит вознаграждение: (70 + 15) × 4 = 340 рублей.*

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. Диапазон дат между `to` и `from` параметрами не должен превышать 31 день.
    4. Фильтр по типу должности `staffType` применяется только по одному значению

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
        from_ (datetime.datetime):  Example: 2011-08-01T18:31:42.
        to (datetime.datetime):  Example: 2011-09-02T19:21:53.
        staff_type (Union[Unset, GetStaffIncentivesByMembersStaffType]):  Example: KitchenMember.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetStaffIncentivesByMembersResponse200]
    """

    return sync_detailed(
        client=client,
        units=units,
        from_=from_,
        to=to,
        staff_type=staff_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    units: str,
    from_: datetime.datetime,
    to: datetime.datetime,
    staff_type: Union[Unset, GetStaffIncentivesByMembersStaffType] = UNSET,
) -> Response[Union[Any, GetStaffIncentivesByMembersResponse200]]:
    """Команда → Вознаграждения (новое)

     Возвращает вознаграждения за период для набора заведений (`units`).
    Вознаграждения сгруппированы по сотруднику с детализацией: смены, премии.
    Вознаграждения считаются для сотрудников, которые отработали хотя бы одну смену в указанных
    заведения за указанный период времени, а также сведения о премии.

    Из-за возможного изменения ставки и коэффициентов в течение времени смены, она разбивается на
    интервалы по 15 минут. Затем к каждому интервалу применяются все коэффициенты и ставки. Остаток от
    разбиения не учитывается. Например, смена длительностью 65 минут будет разбита на 4 интервала и 5
    оставшихся минут не будут учитываться.

    Примеры:

    *Пример 1: Инструктор отработал смену с 08:00 до 16:00. Его ставка 150 рублей/час. В итоге он
    получит вознаграждение: 8 × 150 = 1200 рублей.*

    *Пример 2: Стажер отработал вечернюю смену с 16:00 до 00:00. С 22:00 установлен ночной коэффициент —
    2. Ставка сотрудника 60 рублей/час. За смену он получит вознаграждение: 6 × 60 + 2 × 2 × 60 = 360 +
    240 = 600 рублей.*

    *Пример 3: Пиццамейкер работал с 08:00 до 14:00. Его ставка 100 рублей/час. С 08:00 до 12:00
    ожидался огромный наплыв посетителей, поэтому за работу в это время установлен коэффициент особого
    дня — 1,5. Сотрудник получит такое вознаграждение: 4 × 1,5 × 100 +2 × 100 = 600 + 200 = 800 рублей.*

    *Пример 4: Кандидат отработал 4 часа. Его ставка 70 рублей в час + премия за стаж 15 рублей за час.
    Он получит вознаграждение: (70 + 15) × 4 = 340 рублей.*

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. Диапазон дат между `to` и `from` параметрами не должен превышать 31 день.
    4. Фильтр по типу должности `staffType` применяется только по одному значению

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
        from_ (datetime.datetime):  Example: 2011-08-01T18:31:42.
        to (datetime.datetime):  Example: 2011-09-02T19:21:53.
        staff_type (Union[Unset, GetStaffIncentivesByMembersStaffType]):  Example: KitchenMember.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetStaffIncentivesByMembersResponse200]]
    """

    kwargs = _get_kwargs(
        units=units,
        from_=from_,
        to=to,
        staff_type=staff_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    units: str,
    from_: datetime.datetime,
    to: datetime.datetime,
    staff_type: Union[Unset, GetStaffIncentivesByMembersStaffType] = UNSET,
) -> Optional[Union[Any, GetStaffIncentivesByMembersResponse200]]:
    """Команда → Вознаграждения (новое)

     Возвращает вознаграждения за период для набора заведений (`units`).
    Вознаграждения сгруппированы по сотруднику с детализацией: смены, премии.
    Вознаграждения считаются для сотрудников, которые отработали хотя бы одну смену в указанных
    заведения за указанный период времени, а также сведения о премии.

    Из-за возможного изменения ставки и коэффициентов в течение времени смены, она разбивается на
    интервалы по 15 минут. Затем к каждому интервалу применяются все коэффициенты и ставки. Остаток от
    разбиения не учитывается. Например, смена длительностью 65 минут будет разбита на 4 интервала и 5
    оставшихся минут не будут учитываться.

    Примеры:

    *Пример 1: Инструктор отработал смену с 08:00 до 16:00. Его ставка 150 рублей/час. В итоге он
    получит вознаграждение: 8 × 150 = 1200 рублей.*

    *Пример 2: Стажер отработал вечернюю смену с 16:00 до 00:00. С 22:00 установлен ночной коэффициент —
    2. Ставка сотрудника 60 рублей/час. За смену он получит вознаграждение: 6 × 60 + 2 × 2 × 60 = 360 +
    240 = 600 рублей.*

    *Пример 3: Пиццамейкер работал с 08:00 до 14:00. Его ставка 100 рублей/час. С 08:00 до 12:00
    ожидался огромный наплыв посетителей, поэтому за работу в это время установлен коэффициент особого
    дня — 1,5. Сотрудник получит такое вознаграждение: 4 × 1,5 × 100 +2 × 100 = 600 + 200 = 800 рублей.*

    *Пример 4: Кандидат отработал 4 часа. Его ставка 70 рублей в час + премия за стаж 15 рублей за час.
    Он получит вознаграждение: (70 + 15) × 4 = 340 рублей.*

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 заведений в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;
    3. Диапазон дат между `to` и `from` параметрами не должен превышать 31 день.
    4. Фильтр по типу должности `staffType` применяется только по одному значению

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
        from_ (datetime.datetime):  Example: 2011-08-01T18:31:42.
        to (datetime.datetime):  Example: 2011-09-02T19:21:53.
        staff_type (Union[Unset, GetStaffIncentivesByMembersStaffType]):  Example: KitchenMember.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetStaffIncentivesByMembersResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            units=units,
            from_=from_,
            to=to,
            staff_type=staff_type,
        )
    ).parsed
