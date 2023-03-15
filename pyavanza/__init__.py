"""A python wrapper around the avanza api."""
import json
import logging
import urllib.error
import urllib.request
from typing import Any

import aiohttp

LOGGER = logging.getLogger(__name__)
AVANZA_API_STOCK_URL = "https://www.avanza.se/_api/market-guide/stock/{orderbook_id}"
AVANZA_API_STOCK_URL = (
    "https://www.avanza.se/_api/market-guide/exchangetradedfund/{orderbook_id}"
)


def get_url(url: str) -> dict[str, Any]:
    """Get url."""
    try:
        with urllib.request.urlopen(url) as resp:
            return json.loads(resp.read().decode("utf-8"))  # type: ignore
    except urllib.error.HTTPError as error:
        LOGGER.warning("HTTP Error %d: %s", error.code, error.reason)
    except urllib.error.URLError as error:
        LOGGER.warning("URL Error: %s", error.reason)
    return {}


async def get_url_async(session: aiohttp.ClientSession, url: str) -> dict[str, Any]:
    """Get url asynchronously."""
    try:
        resp = await session.get(url, raise_for_status=True)
        return await resp.json()  # type: ignore
    except aiohttp.ClientResponseError as error:
        LOGGER.warning("Response Error %d: %s", error.status, error.message)
    except aiohttp.ClientConnectionError as error:
        LOGGER.warning("Connection Error: %s", error)
    return {}


def get_stock(orderbook_id: int) -> dict[str, Any]:
    """Get latest information of a stock."""
    url = AVANZA_API_STOCK_URL.format(orderbook_id=orderbook_id)
    return get_url(url)


async def get_stock_async(
    session: aiohttp.ClientSession, orderbook_id: int
) -> dict[str, Any]:
    """Get latest information of a stock asynchronously."""
    url = AVANZA_API_STOCK_URL.format(orderbook_id=orderbook_id)
    return await get_url_async(session, url)


def get_etf(orderbook_id: int) -> dict[str, Any]:
    """Get latest information of an etf."""
    url = AVANZA_API_ETF_URL.format(orderbook_id=orderbook_id)
    return get_url(url)


async def get_etf_async(
    session: aiohttp.ClientSession, orderbook_id: int
) -> dict[str, Any]:
    """Get latest information of an etf asynchronously."""
    url = AVANZA_API_ETF_URL.format(orderbook_id=orderbook_id)
    return await get_url_async(session, url)
