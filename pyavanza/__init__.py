"""A Python wrapper around the Avanza mobile API."""
import json
import logging
import urllib.error
import urllib.request
from typing import Any, Dict

import aiohttp

LOGGER = logging.getLogger(__name__)
AVANZA_API_BASE_URL = "https://www.avanza.se/_api/market-guide"
AVANZA_API_STOCK_URL = AVANZA_API_BASE_URL + "/stock/{id}"


def get_stock(id: int) -> Dict[str, Any]:
    """Get latest information of a stock."""
    url = AVANZA_API_STOCK_URL.format(id=id)
    try:
        resp = urllib.request.urlopen(url).read()
        return json.loads(resp.decode())  # type: ignore
    except urllib.error.HTTPError as e:
        LOGGER.warning("HTTP Error %d: %s" % (e.code, e.reason))
    except urllib.error.URLError as e:
        LOGGER.warning("URL Error: %s" % (e.reason))
    return {}


async def get_stock_async(session: aiohttp.ClientSession, id: int) -> Dict[str, Any]:
    """Get latest information of a stock asynchronously."""
    url = AVANZA_API_STOCK_URL.format(id=id)
    try:
        resp = await session.get(url, raise_for_status=True)
        return await resp.json()  # type: ignore
    except aiohttp.ClientResponseError as e:
        LOGGER.warning("Response Error %d: %s" % (e.status, e.message))
    except aiohttp.ClientConnectionError as e:
        LOGGER.warning("Connection Error: %s" % (e))
    return {}
