"""Test the api."""

import urllib.error

import aiohttp
import pytest
from aiohttp.test_utils import make_mocked_coro

import pyavanza

ORDERBOOK_ID_AVANZA_BANK_HOLDING = 5361
ORDERBOOK_ID_XACT_BEAR = 12251
ORDERBOOK_ID_XACT_BULL = 12252
ORDERBOOK_ID_OMX_STOCKHOLM_30 = 19002
ORDERBOOK_ID_USD_SEK = 19000

ORDERBOOK_IDS_STOCK = [
    ORDERBOOK_ID_AVANZA_BANK_HOLDING,
]
ORDERBOOK_IDS_ETF = [
    ORDERBOOK_ID_XACT_BEAR,
    ORDERBOOK_ID_XACT_BULL,
]
ORDERBOOK_IDS_INDEX = [
    ORDERBOOK_ID_OMX_STOCKHOLM_30,
    ORDERBOOK_ID_USD_SEK,
]
SEARCH_QUERIES = [
    "avanza",
    "xact",
    "omx",
]


def check_stock_info(info, orderbook_id):
    """Check retrieved stock info."""
    assert isinstance(info, dict)
    assert int(info["orderbookId"]) == orderbook_id
    assert info["type"] == pyavanza.InstrumentType.Stock


def check_etf_info(info, orderbook_id):
    """Check retrieved etf info."""
    assert isinstance(info, dict)
    assert int(info["orderbookId"]) == orderbook_id
    assert info["type"] == pyavanza.InstrumentType.ExchangeTradedFund


def check_index_info(info, orderbook_id):
    """Check retrieved index info."""
    assert isinstance(info, dict)
    assert int(info["orderbookId"]) == orderbook_id
    assert info["type"] == pyavanza.InstrumentType.Index


def check_search_info(info, query):
    """Check search info."""
    assert info["searchQuery"] == query
    hits = info["resultGroups"]
    for hit in hits:
        assert isinstance(
            pyavanza.InstrumentType(hit["instrumentType"]), pyavanza.InstrumentType
        )


def make_mocked_session(mocker):
    """Create a mocked session for asyn tests."""
    mock_session = mocker.Mock()
    mock_session.get = make_mocked_coro()
    return mock_session


def test_request_url_http_error(mocker):
    """Check that http error is handled."""
    mock_urlopen = mocker.patch("pyavanza.urllib.request.urlopen")
    mock_urlopen.side_effect = urllib.error.HTTPError("", 404, "", {}, None)
    info = pyavanza.request_url(pyavanza.AVANZA_API_ENDPOINT)
    assert info == {}


def test_request_url_url_error(mocker):
    """Check that url error is handled."""
    mock_urlopen = mocker.patch("pyavanza.urllib.request.urlopen")
    mock_urlopen.side_effect = urllib.error.URLError("")
    info = pyavanza.request_url(pyavanza.AVANZA_API_ENDPOINT)
    assert info == {}


@pytest.mark.parametrize("orderbook_id", ORDERBOOK_IDS_STOCK)
def test_get_stock(orderbook_id):
    """Retrieve and check stock info."""
    info = pyavanza.get_stock(orderbook_id)
    check_stock_info(info, orderbook_id)


@pytest.mark.parametrize("orderbook_id", ORDERBOOK_IDS_ETF)
def test_get_etf(orderbook_id):
    """Retrieve and check etf info."""
    info = pyavanza.get_etf(orderbook_id)
    check_etf_info(info, orderbook_id)


@pytest.mark.parametrize("orderbook_id", ORDERBOOK_IDS_INDEX)
def test_get_index(orderbook_id):
    """Retrieve and check index info."""
    info = pyavanza.get_index(orderbook_id)
    check_index_info(info, orderbook_id)


@pytest.mark.parametrize("query", SEARCH_QUERIES)
def test_search(query):
    """Search for query and check result."""
    info = pyavanza.search(query)
    check_search_info(info, query)


@pytest.mark.asyncio
async def test_request_url_async_client_response_error(mocker):
    """Check that client response error is handled."""
    mock_session = make_mocked_session(mocker)
    mock_session.get.side_effect = aiohttp.ClientResponseError(None, None)
    info = await pyavanza.request_url_async(mock_session, "")
    assert info == {}


@pytest.mark.asyncio
async def test_request_url_async_client_connection_error(mocker):
    """Check that client connection error is handled."""
    mock_session = make_mocked_session(mocker)
    mock_session.get.side_effect = aiohttp.ClientConnectionError(None)
    info = await pyavanza.request_url_async(mock_session, "")
    assert info == {}


@pytest.mark.asyncio
@pytest.mark.parametrize("orderbook_id", ORDERBOOK_IDS_STOCK)
async def test_get_stock_async(orderbook_id):
    """Retrieve and check stock info async."""
    async with aiohttp.ClientSession() as session:
        info = await pyavanza.get_stock_async(session, orderbook_id)
        check_stock_info(info, orderbook_id)


@pytest.mark.asyncio
@pytest.mark.parametrize("orderbook_id", ORDERBOOK_IDS_ETF)
async def test_get_etf_async(orderbook_id):
    """Retrieve and check etf info async."""
    async with aiohttp.ClientSession() as session:
        info = await pyavanza.get_etf_async(session, orderbook_id)
        check_etf_info(info, orderbook_id)


@pytest.mark.asyncio
@pytest.mark.parametrize("orderbook_id", ORDERBOOK_IDS_INDEX)
async def test_get_index_async(orderbook_id):
    """Retrieve and check index info async."""
    async with aiohttp.ClientSession() as session:
        info = await pyavanza.get_index_async(session, orderbook_id)
        check_index_info(info, orderbook_id)


@pytest.mark.asyncio
@pytest.mark.parametrize("query", SEARCH_QUERIES)
async def test_search_async(query):
    """Search for query and check result async."""
    async with aiohttp.ClientSession() as session:
        info = await pyavanza.search_async(session, query)
        check_search_info(info, query)
