"""A Python wrapper around the Avanza mobile API."""
import json
import logging
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, List

import aiohttp

from pyavanza.const import (
    AVANZA_API_SEARCH_INSTRUMENT_URL,
    AVANZA_API_SEARCH_URL,
    AVANZA_API_STOCK_URL,
    InstrumentType,
)
from pyavanza.error import AvanzaParseError, AvanzaRequestError, AvanzaResponseError
from pyavanza.instrument import Instrument, parse_instruments
from pyavanza.stock import Stock

LOGGER = logging.getLogger(__name__)


def _api_call(url: str) -> Dict[str, Any]:
    """Make an api call."""
    try:
        resp = urllib.request.urlopen(url).read()
    except urllib.error.HTTPError as e:
        raise AvanzaResponseError(e.code, e.reason)
    except urllib.error.URLError as e:
        raise AvanzaRequestError(str(e))
    try:
        return json.loads(resp.decode())  # type: ignore
    except json.JSONDecodeError as e:
        raise AvanzaParseError(str(e))


async def _api_call_async(session: aiohttp.ClientSession, url: str) -> Dict[str, Any]:
    """Make an api call asynchronously."""
    try:
        resp = await session.get(url, raise_for_status=True)
    except aiohttp.ClientResponseError as e:
        raise AvanzaResponseError(e.status, e.message)
    except aiohttp.ClientConnectionError as e:
        raise AvanzaRequestError(str(e))
    try:
        return await resp.json()  # type: ignore
    except json.JSONDecodeError as e:
        raise AvanzaParseError(str(e))


def _create_search_url(query: str, limit: int, instrument: InstrumentType) -> str:
    """Create search url."""
    query = urllib.parse.quote(query)
    if instrument is not InstrumentType.ANY:
        url = AVANZA_API_SEARCH_INSTRUMENT_URL.format(
            instrument=instrument.value, query=query, limit=limit
        )
    else:
        url = AVANZA_API_SEARCH_URL.format(query=query, limit=limit)
    return url


def get_stock(id: int) -> Stock:
    """Get latest information of a stock."""
    url = AVANZA_API_STOCK_URL.format(id=id)
    data = _api_call(url)
    return Stock(data)


def search(
    query: str, limit: int = -1, instrument: InstrumentType = InstrumentType.ANY
) -> List[Instrument]:
    """Search for instruments."""
    url = _create_search_url(query, limit, instrument)
    data = _api_call(url)
    return parse_instruments(data)


async def get_stock_async(session: aiohttp.ClientSession, id: int) -> Stock:
    """Get latest information of a stock asynchronously."""
    url = AVANZA_API_STOCK_URL.format(id=id)
    data = await _api_call_async(session, url)
    return Stock(data)


async def search_async(
    session: aiohttp.ClientSession,
    query: str,
    limit: int = -1,
    instrument: InstrumentType = InstrumentType.ANY,
) -> List[Instrument]:
    """Search for instruments asynchronously."""
    url = _create_search_url(query, limit, instrument)
    data = await _api_call_async(session, url)
    return parse_instruments(data)
