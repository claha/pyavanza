"""A Python wrapper around the Avanza mobile API."""
import json
import logging
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, List

import aiohttp

from pyavanza.certificate import Certificate
from pyavanza.const import (
    AVANZA_API_CERTIFICATE_URL,
    AVANZA_API_FUND_URL,
    AVANZA_API_INDEX_URL,
    AVANZA_API_SEARCH_INSTRUMENT_URL,
    AVANZA_API_SEARCH_URL,
    AVANZA_API_STOCK_URL,
    InstrumentType,
)
from pyavanza.error import AvanzaParseError, AvanzaRequestError, AvanzaResponseError
from pyavanza.fund import Fund
from pyavanza.index import Index
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


def get_fund(id: int) -> Fund:
    """Get latest information of a fund."""
    url = AVANZA_API_FUND_URL.format(id=id)
    data = _api_call(url)
    return Fund(data)


def get_stock(id: int) -> Stock:
    """Get latest information of a stock."""
    url = AVANZA_API_STOCK_URL.format(id=id)
    data = _api_call(url)
    return Stock(data)


def get_index(id: int) -> Index:
    """Get latest information of a index."""
    url = AVANZA_API_INDEX_URL.format(id=id)
    data = _api_call(url)
    return Index(data)


def get_certificate(id: int) -> Certificate:
    """Get latest information of a certificate."""
    url = AVANZA_API_CERTIFICATE_URL.format(id=id)
    data = _api_call(url)
    return Certificate(data)


def search(
    query: str, limit: int = -1, instrument: InstrumentType = InstrumentType.ANY
) -> List[Instrument]:
    """Search for instruments."""
    url = _create_search_url(query, limit, instrument)
    data = _api_call(url)
    return parse_instruments(data)


async def get_fund_async(session: aiohttp.ClientSession, id: int) -> Fund:
    """Get latest information of a fund asynchronously."""
    url = AVANZA_API_FUND_URL.format(id=id)
    data = await _api_call_async(session, url)
    return Fund(data)


async def get_stock_async(session: aiohttp.ClientSession, id: int) -> Stock:
    """Get latest information of a stock asynchronously."""
    url = AVANZA_API_STOCK_URL.format(id=id)
    data = await _api_call_async(session, url)
    return Stock(data)


async def get_index_async(session: aiohttp.ClientSession, id: int) -> Index:
    """Get latest information of a stock asynchronously."""
    url = AVANZA_API_INDEX_URL.format(id=id)
    data = await _api_call_async(session, url)
    return Index(data)


async def get_certificate_async(session: aiohttp.ClientSession, id: int) -> Certificate:
    """Get latest information of a stock asynchronously."""
    url = AVANZA_API_CERTIFICATE_URL.format(id=id)
    data = await _api_call_async(session, url)
    return Certificate(data)


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
