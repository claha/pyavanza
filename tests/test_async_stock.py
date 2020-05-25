"""Test stock async."""
import json
from unittest.mock import Mock

import aiohttp
from aiohttp.test_utils import make_mocked_coro

import pyavanza
import tests.common as common


class TestStockAsync(common.TestCase):
    """Tests that retrieve stock information asynchronously."""

    def setUp(self):
        """Set up, runs before each test."""
        self.mock_session = Mock()
        mock_get = make_mocked_coro()
        self.mock_session.get = mock_get

    @common.sync
    async def test_get_stock_fail_request_error(self):
        """Test that triggers a request error."""
        id = 1234
        self.mock_session.get.side_effect = aiohttp.ClientConnectionError(None)

        with self.assertRaises(pyavanza.AvanzaRequestError):
            await pyavanza.get_stock_async(self.mock_session, id)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_STOCK_URL.format(id=id), raise_for_status=True
        )

    @common.sync
    async def test_get_stock_fail_response_error(self):
        """Test that triggers a response error.."""
        id = 1234
        self.mock_session.get.side_effect = aiohttp.ClientResponseError(None, None)

        with self.assertRaises(pyavanza.AvanzaResponseError):
            await pyavanza.get_stock_async(self.mock_session, id)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_STOCK_URL.format(id=id), raise_for_status=True
        )

    @common.sync
    async def test_get_stock_parse_error(self):
        """Test that triggers a parse error."""
        id = 1234
        mock_resp = Mock()
        mock_resp.json = make_mocked_coro()
        mock_resp.json.side_effect = json.JSONDecodeError(None, "", 0)
        self.mock_session.get = make_mocked_coro(return_value=mock_resp)

        with self.assertRaises(pyavanza.AvanzaParseError):
            await pyavanza.get_stock_async(self.mock_session, id)

    @common.sync
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
