"""Test the api."""
import urllib.error

import aiohttp
import pytest
from aiohttp.test_utils import make_mocked_coro

import pyavanza

ORDERBOOK_ID_AVANZA_BANK_HOLDING = 5361
ORDERBOOK_ID_XACT_BEAR = 12251
ORDERBOOK_ID_XACT_BULL = 12252

ORDERBOOK_IDS_STOCK = [
    ORDERBOOK_ID_AVANZA_BANK_HOLDING,
]
ORDERBOOK_IDS_ETF = [
    ORDERBOOK_ID_XACT_BEAR,
    ORDERBOOK_ID_XACT_BULL,
]


def check_stock_info(info, orderbook_id):
    """Check retrieved stock info."""
    assert isinstance(info, dict)
    assert int(info["orderbookId"]) == orderbook_id
    assert info["type"] == "STOCK"


def check_etf_info(info, orderbook_id):
    """Check retrieved etf info."""
    assert isinstance(info, dict)
    assert int(info["orderbookId"]) == orderbook_id
    assert info["type"] == "EXCHANGE_TRADED_FUND"


def make_mocked_session(mocker):
    """Create a mocked session for asyn tests."""
    mock_session = mocker.Mock()
    mock_session.get = make_mocked_coro()
    return mock_session


def test_get_url_http_error(mocker):
    """Check that http error is handled."""
    mock_urlopen = mocker.patch("pyavanza.urllib.request.urlopen")
    mock_urlopen.side_effect = urllib.error.HTTPError("", 404, "", {}, None)
    info = pyavanza.get_url("")
    assert info == {}


def test_get_url_url_error(mocker):
    """Check that url error is handled."""
    mock_urlopen = mocker.patch("pyavanza.urllib.request.urlopen")
    mock_urlopen.side_effect = urllib.error.URLError("")
    info = pyavanza.get_url("")
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


@pytest.mark.asyncio
async def test_get_url_async_client_response_error(mocker):
    """Check that client response error is handled."""
    mock_session = make_mocked_session(mocker)
    mock_session.get.side_effect = aiohttp.ClientResponseError(None, None)
    info = await pyavanza.get_url_async(mock_session, "")
    assert info == {}


@pytest.mark.asyncio
async def test_get_url_async_client_connection_error(mocker):
    """Check that client connection error is handled."""
    mock_session = make_mocked_session(mocker)
    mock_session.get.side_effect = aiohttp.ClientConnectionError(None)
    info = await pyavanza.get_url_async(mock_session, "")
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
