from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_contract import ErrorContract
from ...models.error_contract_bad_request import ErrorContractBadRequest
from ...types import Response


def _get_kwargs(
    id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/staff/schedules/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorContract, ErrorContractBadRequest]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorContractBadRequest.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorContract.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorContract.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorContract, ErrorContractBadRequest]]:
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
) -> Response[Union[Any, ErrorContract, ErrorContractBadRequest]]:
    """Команда → Расписания (удаление)

     Удаление расписания смен сотрудников.

    ### Требования к удаляемой запланированной смене:
    - Должен быть доступ к заведению, в графике которого находится запланированная смена
    - Нельзя удалять запланированные смены из закрытых заведений
    - Нельзя удалять запланированные смены в прошлом

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        id (str):  Example: 2a69836ab8f583ec11ed90098ae24dff.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorContract, ErrorContractBadRequest]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorContract, ErrorContractBadRequest]]:
    """Команда → Расписания (удаление)

     Удаление расписания смен сотрудников.

    ### Требования к удаляемой запланированной смене:
    - Должен быть доступ к заведению, в графике которого находится запланированная смена
    - Нельзя удалять запланированные смены из закрытых заведений
    - Нельзя удалять запланированные смены в прошлом

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        id (str):  Example: 2a69836ab8f583ec11ed90098ae24dff.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorContract, ErrorContractBadRequest]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorContract, ErrorContractBadRequest]]:
    """Команда → Расписания (удаление)

     Удаление расписания смен сотрудников.

    ### Требования к удаляемой запланированной смене:
    - Должен быть доступ к заведению, в графике которого находится запланированная смена
    - Нельзя удалять запланированные смены из закрытых заведений
    - Нельзя удалять запланированные смены в прошлом

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        id (str):  Example: 2a69836ab8f583ec11ed90098ae24dff.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorContract, ErrorContractBadRequest]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorContract, ErrorContractBadRequest]]:
    """Команда → Расписания (удаление)

     Удаление расписания смен сотрудников.

    ### Требования к удаляемой запланированной смене:
    - Должен быть доступ к заведению, в графике которого находится запланированная смена
    - Нельзя удалять запланированные смены из закрытых заведений
    - Нельзя удалять запланированные смены в прошлом

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        id (str):  Example: 2a69836ab8f583ec11ed90098ae24dff.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorContract, ErrorContractBadRequest]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
