"""Test stock async."""
import asyncio
import json
import unittest
from unittest.mock import Mock

import aiohttp
from aiohttp.test_utils import make_mocked_coro

import pyavanza


def sync(coro):
    """Use this wrapper to run an test asynchronously."""

    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(coro(*args, **kwargs))

    return wrapper


class TestStockAsync(unittest.TestCase):
    """Tests that retrieve stock information asynchronously."""

    def shortDescription(self):
        """Disable printing of docstring in test runner."""
        return None

    def setUp(self):
        """Set up, runs before each test."""
        self.mock_session = Mock()
        mock_get = make_mocked_coro()
        self.mock_session.get = mock_get

    @sync
    async def test_get_stock_fail_request_error(self):
        """Test that triggers a request error."""
        id = 1234
        self.mock_session.get.side_effect = aiohttp.ClientConnectionError(None)

        with self.assertRaises(pyavanza.AvanzaRequestError):
            await pyavanza.get_stock_async(self.mock_session, id)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_STOCK_URL.format(id=id), raise_for_status=True
        )

    @sync
    async def test_get_stock_fail_response_error(self):
        """Test that triggers a response error.."""
        id = 1234
        self.mock_session.get.side_effect = aiohttp.ClientResponseError(None, None)

        with self.assertRaises(pyavanza.AvanzaResponseError):
            await pyavanza.get_stock_async(self.mock_session, id)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_STOCK_URL.format(id=id), raise_for_status=True
        )

    @sync
    async def test_get_stock_parse_error(self):
        """Test that triggers a parse error."""
        id = 1234
        mock_resp = Mock()
        mock_resp.json = make_mocked_coro()
        mock_resp.json.side_effect = json.JSONDecodeError(None, "", 0)
        self.mock_session.get = make_mocked_coro(return_value=mock_resp)

        with self.assertRaises(pyavanza.AvanzaParseError):
            await pyavanza.get_stock_async(self.mock_session, id)

    @sync
    async def test_get_stock_success(self):
        """Test a successful request and response."""
        id = 1234
        mock_resp = Mock()
        mock_resp.json = make_mocked_coro(return_value={"id": id})
        self.mock_session.get = make_mocked_coro(return_value=mock_resp)

        data = await pyavanza.get_stock_async(self.mock_session, id)
        self.assertEqual(len(data), 1)
        self.assertTrue("id" in data)
        self.assertEqual(data["id"], id)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_STOCK_URL.format(id=id), raise_for_status=True
        )
