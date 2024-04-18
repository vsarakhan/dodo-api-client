import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.staff_members_search_response import StaffMembersSearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    first_name: Union[None, Unset, str] = UNSET,
    last_name: Union[None, Unset, str] = UNSET,
    patronymic_name: Union[None, Unset, str] = UNSET,
    taxpayer_identification_number: Union[None, Unset, str] = UNSET,
    phone_number: Union[None, Unset, str] = UNSET,
    date_of_birth: Union[None, Unset, datetime.date] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_first_name: Union[None, Unset, str]
    if isinstance(first_name, Unset):
        json_first_name = UNSET
    else:
        json_first_name = first_name
    params["firstName"] = json_first_name

    json_last_name: Union[None, Unset, str]
    if isinstance(last_name, Unset):
        json_last_name = UNSET
    else:
        json_last_name = last_name
    params["lastName"] = json_last_name

    json_patronymic_name: Union[None, Unset, str]
    if isinstance(patronymic_name, Unset):
        json_patronymic_name = UNSET
    else:
        json_patronymic_name = patronymic_name
    params["patronymicName"] = json_patronymic_name

    json_taxpayer_identification_number: Union[None, Unset, str]
    if isinstance(taxpayer_identification_number, Unset):
        json_taxpayer_identification_number = UNSET
    else:
        json_taxpayer_identification_number = taxpayer_identification_number
    params["taxpayerIdentificationNumber"] = json_taxpayer_identification_number

    json_phone_number: Union[None, Unset, str]
    if isinstance(phone_number, Unset):
        json_phone_number = UNSET
    else:
        json_phone_number = phone_number
    params["phoneNumber"] = json_phone_number

    json_date_of_birth: Union[None, Unset, str]
    if isinstance(date_of_birth, Unset):
        json_date_of_birth = UNSET
    elif isinstance(date_of_birth, datetime.date):
        json_date_of_birth = date_of_birth.isoformat()
    else:
        json_date_of_birth = date_of_birth
    params["dateOfBirth"] = json_date_of_birth

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/staff/members/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, StaffMembersSearchResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StaffMembersSearchResponse.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, StaffMembersSearchResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    first_name: Union[None, Unset, str] = UNSET,
    last_name: Union[None, Unset, str] = UNSET,
    patronymic_name: Union[None, Unset, str] = UNSET,
    taxpayer_identification_number: Union[None, Unset, str] = UNSET,
    phone_number: Union[None, Unset, str] = UNSET,
    date_of_birth: Union[None, Unset, datetime.date] = UNSET,
) -> Response[Union[Any, StaffMembersSearchResponse]]:
    """Команда → Поиск сотрудников

     Возвращает список сотрудников с данными о трудоустройстве.
    Для поиска используется алгоритм, который описан ниже, а результирующие персональные данные
    скрываются.

    ### ВАЖНО:
    Алгоритм рассматривает только указанные ниже группы совпадений!

    ## Группировка запросов для алгоритма поиска

    ### 6 совпадений:

    Фамилия - Имя - Отчество - Номер телефона - Дата Рождения - ИНН

    ### 5 совпадений:

    Фамилия - Имя - Номер телефона - Дата Рождения - ИНН

    ### 4 совпадения:

    Фамилия - Имя - Номер телефона - Дата Рождения

    ### 3 совпадения:

    Фамилия - Имя - Номер телефона

    Фамилия - Имя - Дата Рождения

    Фамилия - Имя - ИНН

    ### 2 совпадения:

    Фамилия - Имя

    Фамилия - Номер телефона

    Фамилия - Дата рождения

    Фамилия - ИНН

    ### 1 совпадение:

    Номер телефона

    ИНН

    ### Требования к query параметрам:
    Если входные параметры поиска не попадают ни в одну из указанных групп, то вернется пустой результат

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены

    Args:
        first_name (Union[None, Unset, str]):  Example: Иван.
        last_name (Union[None, Unset, str]):  Example: Иванов.
        patronymic_name (Union[None, Unset, str]):  Example: Иванович.
        taxpayer_identification_number (Union[None, Unset, str]):  Example: 123456789112.
        phone_number (Union[None, Unset, str]):  Example: +79095991202.
        date_of_birth (Union[None, Unset, datetime.date]):  Example: 1995-06-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StaffMembersSearchResponse]]
    """

    kwargs = _get_kwargs(
        first_name=first_name,
        last_name=last_name,
        patronymic_name=patronymic_name,
        taxpayer_identification_number=taxpayer_identification_number,
        phone_number=phone_number,
        date_of_birth=date_of_birth,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    first_name: Union[None, Unset, str] = UNSET,
    last_name: Union[None, Unset, str] = UNSET,
    patronymic_name: Union[None, Unset, str] = UNSET,
    taxpayer_identification_number: Union[None, Unset, str] = UNSET,
    phone_number: Union[None, Unset, str] = UNSET,
    date_of_birth: Union[None, Unset, datetime.date] = UNSET,
) -> Optional[Union[Any, StaffMembersSearchResponse]]:
    """Команда → Поиск сотрудников

     Возвращает список сотрудников с данными о трудоустройстве.
    Для поиска используется алгоритм, который описан ниже, а результирующие персональные данные
    скрываются.

    ### ВАЖНО:
    Алгоритм рассматривает только указанные ниже группы совпадений!

    ## Группировка запросов для алгоритма поиска

    ### 6 совпадений:

    Фамилия - Имя - Отчество - Номер телефона - Дата Рождения - ИНН

    ### 5 совпадений:

    Фамилия - Имя - Номер телефона - Дата Рождения - ИНН

    ### 4 совпадения:

    Фамилия - Имя - Номер телефона - Дата Рождения

    ### 3 совпадения:

    Фамилия - Имя - Номер телефона

    Фамилия - Имя - Дата Рождения

    Фамилия - Имя - ИНН

    ### 2 совпадения:

    Фамилия - Имя

    Фамилия - Номер телефона

    Фамилия - Дата рождения

    Фамилия - ИНН

    ### 1 совпадение:

    Номер телефона

    ИНН

    ### Требования к query параметрам:
    Если входные параметры поиска не попадают ни в одну из указанных групп, то вернется пустой результат

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены

    Args:
        first_name (Union[None, Unset, str]):  Example: Иван.
        last_name (Union[None, Unset, str]):  Example: Иванов.
        patronymic_name (Union[None, Unset, str]):  Example: Иванович.
        taxpayer_identification_number (Union[None, Unset, str]):  Example: 123456789112.
        phone_number (Union[None, Unset, str]):  Example: +79095991202.
        date_of_birth (Union[None, Unset, datetime.date]):  Example: 1995-06-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StaffMembersSearchResponse]
    """

    return sync_detailed(
        client=client,
        first_name=first_name,
        last_name=last_name,
        patronymic_name=patronymic_name,
        taxpayer_identification_number=taxpayer_identification_number,
        phone_number=phone_number,
        date_of_birth=date_of_birth,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    first_name: Union[None, Unset, str] = UNSET,
    last_name: Union[None, Unset, str] = UNSET,
    patronymic_name: Union[None, Unset, str] = UNSET,
    taxpayer_identification_number: Union[None, Unset, str] = UNSET,
    phone_number: Union[None, Unset, str] = UNSET,
    date_of_birth: Union[None, Unset, datetime.date] = UNSET,
) -> Response[Union[Any, StaffMembersSearchResponse]]:
    """Команда → Поиск сотрудников

     Возвращает список сотрудников с данными о трудоустройстве.
    Для поиска используется алгоритм, который описан ниже, а результирующие персональные данные
    скрываются.

    ### ВАЖНО:
    Алгоритм рассматривает только указанные ниже группы совпадений!

    ## Группировка запросов для алгоритма поиска

    ### 6 совпадений:

    Фамилия - Имя - Отчество - Номер телефона - Дата Рождения - ИНН

    ### 5 совпадений:

    Фамилия - Имя - Номер телефона - Дата Рождения - ИНН

    ### 4 совпадения:

    Фамилия - Имя - Номер телефона - Дата Рождения

    ### 3 совпадения:

    Фамилия - Имя - Номер телефона

    Фамилия - Имя - Дата Рождения

    Фамилия - Имя - ИНН

    ### 2 совпадения:

    Фамилия - Имя

    Фамилия - Номер телефона

    Фамилия - Дата рождения

    Фамилия - ИНН

    ### 1 совпадение:

    Номер телефона

    ИНН

    ### Требования к query параметрам:
    Если входные параметры поиска не попадают ни в одну из указанных групп, то вернется пустой результат

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены

    Args:
        first_name (Union[None, Unset, str]):  Example: Иван.
        last_name (Union[None, Unset, str]):  Example: Иванов.
        patronymic_name (Union[None, Unset, str]):  Example: Иванович.
        taxpayer_identification_number (Union[None, Unset, str]):  Example: 123456789112.
        phone_number (Union[None, Unset, str]):  Example: +79095991202.
        date_of_birth (Union[None, Unset, datetime.date]):  Example: 1995-06-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StaffMembersSearchResponse]]
    """

    kwargs = _get_kwargs(
        first_name=first_name,
        last_name=last_name,
        patronymic_name=patronymic_name,
        taxpayer_identification_number=taxpayer_identification_number,
        phone_number=phone_number,
        date_of_birth=date_of_birth,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    first_name: Union[None, Unset, str] = UNSET,
    last_name: Union[None, Unset, str] = UNSET,
    patronymic_name: Union[None, Unset, str] = UNSET,
    taxpayer_identification_number: Union[None, Unset, str] = UNSET,
    phone_number: Union[None, Unset, str] = UNSET,
    date_of_birth: Union[None, Unset, datetime.date] = UNSET,
) -> Optional[Union[Any, StaffMembersSearchResponse]]:
    """Команда → Поиск сотрудников

     Возвращает список сотрудников с данными о трудоустройстве.
    Для поиска используется алгоритм, который описан ниже, а результирующие персональные данные
    скрываются.

    ### ВАЖНО:
    Алгоритм рассматривает только указанные ниже группы совпадений!

    ## Группировка запросов для алгоритма поиска

    ### 6 совпадений:

    Фамилия - Имя - Отчество - Номер телефона - Дата Рождения - ИНН

    ### 5 совпадений:

    Фамилия - Имя - Номер телефона - Дата Рождения - ИНН

    ### 4 совпадения:

    Фамилия - Имя - Номер телефона - Дата Рождения

    ### 3 совпадения:

    Фамилия - Имя - Номер телефона

    Фамилия - Имя - Дата Рождения

    Фамилия - Имя - ИНН

    ### 2 совпадения:

    Фамилия - Имя

    Фамилия - Номер телефона

    Фамилия - Дата рождения

    Фамилия - ИНН

    ### 1 совпадение:

    Номер телефона

    ИНН

    ### Требования к query параметрам:
    Если входные параметры поиска не попадают ни в одну из указанных групп, то вернется пустой результат

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса
    >
    >   `Shift supervisor` - Менеджер смены

    Args:
        first_name (Union[None, Unset, str]):  Example: Иван.
        last_name (Union[None, Unset, str]):  Example: Иванов.
        patronymic_name (Union[None, Unset, str]):  Example: Иванович.
        taxpayer_identification_number (Union[None, Unset, str]):  Example: 123456789112.
        phone_number (Union[None, Unset, str]):  Example: +79095991202.
        date_of_birth (Union[None, Unset, datetime.date]):  Example: 1995-06-01.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StaffMembersSearchResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            first_name=first_name,
            last_name=last_name,
            patronymic_name=patronymic_name,
            taxpayer_identification_number=taxpayer_identification_number,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
        )
    ).parsed
