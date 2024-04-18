from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_delivery_sectors_response_200 import GetDeliverySectorsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    units: str,
    show_deleted: Union[Unset, bool] = UNSET,
    show_sub_sectors: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["units"] = units

    params["showDeleted"] = show_deleted

    params["showSubSectors"] = show_sub_sectors

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/delivery/delivery-sectors",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetDeliverySectorsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetDeliverySectorsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetDeliverySectorsResponse200]]:
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
    show_deleted: Union[Unset, bool] = UNSET,
    show_sub_sectors: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, GetDeliverySectorsResponse200]]:
    """Доставка → Сектора доставки

     Возвращает данные о секторах доставки

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 отделов в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        show_deleted (Union[Unset, bool]):
        show_sub_sectors (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetDeliverySectorsResponse200]]
    """

    kwargs = _get_kwargs(
        units=units,
        show_deleted=show_deleted,
        show_sub_sectors=show_sub_sectors,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    units: str,
    show_deleted: Union[Unset, bool] = UNSET,
    show_sub_sectors: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, GetDeliverySectorsResponse200]]:
    """Доставка → Сектора доставки

     Возвращает данные о секторах доставки

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 отделов в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        show_deleted (Union[Unset, bool]):
        show_sub_sectors (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetDeliverySectorsResponse200]
    """

    return sync_detailed(
        client=client,
        units=units,
        show_deleted=show_deleted,
        show_sub_sectors=show_sub_sectors,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    units: str,
    show_deleted: Union[Unset, bool] = UNSET,
    show_sub_sectors: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, GetDeliverySectorsResponse200]]:
    """Доставка → Сектора доставки

     Возвращает данные о секторах доставки

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 отделов в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        show_deleted (Union[Unset, bool]):
        show_sub_sectors (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetDeliverySectorsResponse200]]
    """

    kwargs = _get_kwargs(
        units=units,
        show_deleted=show_deleted,
        show_sub_sectors=show_sub_sectors,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    units: str,
    show_deleted: Union[Unset, bool] = UNSET,
    show_sub_sectors: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, GetDeliverySectorsResponse200]]:
    """Доставка → Сектора доставки

     Возвращает данные о секторах доставки

    ### Требования к query параметрам:
    1. В `units` можно перечислить до 30 отделов в одном запросе;
    2. В `units` следует перечислять UUID-ы строго через запятую без пробелов;

    > #### Доступно для следующих ролей:
    >
    >   `Division administrator` - Администратор подразделения
    >
    >   `Store Manager` - Менеджер офиса

    Args:
        units (str):  Example: 000d3a240c719a8711e68aba13f7f862,000d3a240c719a8711e68aba13f7fc8a,0
            00d3a240c719a8711e68aba13f7fe13.
        show_deleted (Union[Unset, bool]):
        show_sub_sectors (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetDeliverySectorsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            units=units,
            show_deleted=show_deleted,
            show_sub_sectors=show_sub_sectors,
        )
    ).parsed
