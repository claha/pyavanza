"""A Python wrapper around the Avanza mobile API."""
import json
import logging
import urllib

import aiohttp

LOGGER = logging.getLogger(__name__)
AVANZA_API_BASE_URL = "https://www.avanza.se/_mobile/market"
AVANZA_API_STOCK_URL = AVANZA_API_BASE_URL + "/stock/{id}"


def get_stock(id: int) -> dict:
    """Get latest information of a stock."""
    url = AVANZA_API_STOCK_URL.format(id=id)
    try:
        resp = urllib.request.urlopen(url).read()
        return json.loads(resp.decode())
    except urllib.error.HTTPError as e:
        LOGGER.warning("HTTP Error %d: %s" % (e.code, e.reason))
    except urllib.error.URLError as e:
        LOGGER.warning("URL Error: %s" % (e.reason))
    return {}


async def get_stock_async(session: aiohttp.ClientSession, id: int) -> dict:
    """Get latest information of a stock asynchronously."""
    url = AVANZA_API_STOCK_URL.format(id=id)
    try:
        resp = await session.get(url, raise_for_status=True)
        return await resp.json()
    except aiohttp.ClientResponseError as e:
        LOGGER.warning("HTTP Error %d: %s" % (e.status, e.message))
    except aiohttp.ClientConnectionError as e:
        LOGGER.warning("URL Error [Errno %d] %s" % (e.errno, e.strerror))
    return {}
