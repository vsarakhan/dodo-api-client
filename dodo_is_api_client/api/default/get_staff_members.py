import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_staff_members_staff_type import GetStaffMembersStaffType
from ...models.staff_members_response import StaffMembersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    staff_type: Union[Unset, GetStaffMembersStaffType] = UNSET,
    statuses: Union[Unset, str] = UNSET,
    hired_from: Union[Unset, datetime.date] = UNSET,
    hired_to: Union[Unset, datetime.date] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    dismissed_from: Union[Unset, datetime.date] = UNSET,
    dismissed_to: Union[Unset, datetime.date] = UNSET,
    units: Union[Unset, str] = UNSET,
    last_modified_from: Union[Unset, datetime.date] = UNSET,
    last_modified_to: Union[Unset, datetime.date] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_staff_type: Union[Unset, str] = UNSET
    if not isinstance(staff_type, Unset):
        json_staff_type = staff_type.value

    params["staffType"] = json_staff_type

    params["statuses"] = statuses

    json_hired_from: Union[Unset, str] = UNSET
    if not isinstance(hired_from, Unset):
        json_hired_from = hired_from.isoformat()
    params["hiredFrom"] = json_hired_from

    json_hired_to: Union[Unset, str] = UNSET
    if not isinstance(hired_to, Unset):
        json_hired_to = hired_to.isoformat()
    params["hiredTo"] = json_hired_to

    params["skip"] = skip

    params["take"] = take

    json_dismissed_from: Union[Unset, str] = UNSET
    if not isinstance(dismissed_from, Unset):
        json_dismissed_from = dismissed_from.isoformat()
    params["dismissedFrom"] = json_dismissed_from

    json_dismissed_to: Union[Unset, str] = UNSET
    if not isinstance(dismissed_to, Unset):
        json_dismissed_to = dismissed_to.isoformat()
    params["dismissedTo"] = json_dismissed_to

    params["units"] = units

    json_last_modified_from: Union[Unset, str] = UNSET
    if not isinstance(last_modified_from, Unset):
        json_last_modified_from = last_modified_from.isoformat()
    params["lastModifiedFrom"] = json_last_modified_from

    json_last_modified_to: Union[Unset, str] = UNSET
    if not isinstance(last_modified_to, Unset):
        json_last_modified_to = last_modified_to.isoformat()
    params["lastModifiedTo"] = json_last_modified_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/staff/members",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, StaffMembersResponse, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StaffMembersResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(str, response.json())
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
) -> Response[Union[Any, StaffMembersResponse, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    staff_type: Union[Unset, GetStaffMembersStaffType] = UNSET,
    statuses: Union[Unset, str] = UNSET,
    hired_from: Union[Unset, datetime.date] = UNSET,
    hired_to: Union[Unset, datetime.date] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    dismissed_from: Union[Unset, datetime.date] = UNSET,
    dismissed_to: Union[Unset, datetime.date] = UNSET,
    units: Union[Unset, str] = UNSET,
    last_modified_from: Union[Unset, datetime.date] = UNSET,
    last_modified_to: Union[Unset, datetime.date] = UNSET,
) -> Response[Union[Any, StaffMembersResponse, str]]:
    """Команда → Список сотрудников

     Возвращает список сотрудников, отсортированный по дате трудоустройства (`hiredOn`).

    ### Требования к query параметрам:
    - фильтр по типу должности `staffType` применяется только по одному значению
    - фильтр по статусу `statuses` применяется по нескольким значениям (указывается через запятую без
    пробелов)
    - фильтр по дате трудоустройства `hiredFrom/hiredTo`, применяется как по промежутку дат, так и по
    отдельным from/to датам
    - фильтр по дате увольнения `dismissedFrom/dismissedTo`, применяется как по промежутку дат, так и по
    отдельным from/to датам
    - фильтр по дате изменения `lastModifiedFrom/lastModifiedTo`, применяется как по промежутку дат, так
    и по отдельным from/to датам
    - фильтр по заведениям `units` применяется по нескольким значениям; если не указан, то будут выданы
    записи по всем доступным для пользователя заведениям
    - фильтр `skip` должен быть больше 0, иначе возвращается 400
    - фильтр `take` должен быть больше 0 и меньше либо равен 1000, иначе возвращается 400
    - фильтр `hiredFrom` должен быть не больше `hiredTo`, иначе возвращается 400
    - фильтр `dismissedFrom` должен быть не больше `dismissedTo`, иначе возвращается 400
    - фильтр `lastModifiedFrom` должен быть не больше `lastModifiedTo`, иначе возвращается 400
    - разрешенные значения для фильтров `staffType`, `statuses` указаны в их описаниях

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены

    Args:
        staff_type (Union[Unset, GetStaffMembersStaffType]):  Example: KitchenMember.
        statuses (Union[Unset, str]):  Example: Suspended,Dismissed.
        hired_from (Union[Unset, datetime.date]):  Example: 2022-10-20.
        hired_to (Union[Unset, datetime.date]):  Example: 2022-10-27.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        dismissed_from (Union[Unset, datetime.date]):  Example: 2022-10-20.
        dismissed_to (Union[Unset, datetime.date]):  Example: 2022-10-27.
        units (Union[Unset, str]):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e6
            8aba13f7fc8a,000d3a240c719a8711e68aba13f7fe13.
        last_modified_from (Union[Unset, datetime.date]):  Example: 2022-11-20.
        last_modified_to (Union[Unset, datetime.date]):  Example: 2022-11-27.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StaffMembersResponse, str]]
    """

    kwargs = _get_kwargs(
        staff_type=staff_type,
        statuses=statuses,
        hired_from=hired_from,
        hired_to=hired_to,
        skip=skip,
        take=take,
        dismissed_from=dismissed_from,
        dismissed_to=dismissed_to,
        units=units,
        last_modified_from=last_modified_from,
        last_modified_to=last_modified_to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    staff_type: Union[Unset, GetStaffMembersStaffType] = UNSET,
    statuses: Union[Unset, str] = UNSET,
    hired_from: Union[Unset, datetime.date] = UNSET,
    hired_to: Union[Unset, datetime.date] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    dismissed_from: Union[Unset, datetime.date] = UNSET,
    dismissed_to: Union[Unset, datetime.date] = UNSET,
    units: Union[Unset, str] = UNSET,
    last_modified_from: Union[Unset, datetime.date] = UNSET,
    last_modified_to: Union[Unset, datetime.date] = UNSET,
) -> Optional[Union[Any, StaffMembersResponse, str]]:
    """Команда → Список сотрудников

     Возвращает список сотрудников, отсортированный по дате трудоустройства (`hiredOn`).

    ### Требования к query параметрам:
    - фильтр по типу должности `staffType` применяется только по одному значению
    - фильтр по статусу `statuses` применяется по нескольким значениям (указывается через запятую без
    пробелов)
    - фильтр по дате трудоустройства `hiredFrom/hiredTo`, применяется как по промежутку дат, так и по
    отдельным from/to датам
    - фильтр по дате увольнения `dismissedFrom/dismissedTo`, применяется как по промежутку дат, так и по
    отдельным from/to датам
    - фильтр по дате изменения `lastModifiedFrom/lastModifiedTo`, применяется как по промежутку дат, так
    и по отдельным from/to датам
    - фильтр по заведениям `units` применяется по нескольким значениям; если не указан, то будут выданы
    записи по всем доступным для пользователя заведениям
    - фильтр `skip` должен быть больше 0, иначе возвращается 400
    - фильтр `take` должен быть больше 0 и меньше либо равен 1000, иначе возвращается 400
    - фильтр `hiredFrom` должен быть не больше `hiredTo`, иначе возвращается 400
    - фильтр `dismissedFrom` должен быть не больше `dismissedTo`, иначе возвращается 400
    - фильтр `lastModifiedFrom` должен быть не больше `lastModifiedTo`, иначе возвращается 400
    - разрешенные значения для фильтров `staffType`, `statuses` указаны в их описаниях

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены

    Args:
        staff_type (Union[Unset, GetStaffMembersStaffType]):  Example: KitchenMember.
        statuses (Union[Unset, str]):  Example: Suspended,Dismissed.
        hired_from (Union[Unset, datetime.date]):  Example: 2022-10-20.
        hired_to (Union[Unset, datetime.date]):  Example: 2022-10-27.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        dismissed_from (Union[Unset, datetime.date]):  Example: 2022-10-20.
        dismissed_to (Union[Unset, datetime.date]):  Example: 2022-10-27.
        units (Union[Unset, str]):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e6
            8aba13f7fc8a,000d3a240c719a8711e68aba13f7fe13.
        last_modified_from (Union[Unset, datetime.date]):  Example: 2022-11-20.
        last_modified_to (Union[Unset, datetime.date]):  Example: 2022-11-27.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StaffMembersResponse, str]
    """

    return sync_detailed(
        client=client,
        staff_type=staff_type,
        statuses=statuses,
        hired_from=hired_from,
        hired_to=hired_to,
        skip=skip,
        take=take,
        dismissed_from=dismissed_from,
        dismissed_to=dismissed_to,
        units=units,
        last_modified_from=last_modified_from,
        last_modified_to=last_modified_to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    staff_type: Union[Unset, GetStaffMembersStaffType] = UNSET,
    statuses: Union[Unset, str] = UNSET,
    hired_from: Union[Unset, datetime.date] = UNSET,
    hired_to: Union[Unset, datetime.date] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    dismissed_from: Union[Unset, datetime.date] = UNSET,
    dismissed_to: Union[Unset, datetime.date] = UNSET,
    units: Union[Unset, str] = UNSET,
    last_modified_from: Union[Unset, datetime.date] = UNSET,
    last_modified_to: Union[Unset, datetime.date] = UNSET,
) -> Response[Union[Any, StaffMembersResponse, str]]:
    """Команда → Список сотрудников

     Возвращает список сотрудников, отсортированный по дате трудоустройства (`hiredOn`).

    ### Требования к query параметрам:
    - фильтр по типу должности `staffType` применяется только по одному значению
    - фильтр по статусу `statuses` применяется по нескольким значениям (указывается через запятую без
    пробелов)
    - фильтр по дате трудоустройства `hiredFrom/hiredTo`, применяется как по промежутку дат, так и по
    отдельным from/to датам
    - фильтр по дате увольнения `dismissedFrom/dismissedTo`, применяется как по промежутку дат, так и по
    отдельным from/to датам
    - фильтр по дате изменения `lastModifiedFrom/lastModifiedTo`, применяется как по промежутку дат, так
    и по отдельным from/to датам
    - фильтр по заведениям `units` применяется по нескольким значениям; если не указан, то будут выданы
    записи по всем доступным для пользователя заведениям
    - фильтр `skip` должен быть больше 0, иначе возвращается 400
    - фильтр `take` должен быть больше 0 и меньше либо равен 1000, иначе возвращается 400
    - фильтр `hiredFrom` должен быть не больше `hiredTo`, иначе возвращается 400
    - фильтр `dismissedFrom` должен быть не больше `dismissedTo`, иначе возвращается 400
    - фильтр `lastModifiedFrom` должен быть не больше `lastModifiedTo`, иначе возвращается 400
    - разрешенные значения для фильтров `staffType`, `statuses` указаны в их описаниях

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены

    Args:
        staff_type (Union[Unset, GetStaffMembersStaffType]):  Example: KitchenMember.
        statuses (Union[Unset, str]):  Example: Suspended,Dismissed.
        hired_from (Union[Unset, datetime.date]):  Example: 2022-10-20.
        hired_to (Union[Unset, datetime.date]):  Example: 2022-10-27.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        dismissed_from (Union[Unset, datetime.date]):  Example: 2022-10-20.
        dismissed_to (Union[Unset, datetime.date]):  Example: 2022-10-27.
        units (Union[Unset, str]):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e6
            8aba13f7fc8a,000d3a240c719a8711e68aba13f7fe13.
        last_modified_from (Union[Unset, datetime.date]):  Example: 2022-11-20.
        last_modified_to (Union[Unset, datetime.date]):  Example: 2022-11-27.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StaffMembersResponse, str]]
    """

    kwargs = _get_kwargs(
        staff_type=staff_type,
        statuses=statuses,
        hired_from=hired_from,
        hired_to=hired_to,
        skip=skip,
        take=take,
        dismissed_from=dismissed_from,
        dismissed_to=dismissed_to,
        units=units,
        last_modified_from=last_modified_from,
        last_modified_to=last_modified_to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    staff_type: Union[Unset, GetStaffMembersStaffType] = UNSET,
    statuses: Union[Unset, str] = UNSET,
    hired_from: Union[Unset, datetime.date] = UNSET,
    hired_to: Union[Unset, datetime.date] = UNSET,
    skip: Union[Unset, int] = 0,
    take: Union[Unset, int] = 100,
    dismissed_from: Union[Unset, datetime.date] = UNSET,
    dismissed_to: Union[Unset, datetime.date] = UNSET,
    units: Union[Unset, str] = UNSET,
    last_modified_from: Union[Unset, datetime.date] = UNSET,
    last_modified_to: Union[Unset, datetime.date] = UNSET,
) -> Optional[Union[Any, StaffMembersResponse, str]]:
    """Команда → Список сотрудников

     Возвращает список сотрудников, отсортированный по дате трудоустройства (`hiredOn`).

    ### Требования к query параметрам:
    - фильтр по типу должности `staffType` применяется только по одному значению
    - фильтр по статусу `statuses` применяется по нескольким значениям (указывается через запятую без
    пробелов)
    - фильтр по дате трудоустройства `hiredFrom/hiredTo`, применяется как по промежутку дат, так и по
    отдельным from/to датам
    - фильтр по дате увольнения `dismissedFrom/dismissedTo`, применяется как по промежутку дат, так и по
    отдельным from/to датам
    - фильтр по дате изменения `lastModifiedFrom/lastModifiedTo`, применяется как по промежутку дат, так
    и по отдельным from/to датам
    - фильтр по заведениям `units` применяется по нескольким значениям; если не указан, то будут выданы
    записи по всем доступным для пользователя заведениям
    - фильтр `skip` должен быть больше 0, иначе возвращается 400
    - фильтр `take` должен быть больше 0 и меньше либо равен 1000, иначе возвращается 400
    - фильтр `hiredFrom` должен быть не больше `hiredTo`, иначе возвращается 400
    - фильтр `dismissedFrom` должен быть не больше `dismissedTo`, иначе возвращается 400
    - фильтр `lastModifiedFrom` должен быть не больше `lastModifiedTo`, иначе возвращается 400
    - разрешенные значения для фильтров `staffType`, `statuses` указаны в их описаниях

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены

    Args:
        staff_type (Union[Unset, GetStaffMembersStaffType]):  Example: KitchenMember.
        statuses (Union[Unset, str]):  Example: Suspended,Dismissed.
        hired_from (Union[Unset, datetime.date]):  Example: 2022-10-20.
        hired_to (Union[Unset, datetime.date]):  Example: 2022-10-27.
        skip (Union[Unset, int]):  Default: 0. Example: 100.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        dismissed_from (Union[Unset, datetime.date]):  Example: 2022-10-20.
        dismissed_to (Union[Unset, datetime.date]):  Example: 2022-10-27.
        units (Union[Unset, str]):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e6
            8aba13f7fc8a,000d3a240c719a8711e68aba13f7fe13.
        last_modified_from (Union[Unset, datetime.date]):  Example: 2022-11-20.
        last_modified_to (Union[Unset, datetime.date]):  Example: 2022-11-27.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StaffMembersResponse, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            staff_type=staff_type,
            statuses=statuses,
            hired_from=hired_from,
            hired_to=hired_to,
            skip=skip,
            take=take,
            dismissed_from=dismissed_from,
            dismissed_to=dismissed_to,
            units=units,
            last_modified_from=last_modified_from,
            last_modified_to=last_modified_to,
        )
    ).parsed
