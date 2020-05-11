"""A Python wrapper around the Avanza mobile API."""
import json
import logging
import urllib.request

from aiohttp import ClientSession

AVANZA_API_BASE_URL = "https://www.avanza.se/_mobile/market"


def get_stock(id: int) -> dict:
    """Get latest information of a stock."""
    url = "{}/stock/{}".format(AVANZA_API_BASE_URL, id)
    req = urllib.request.Request(url)

    try:
        resp = urllib.request.urlopen(req).read()
        return json.loads(resp.decode())
    except Exception as e:
        logging.getLogger(__name__).error(e)
        return {}


async def get_stock_async(session: ClientSession, id: int) -> dict:
    """Get latest information of a stock asynchronously."""
    url = "{}/stock/{}".format(AVANZA_API_BASE_URL, id)
    async with session.get(url) as resp:
        if resp.status == 200:
            return await resp.json()
        else:
            return {}
