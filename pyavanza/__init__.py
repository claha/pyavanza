"""A Python wrapper around the Avanza mobile API."""
import json
import logging
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict

import aiohttp

from .const import (
    AVANZA_API_SEARCH_INSTRUMENT_URL,
    AVANZA_API_SEARCH_URL,
    AVANZA_API_STOCK_URL,
    Instrument,
)

LOGGER = logging.getLogger(__name__)


def _api_call(url: str) -> Dict[str, Any]:
    """Make an api call."""
    try:
        resp = urllib.request.urlopen(url).read()
        return json.loads(resp.decode())  # type: ignore
    except urllib.error.HTTPError as e:
        LOGGER.warning("HTTP Error %d: %s" % (e.code, e.reason))
    except urllib.error.URLError as e:
        LOGGER.warning("URL Error: %s" % (e.reason))
    return {}


def get_stock(id: int) -> Dict[str, Any]:
    """Get latest information of a stock."""
    url = AVANZA_API_STOCK_URL.format(id=id)
    return _api_call(url)


def search(
    query: str, limit: int = -1, instrument: Instrument = Instrument.ANY
) -> Dict[str, Any]:
    """Search for instruments."""
    query = urllib.parse.quote(query)
    if instrument is not Instrument.ANY:
        url = AVANZA_API_SEARCH_INSTRUMENT_URL.format(
            instrument=instrument.value, query=query, limit=limit
        )
    else:
        url = AVANZA_API_SEARCH_URL.format(query=query, limit=limit)
    return _api_call(url)


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
