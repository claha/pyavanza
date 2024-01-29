"""A python wrapper around the avanza api."""

import json
import logging
import urllib.error
import urllib.request
from enum import Enum
from typing import Any

import aiohttp

LOGGER = logging.getLogger(__name__)

AVANZA_API_ENDPOINT = "https://www.avanza.se/_api"
AVANZA_API_STOCK_URL = AVANZA_API_ENDPOINT + "/market-guide/stock/{orderbook_id}"
AVANZA_API_ETF_URL = AVANZA_API_ENDPOINT + "/market-etf/{orderbook_id}"
AVANZA_API_INDEX_URL = AVANZA_API_ENDPOINT + "/market-index/{orderbook_id}"
AVANZA_API_SEARCH_URL = AVANZA_API_ENDPOINT + "/search/global-search?limit={limit}"


class InstrumentType(str, Enum):
    """Instrument types enum."""

    ExchangeTradedFund = "EXCHANGE_TRADED_FUND"
    Fund = "FUND"
    Index = "INDEX"
    Option = "OPTION"
    Stock = "STOCK"


def request_url(url: str, data: dict[str, Any] = {}) -> dict[str, Any]:
    """Make a GET or POST request based on the presence of data."""
    try:
        if data:
            # If data is provided, make a POST request
            data_json = json.dumps(data).encode("utf-8")
            request = urllib.request.Request(
                url, data=data_json, headers={"Content-Type": "application/json"}
            )
        else:
            # If no data is provided, make a GET request
            request = urllib.request.Request(url)

        with urllib.request.urlopen(request) as resp:
            return json.loads(resp.read().decode("utf-8"))  # type: ignore
    except urllib.error.HTTPError as error:
        LOGGER.warning("HTTP Error %d: %s", error.code, error.reason)
    except urllib.error.URLError as error:
        LOGGER.warning("URL Error: %s", error.reason)
    return {}


async def request_url_async(
    session: aiohttp.ClientSession, url: str, data: dict[str, Any] = {}
) -> dict[str, Any]:
    """Make an asynchronous GET or POST request based on the presence of data."""
    try:
        if data:
            # If data is provided, make an asynchronous POST request
            headers = {"Content-Type": "application/json"}
            async with session.post(
                url, data=json.dumps(data).encode("utf-8"), headers=headers
            ) as resp:
                return await resp.json()  # type: ignore
        else:
            # If no data is provided, make an asynchronous GET request
            async with session.get(url, raise_for_status=True) as resp:
                return await resp.json()  # type: ignore
    except aiohttp.ClientResponseError as error:
        LOGGER.warning("Response Error %d: %s", error.status, error.message)
    except aiohttp.ClientConnectionError as error:
        LOGGER.warning("Connection Error: %s", error)
    return {}


def get_stock(orderbook_id: int) -> dict[str, Any]:
    """Get latest information of a stock."""
    url = AVANZA_API_STOCK_URL.format(orderbook_id=orderbook_id)
    return request_url(url)


async def get_stock_async(
    session: aiohttp.ClientSession, orderbook_id: int
) -> dict[str, Any]:
    """Get latest information of a stock asynchronously."""
    url = AVANZA_API_STOCK_URL.format(orderbook_id=orderbook_id)
    return await request_url_async(session, url)


def get_etf(orderbook_id: int) -> dict[str, Any]:
    """Get latest information of an etf."""
    url = AVANZA_API_ETF_URL.format(orderbook_id=orderbook_id)
    return request_url(url)


async def get_etf_async(
    session: aiohttp.ClientSession, orderbook_id: int
) -> dict[str, Any]:
    """Get latest information of an etf asynchronously."""
    url = AVANZA_API_ETF_URL.format(orderbook_id=orderbook_id)
    return await request_url_async(session, url)


def get_index(orderbook_id: int) -> dict[str, Any]:
    """Get latest information of an index."""
    url = AVANZA_API_INDEX_URL.format(orderbook_id=orderbook_id)
    return request_url(url)


async def get_index_async(
    session: aiohttp.ClientSession, orderbook_id: int
) -> dict[str, Any]:
    """Get latest information of an index asynchronously."""
    url = AVANZA_API_INDEX_URL.format(orderbook_id=orderbook_id)
    return await request_url_async(session, url)


def search(query: str, limit: int = 10) -> dict[str, Any]:
    """Search for instruments."""
    url = AVANZA_API_SEARCH_URL.format(limit=limit)
    return request_url(url, data={"query": query})


async def search_async(
    session: aiohttp.ClientSession, query: str, limit: int = 10
) -> dict[str, Any]:
    """Search for instruments asynchronously."""
    url = AVANZA_API_SEARCH_URL.format(limit=limit)
    return await request_url_async(session, url, data={"query": query})
