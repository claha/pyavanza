"""A python wrapper around the avanza api."""
import json
import logging
import urllib.error
import urllib.request
from typing import Any

import aiohttp  # pylint: disable=import-error

LOGGER = logging.getLogger(__name__)
AVANZA_API_STOCK_URL = "https://www.avanza.se/_api/market-guide/stock/{orderbook_id}"


def get_stock(orderbook_id: int) -> dict[str, Any]:
    """Get latest information of a stock."""
    url = AVANZA_API_STOCK_URL.format(orderbook_id=orderbook_id)
    try:
        with urllib.request.urlopen(url) as resp:
            return json.loads(resp.decode())  # type: ignore
    except urllib.error.HTTPError as error:
        LOGGER.warning("HTTP Error %d: %s", error.code, error.reason)
    except urllib.error.URLError as error:
        LOGGER.warning("URL Error: %s", error.reason)
    return {}


async def get_stock_async(
    session: aiohttp.ClientSession, orderbook_id: int
) -> dict[str, Any]:
    """Get latest information of a stock asynchronously."""
    url = AVANZA_API_STOCK_URL.format(orderbook_id=orderbook_id)
    try:
        resp = await session.get(url, raise_for_status=True)
        return await resp.json()  # type: ignore
    except aiohttp.ClientResponseError as error:
        LOGGER.warning("Response Error %d: %s", error.status, error.message)
    except aiohttp.ClientConnectionError as error:
        LOGGER.warning("Connection Error: %s", error)
    return {}
