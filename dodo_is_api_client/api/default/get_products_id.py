from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_products_id_response_400 import GetProductsIdResponse400
from ...models.product import Product
from ...types import Response


def _get_kwargs(
    id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/accounting/products/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetProductsIdResponse400, Product]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Product.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetProductsIdResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetProductsIdResponse400, Product]]:
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
) -> Response[Union[Any, GetProductsIdResponse400, Product]]:
    """Учёт → Информация о продукте

     Возвращает информацию о продукте

    Args:
        id (str):  Example: 000d3a240c719a8711e68aba13f7fe13.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetProductsIdResponse400, Product]]
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
) -> Optional[Union[Any, GetProductsIdResponse400, Product]]:
    """Учёт → Информация о продукте

     Возвращает информацию о продукте

    Args:
        id (str):  Example: 000d3a240c719a8711e68aba13f7fe13.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetProductsIdResponse400, Product]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, GetProductsIdResponse400, Product]]:
    """Учёт → Информация о продукте

     Возвращает информацию о продукте

    Args:
        id (str):  Example: 000d3a240c719a8711e68aba13f7fe13.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetProductsIdResponse400, Product]]
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
) -> Optional[Union[Any, GetProductsIdResponse400, Product]]:
    """Учёт → Информация о продукте

     Возвращает информацию о продукте

    Args:
        id (str):  Example: 000d3a240c719a8711e68aba13f7fe13.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetProductsIdResponse400, Product]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
