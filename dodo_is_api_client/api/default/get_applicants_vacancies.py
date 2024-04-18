from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_contract import ErrorContract
from ...models.error_contract_bad_request import ErrorContractBadRequest
from ...models.get_applicants_vacancies_response_200 import GetApplicantsVacanciesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    localities: Union[Unset, str] = UNSET,
    units: Union[Unset, str] = UNSET,
    take: Union[Unset, int] = 100,
    skip: Union[Unset, int] = 0,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["localities"] = localities

    params["units"] = units

    params["take"] = take

    params["skip"] = skip

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/staff/vacancies",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorContract, ErrorContractBadRequest, GetApplicantsVacanciesResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetApplicantsVacanciesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, ErrorContract, ErrorContractBadRequest, GetApplicantsVacanciesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    localities: Union[Unset, str] = UNSET,
    units: Union[Unset, str] = UNSET,
    take: Union[Unset, int] = 100,
    skip: Union[Unset, int] = 0,
) -> Response[Union[Any, ErrorContract, ErrorContractBadRequest, GetApplicantsVacanciesResponse200]]:
    """Команда → Открытые вакансии

     Получение открытых вакансий в заведениях

    ### Требования к входным параметрам:
     - В `units` можно перечислить до 30 заведений в одном запросе;
     - В `units` следует перечислять UUID-ы строго через запятую без пробелов;
     - В `localities` можно перечислить до 30 населенных пунктов в одном запросе;
     - В `localities` следует перечислять UUID-ы строго через запятую без пробелов;
     - Можно передавать либо параметр `units` для получения вакансий по переданным заведениям либо
    параметр `localities` для получения вакансий по всем заведениям переданных населенных пунктов;
     - Если не передать ни `units` ни `localities` будут выданы все вакансии по всем заведениям;
      - Можно получить информацию только о вакансиях в Заведениях (пиццериях) и ПРЦ (Производственно-
    распределительный центр)

    Args:
        localities (Union[Unset, str]):
        units (Union[Unset, str]):  Example:
            000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        skip (Union[Unset, int]):  Default: 0. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorContract, ErrorContractBadRequest, GetApplicantsVacanciesResponse200]]
    """

    kwargs = _get_kwargs(
        localities=localities,
        units=units,
        take=take,
        skip=skip,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    localities: Union[Unset, str] = UNSET,
    units: Union[Unset, str] = UNSET,
    take: Union[Unset, int] = 100,
    skip: Union[Unset, int] = 0,
) -> Optional[Union[Any, ErrorContract, ErrorContractBadRequest, GetApplicantsVacanciesResponse200]]:
    """Команда → Открытые вакансии

     Получение открытых вакансий в заведениях

    ### Требования к входным параметрам:
     - В `units` можно перечислить до 30 заведений в одном запросе;
     - В `units` следует перечислять UUID-ы строго через запятую без пробелов;
     - В `localities` можно перечислить до 30 населенных пунктов в одном запросе;
     - В `localities` следует перечислять UUID-ы строго через запятую без пробелов;
     - Можно передавать либо параметр `units` для получения вакансий по переданным заведениям либо
    параметр `localities` для получения вакансий по всем заведениям переданных населенных пунктов;
     - Если не передать ни `units` ни `localities` будут выданы все вакансии по всем заведениям;
      - Можно получить информацию только о вакансиях в Заведениях (пиццериях) и ПРЦ (Производственно-
    распределительный центр)

    Args:
        localities (Union[Unset, str]):
        units (Union[Unset, str]):  Example:
            000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        skip (Union[Unset, int]):  Default: 0. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorContract, ErrorContractBadRequest, GetApplicantsVacanciesResponse200]
    """

    return sync_detailed(
        client=client,
        localities=localities,
        units=units,
        take=take,
        skip=skip,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    localities: Union[Unset, str] = UNSET,
    units: Union[Unset, str] = UNSET,
    take: Union[Unset, int] = 100,
    skip: Union[Unset, int] = 0,
) -> Response[Union[Any, ErrorContract, ErrorContractBadRequest, GetApplicantsVacanciesResponse200]]:
    """Команда → Открытые вакансии

     Получение открытых вакансий в заведениях

    ### Требования к входным параметрам:
     - В `units` можно перечислить до 30 заведений в одном запросе;
     - В `units` следует перечислять UUID-ы строго через запятую без пробелов;
     - В `localities` можно перечислить до 30 населенных пунктов в одном запросе;
     - В `localities` следует перечислять UUID-ы строго через запятую без пробелов;
     - Можно передавать либо параметр `units` для получения вакансий по переданным заведениям либо
    параметр `localities` для получения вакансий по всем заведениям переданных населенных пунктов;
     - Если не передать ни `units` ни `localities` будут выданы все вакансии по всем заведениям;
      - Можно получить информацию только о вакансиях в Заведениях (пиццериях) и ПРЦ (Производственно-
    распределительный центр)

    Args:
        localities (Union[Unset, str]):
        units (Union[Unset, str]):  Example:
            000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        skip (Union[Unset, int]):  Default: 0. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorContract, ErrorContractBadRequest, GetApplicantsVacanciesResponse200]]
    """

    kwargs = _get_kwargs(
        localities=localities,
        units=units,
        take=take,
        skip=skip,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    localities: Union[Unset, str] = UNSET,
    units: Union[Unset, str] = UNSET,
    take: Union[Unset, int] = 100,
    skip: Union[Unset, int] = 0,
) -> Optional[Union[Any, ErrorContract, ErrorContractBadRequest, GetApplicantsVacanciesResponse200]]:
    """Команда → Открытые вакансии

     Получение открытых вакансий в заведениях

    ### Требования к входным параметрам:
     - В `units` можно перечислить до 30 заведений в одном запросе;
     - В `units` следует перечислять UUID-ы строго через запятую без пробелов;
     - В `localities` можно перечислить до 30 населенных пунктов в одном запросе;
     - В `localities` следует перечислять UUID-ы строго через запятую без пробелов;
     - Можно передавать либо параметр `units` для получения вакансий по переданным заведениям либо
    параметр `localities` для получения вакансий по всем заведениям переданных населенных пунктов;
     - Если не передать ни `units` ни `localities` будут выданы все вакансии по всем заведениям;
      - Можно получить информацию только о вакансиях в Заведениях (пиццериях) и ПРЦ (Производственно-
    распределительный центр)

    Args:
        localities (Union[Unset, str]):
        units (Union[Unset, str]):  Example:
            000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a.
        take (Union[Unset, int]):  Default: 100. Example: 100.
        skip (Union[Unset, int]):  Default: 0. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorContract, ErrorContractBadRequest, GetApplicantsVacanciesResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            localities=localities,
            units=units,
            take=take,
            skip=skip,
        )
    ).parsed
