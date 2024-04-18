from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_contract import ErrorContract
from ...models.error_contract_bad_request import ErrorContractBadRequest
from ...models.post_staff_schedules_body import PostStaffSchedulesBody
from ...models.post_staff_schedules_response_200 import PostStaffSchedulesResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostStaffSchedulesBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/staff/schedules",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorContract, ErrorContractBadRequest, PostStaffSchedulesResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostStaffSchedulesResponse200.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, ErrorContract, ErrorContractBadRequest, PostStaffSchedulesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostStaffSchedulesBody,
) -> Response[Union[Any, ErrorContract, ErrorContractBadRequest, PostStaffSchedulesResponse200]]:
    """Команда → Расписания (создание)

     Создание расписания смен сотрудников.

    ### Требования к входным параметрам:
     - При добавлении нескольких смен на одного сотрудника они не должны пересекаться.
     - scheduledShiftStartAt и scheduledShiftEndAt необходимо передавать в UTC. Однако при получении
    графика будет отображаться уже локальное время.
     - scheduledShiftStartAt, scheduledShiftEndAt - должны быть переданы в разрезе 15-ти минутного
    интервала без секунд.
     - Максимальная длительность смены в графике 24 часа, минимальная 15 минут.
     - Добавлять смены в график можно не дальше чем на 31 день.
     - Добавлять смены в график можно только в будущем.
     - Запрещено добавлять курьеров производственные станции внутри заведения.
     - Запрещено добавлять работника заведения в график курьеров.
     - Список доступных производственных станций можно запросить в `Заведения → Производственные
    станции`
     - Список доступных должностей можно запросить в `Команда → Должности сотрудников`

    ---

     ### Требования к пользовательскому доступу:
     Требуется одна из ролей:
      - `Division administrator` - Администратор подразделения
      - `Store Manager` - Менеджер офиса

    Args:
        body (PostStaffSchedulesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorContract, ErrorContractBadRequest, PostStaffSchedulesResponse200]]
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
    body: PostStaffSchedulesBody,
) -> Optional[Union[Any, ErrorContract, ErrorContractBadRequest, PostStaffSchedulesResponse200]]:
    """Команда → Расписания (создание)

     Создание расписания смен сотрудников.

    ### Требования к входным параметрам:
     - При добавлении нескольких смен на одного сотрудника они не должны пересекаться.
     - scheduledShiftStartAt и scheduledShiftEndAt необходимо передавать в UTC. Однако при получении
    графика будет отображаться уже локальное время.
     - scheduledShiftStartAt, scheduledShiftEndAt - должны быть переданы в разрезе 15-ти минутного
    интервала без секунд.
     - Максимальная длительность смены в графике 24 часа, минимальная 15 минут.
     - Добавлять смены в график можно не дальше чем на 31 день.
     - Добавлять смены в график можно только в будущем.
     - Запрещено добавлять курьеров производственные станции внутри заведения.
     - Запрещено добавлять работника заведения в график курьеров.
     - Список доступных производственных станций можно запросить в `Заведения → Производственные
    станции`
     - Список доступных должностей можно запросить в `Команда → Должности сотрудников`

    ---

     ### Требования к пользовательскому доступу:
     Требуется одна из ролей:
      - `Division administrator` - Администратор подразделения
      - `Store Manager` - Менеджер офиса

    Args:
        body (PostStaffSchedulesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorContract, ErrorContractBadRequest, PostStaffSchedulesResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostStaffSchedulesBody,
) -> Response[Union[Any, ErrorContract, ErrorContractBadRequest, PostStaffSchedulesResponse200]]:
    """Команда → Расписания (создание)

     Создание расписания смен сотрудников.

    ### Требования к входным параметрам:
     - При добавлении нескольких смен на одного сотрудника они не должны пересекаться.
     - scheduledShiftStartAt и scheduledShiftEndAt необходимо передавать в UTC. Однако при получении
    графика будет отображаться уже локальное время.
     - scheduledShiftStartAt, scheduledShiftEndAt - должны быть переданы в разрезе 15-ти минутного
    интервала без секунд.
     - Максимальная длительность смены в графике 24 часа, минимальная 15 минут.
     - Добавлять смены в график можно не дальше чем на 31 день.
     - Добавлять смены в график можно только в будущем.
     - Запрещено добавлять курьеров производственные станции внутри заведения.
     - Запрещено добавлять работника заведения в график курьеров.
     - Список доступных производственных станций можно запросить в `Заведения → Производственные
    станции`
     - Список доступных должностей можно запросить в `Команда → Должности сотрудников`

    ---

     ### Требования к пользовательскому доступу:
     Требуется одна из ролей:
      - `Division administrator` - Администратор подразделения
      - `Store Manager` - Менеджер офиса

    Args:
        body (PostStaffSchedulesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorContract, ErrorContractBadRequest, PostStaffSchedulesResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostStaffSchedulesBody,
) -> Optional[Union[Any, ErrorContract, ErrorContractBadRequest, PostStaffSchedulesResponse200]]:
    """Команда → Расписания (создание)

     Создание расписания смен сотрудников.

    ### Требования к входным параметрам:
     - При добавлении нескольких смен на одного сотрудника они не должны пересекаться.
     - scheduledShiftStartAt и scheduledShiftEndAt необходимо передавать в UTC. Однако при получении
    графика будет отображаться уже локальное время.
     - scheduledShiftStartAt, scheduledShiftEndAt - должны быть переданы в разрезе 15-ти минутного
    интервала без секунд.
     - Максимальная длительность смены в графике 24 часа, минимальная 15 минут.
     - Добавлять смены в график можно не дальше чем на 31 день.
     - Добавлять смены в график можно только в будущем.
     - Запрещено добавлять курьеров производственные станции внутри заведения.
     - Запрещено добавлять работника заведения в график курьеров.
     - Список доступных производственных станций можно запросить в `Заведения → Производственные
    станции`
     - Список доступных должностей можно запросить в `Команда → Должности сотрудников`

    ---

     ### Требования к пользовательскому доступу:
     Требуется одна из ролей:
      - `Division administrator` - Администратор подразделения
      - `Store Manager` - Менеджер офиса

    Args:
        body (PostStaffSchedulesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorContract, ErrorContractBadRequest, PostStaffSchedulesResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
