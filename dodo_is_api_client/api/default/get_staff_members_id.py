from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_staff_members_id_findby import GetStaffMembersIdFindby
from ...models.staff_member import StaffMember
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    findby: Union[Unset, GetStaffMembersIdFindby] = GetStaffMembersIdFindby.STAFFID,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_findby: Union[Unset, str] = UNSET
    if not isinstance(findby, Unset):
        json_findby = findby.value

    params["findby"] = json_findby

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/staff/members/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, StaffMember]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StaffMember.from_dict(response.json())

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
) -> Response[Union[Any, StaffMember]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    findby: Union[Unset, GetStaffMembersIdFindby] = GetStaffMembersIdFindby.STAFFID,
) -> Response[Union[Any, StaffMember]]:
    """Команда → Информация о сотруднике

     Возвращает полную информацию по запрошенному сотруднику.

    Вы можете запросить информацию о сотруднике как по идентификатору сотрудника (`staffId`), так и по
    идентификатору пользователя (`userId`). Для этого необходимо указать дополнительный параметр
    `findby`. Данный параметр принимает 2 значения:
     - `staffid` - для поиска по идентификатору сотрудника (используется как стандартное значение)
     - `userid` - для поиска по идентификатору пользователя

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены.
    >
    >   `Employee` - Сотрудник. Получение данных **только о самом себе**

    Args:
        id (str):  Example: 000d3a240c719a8711e68aba13f7fe13.
        findby (Union[Unset, GetStaffMembersIdFindby]):  Default: GetStaffMembersIdFindby.STAFFID.
            Example: staffid.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StaffMember]]
    """

    kwargs = _get_kwargs(
        id=id,
        findby=findby,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    findby: Union[Unset, GetStaffMembersIdFindby] = GetStaffMembersIdFindby.STAFFID,
) -> Optional[Union[Any, StaffMember]]:
    """Команда → Информация о сотруднике

     Возвращает полную информацию по запрошенному сотруднику.

    Вы можете запросить информацию о сотруднике как по идентификатору сотрудника (`staffId`), так и по
    идентификатору пользователя (`userId`). Для этого необходимо указать дополнительный параметр
    `findby`. Данный параметр принимает 2 значения:
     - `staffid` - для поиска по идентификатору сотрудника (используется как стандартное значение)
     - `userid` - для поиска по идентификатору пользователя

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены.
    >
    >   `Employee` - Сотрудник. Получение данных **только о самом себе**

    Args:
        id (str):  Example: 000d3a240c719a8711e68aba13f7fe13.
        findby (Union[Unset, GetStaffMembersIdFindby]):  Default: GetStaffMembersIdFindby.STAFFID.
            Example: staffid.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StaffMember]
    """

    return sync_detailed(
        id=id,
        client=client,
        findby=findby,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    findby: Union[Unset, GetStaffMembersIdFindby] = GetStaffMembersIdFindby.STAFFID,
) -> Response[Union[Any, StaffMember]]:
    """Команда → Информация о сотруднике

     Возвращает полную информацию по запрошенному сотруднику.

    Вы можете запросить информацию о сотруднике как по идентификатору сотрудника (`staffId`), так и по
    идентификатору пользователя (`userId`). Для этого необходимо указать дополнительный параметр
    `findby`. Данный параметр принимает 2 значения:
     - `staffid` - для поиска по идентификатору сотрудника (используется как стандартное значение)
     - `userid` - для поиска по идентификатору пользователя

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены.
    >
    >   `Employee` - Сотрудник. Получение данных **только о самом себе**

    Args:
        id (str):  Example: 000d3a240c719a8711e68aba13f7fe13.
        findby (Union[Unset, GetStaffMembersIdFindby]):  Default: GetStaffMembersIdFindby.STAFFID.
            Example: staffid.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StaffMember]]
    """

    kwargs = _get_kwargs(
        id=id,
        findby=findby,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    findby: Union[Unset, GetStaffMembersIdFindby] = GetStaffMembersIdFindby.STAFFID,
) -> Optional[Union[Any, StaffMember]]:
    """Команда → Информация о сотруднике

     Возвращает полную информацию по запрошенному сотруднику.

    Вы можете запросить информацию о сотруднике как по идентификатору сотрудника (`staffId`), так и по
    идентификатору пользователя (`userId`). Для этого необходимо указать дополнительный параметр
    `findby`. Данный параметр принимает 2 значения:
     - `staffid` - для поиска по идентификатору сотрудника (используется как стандартное значение)
     - `userid` - для поиска по идентификатору пользователя

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены.
    >
    >   `Employee` - Сотрудник. Получение данных **только о самом себе**

    Args:
        id (str):  Example: 000d3a240c719a8711e68aba13f7fe13.
        findby (Union[Unset, GetStaffMembersIdFindby]):  Default: GetStaffMembersIdFindby.STAFFID.
            Example: staffid.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StaffMember]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            findby=findby,
        )
    ).parsed
