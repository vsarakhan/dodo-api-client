from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_staff_members_id_suspend_response_400 import PostStaffMembersIdSuspendResponse400
from ...models.staff_member_suspend import StaffMemberSuspend
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: StaffMemberSuspend,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/staff/members/{id}/suspend",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PostStaffMembersIdSuspendResponse400]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = PostStaffMembersIdSuspendResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PostStaffMembersIdSuspendResponse400]]:
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
    body: StaffMemberSuspend,
) -> Response[Union[Any, PostStaffMembersIdSuspendResponse400]]:
    """Команда → Отстранение сотрудника

     Отстраняет сотрудника по id.

    Отстраненный сотрудник не участвует в штатной деятельности пиццерии:
     - выход на смены;
     - учет в штатных метриках пиццерии (текучесть, укомплектованность и т.д.).

    Отстранить можно только сотрудника, который сейчас находится на статусе Активен.

    Даты и время отстранения, передаваемые в API, ожидаются в UTC и далее будут приведены к локальным
    датам и времени относительно департамента отстраянемого сотрудника.

    Список идентификаторов причин для отстранения:
     - dc1746fb4916483797b16af1c8eae7a2 - просрочена мед. книжка;
     - 2206cdfd19564b1b9e52afded480d8c0 - отпуск;
     - c3e2ece1c8374e2681ba0750ca65dd82 - больничный;
     - 3f8481fdfa0a4be0b3c0a966c3ad0f39 - просрочено разрешение на работу или регистрация;
     - 64d65e1a72c1472c8a3175d0415e618f - другое.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        id (str):  Example: 000d3a240c719a8711e68aba13f7fe13.
        body (StaffMemberSuspend): Информация об отстранении

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostStaffMembersIdSuspendResponse400]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: StaffMemberSuspend,
) -> Optional[Union[Any, PostStaffMembersIdSuspendResponse400]]:
    """Команда → Отстранение сотрудника

     Отстраняет сотрудника по id.

    Отстраненный сотрудник не участвует в штатной деятельности пиццерии:
     - выход на смены;
     - учет в штатных метриках пиццерии (текучесть, укомплектованность и т.д.).

    Отстранить можно только сотрудника, который сейчас находится на статусе Активен.

    Даты и время отстранения, передаваемые в API, ожидаются в UTC и далее будут приведены к локальным
    датам и времени относительно департамента отстраянемого сотрудника.

    Список идентификаторов причин для отстранения:
     - dc1746fb4916483797b16af1c8eae7a2 - просрочена мед. книжка;
     - 2206cdfd19564b1b9e52afded480d8c0 - отпуск;
     - c3e2ece1c8374e2681ba0750ca65dd82 - больничный;
     - 3f8481fdfa0a4be0b3c0a966c3ad0f39 - просрочено разрешение на работу или регистрация;
     - 64d65e1a72c1472c8a3175d0415e618f - другое.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        id (str):  Example: 000d3a240c719a8711e68aba13f7fe13.
        body (StaffMemberSuspend): Информация об отстранении

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostStaffMembersIdSuspendResponse400]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: StaffMemberSuspend,
) -> Response[Union[Any, PostStaffMembersIdSuspendResponse400]]:
    """Команда → Отстранение сотрудника

     Отстраняет сотрудника по id.

    Отстраненный сотрудник не участвует в штатной деятельности пиццерии:
     - выход на смены;
     - учет в штатных метриках пиццерии (текучесть, укомплектованность и т.д.).

    Отстранить можно только сотрудника, который сейчас находится на статусе Активен.

    Даты и время отстранения, передаваемые в API, ожидаются в UTC и далее будут приведены к локальным
    датам и времени относительно департамента отстраянемого сотрудника.

    Список идентификаторов причин для отстранения:
     - dc1746fb4916483797b16af1c8eae7a2 - просрочена мед. книжка;
     - 2206cdfd19564b1b9e52afded480d8c0 - отпуск;
     - c3e2ece1c8374e2681ba0750ca65dd82 - больничный;
     - 3f8481fdfa0a4be0b3c0a966c3ad0f39 - просрочено разрешение на работу или регистрация;
     - 64d65e1a72c1472c8a3175d0415e618f - другое.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        id (str):  Example: 000d3a240c719a8711e68aba13f7fe13.
        body (StaffMemberSuspend): Информация об отстранении

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostStaffMembersIdSuspendResponse400]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: StaffMemberSuspend,
) -> Optional[Union[Any, PostStaffMembersIdSuspendResponse400]]:
    """Команда → Отстранение сотрудника

     Отстраняет сотрудника по id.

    Отстраненный сотрудник не участвует в штатной деятельности пиццерии:
     - выход на смены;
     - учет в штатных метриках пиццерии (текучесть, укомплектованность и т.д.).

    Отстранить можно только сотрудника, который сейчас находится на статусе Активен.

    Даты и время отстранения, передаваемые в API, ожидаются в UTC и далее будут приведены к локальным
    датам и времени относительно департамента отстраянемого сотрудника.

    Список идентификаторов причин для отстранения:
     - dc1746fb4916483797b16af1c8eae7a2 - просрочена мед. книжка;
     - 2206cdfd19564b1b9e52afded480d8c0 - отпуск;
     - c3e2ece1c8374e2681ba0750ca65dd82 - больничный;
     - 3f8481fdfa0a4be0b3c0a966c3ad0f39 - просрочено разрешение на работу или регистрация;
     - 64d65e1a72c1472c8a3175d0415e618f - другое.

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        id (str):  Example: 000d3a240c719a8711e68aba13f7fe13.
        body (StaffMemberSuspend): Информация об отстранении

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostStaffMembersIdSuspendResponse400]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
