"""A Python wrapper around the Avanza API."""
import json
import logging
import urllib.error
import urllib.request
from typing import Any, Dict

import aiohttp

LOGGER = logging.getLogger(__name__)
AVANZA_API_INSTRUMENT_URL = "https://www.avanza.se/_api/market-guide/{instrument_type}/{id}"

def get_instrument(instrument_type: str, id: int) -> Dict[str, Any]:
    """Get latest information."""
    url = AVANZA_API_INSTRUMENT_URL.format(instrument_type=instrument_type, id=id)
    try:
        resp = urllib.request.urlopen(url).read()
        return json.loads(resp.decode())  # type: ignore
    except urllib.error.HTTPError as e:
        LOGGER.warning("HTTP Error %d: %s" % (e.code, e.reason))
    except urllib.error.URLError as e:
        LOGGER.warning("URL Error: %s" % (e.reason))
    return {}


async def get_instrument_async(session: aiohttp.ClientSession, instrument_type: str, id: int) -> Dict[str, Any]:
    """Get latest information asynchronously."""
    url = AVANZA_API_INSTRUMENT_URL.format(instrument_type=instrument_type, id=id)
    try:
        resp = await session.get(url, raise_for_status=True)
        return await resp.json()  # type: ignore
    except aiohttp.ClientResponseError as e:
        LOGGER.warning("Response Error %d: %s" % (e.status, e.message))
    except aiohttp.ClientConnectionError as e:
        LOGGER.warning("Connection Error: %s" % (e))
    return {}
