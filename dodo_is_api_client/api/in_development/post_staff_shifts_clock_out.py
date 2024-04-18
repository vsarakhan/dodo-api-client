from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_contract import ErrorContract
from ...models.post_staff_shifts_clock_out_body import PostStaffShiftsClockOutBody
from ...types import Response


def _get_kwargs(
    *,
    body: PostStaffShiftsClockOutBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/staff/shifts/clock-out",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorContract]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorContract.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorContract.from_dict(response.json())

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
) -> Response[Union[Any, ErrorContract]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostStaffShiftsClockOutBody,
) -> Response[Union[Any, ErrorContract]]:
    """Команда → Закрытие смены

     Закрытие активной смены сотрудника.

    <!-- theme: none -->

    > #### Доступно для следующих ролей:
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены
    >
    >   `Division administrator` - Администратор подразделения

    Args:
        body (PostStaffShiftsClockOutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorContract]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostStaffShiftsClockOutBody,
) -> Optional[Union[Any, ErrorContract]]:
    """Команда → Закрытие смены

     Закрытие активной смены сотрудника.

    <!-- theme: none -->

    > #### Доступно для следующих ролей:
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены
    >
    >   `Division administrator` - Администратор подразделения

    Args:
        body (PostStaffShiftsClockOutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorContract]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostStaffShiftsClockOutBody,
) -> Response[Union[Any, ErrorContract]]:
    """Команда → Закрытие смены

     Закрытие активной смены сотрудника.

    <!-- theme: none -->

    > #### Доступно для следующих ролей:
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены
    >
    >   `Division administrator` - Администратор подразделения

    Args:
        body (PostStaffShiftsClockOutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorContract]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostStaffShiftsClockOutBody,
) -> Optional[Union[Any, ErrorContract]]:
    """Команда → Закрытие смены

     Закрытие активной смены сотрудника.

    <!-- theme: none -->

    > #### Доступно для следующих ролей:
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены
    >
    >   `Division administrator` - Администратор подразделения

    Args:
        body (PostStaffShiftsClockOutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorContract]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
