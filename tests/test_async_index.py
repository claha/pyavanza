"""Test index async."""
import copy
import json
from unittest.mock import Mock

import aiohttp
from aiohttp.test_utils import make_mocked_coro

import pyavanza
import tests.common as common


class TestIndexAsync(common.TestCase):
    """Tests that retrieve index information asynchronously."""

    def setUp(self):
        """Set up, runs before each test."""
        self.mock_session = Mock()
        mock_get = make_mocked_coro()
        self.mock_session.get = mock_get

    @common.sync
    async def test_get_index_fail_request_error(self):
        """Test that triggers a request error."""
        id = 1234
        self.mock_session.get.side_effect = aiohttp.ClientConnectionError(None)

        with self.assertRaises(pyavanza.AvanzaRequestError):
            await pyavanza.get_index_async(self.mock_session, id)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_INDEX_URL.format(id=id), raise_for_status=True
        )

    @common.sync
    async def test_get_index_fail_response_error(self):
        """Test that triggers a response error.."""
        id = 1234
        self.mock_session.get.side_effect = aiohttp.ClientResponseError(None, None)

        with self.assertRaises(pyavanza.AvanzaResponseError):
            await pyavanza.get_index_async(self.mock_session, id)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_INDEX_URL.format(id=id), raise_for_status=True
        )

    @common.sync
    async def test_get_index_parse_error(self):
        """Test that triggers a parse error."""
        id = 1234
        mock_resp = Mock()
        mock_resp.json = make_mocked_coro()
        mock_resp.json.side_effect = json.JSONDecodeError(None, "", 0)
        self.mock_session.get = make_mocked_coro(return_value=mock_resp)

        with self.assertRaises(pyavanza.AvanzaParseError):
            await pyavanza.get_index_async(self.mock_session, id)

    @common.sync
    async def test_get_index_success(self):
        """Test a successful request and response."""
        id = 1234
        data = copy.deepcopy(common.JSON_INDEX_DATA)
        data["id"] = id
        mock_resp = Mock()
        mock_resp.json = make_mocked_coro(return_value=data)
        self.mock_session.get = make_mocked_coro(return_value=mock_resp)

        index = await pyavanza.get_index_async(self.mock_session, id)
        self.assertEqual(index.change, None)
        self.assertEqual(index.change_percent, None)
        self.assertEqual(index.currency, None)
        self.assertEqual(index.description, None)
        self.assertEqual(index.flag_code, None)
        self.assertEqual(index.highest_price, None)
        self.assertEqual(index.id, id)
        self.assertEqual(index.last_price, None)
        self.assertEqual(index.last_price_updated, None)
        self.assertEqual(index.lowest_price, None)
        self.assertEqual(index.name, None)
        self.assertEqual(index.price_at_start_of_year, None)
        self.assertEqual(index.price_five_years_ago, None)
        self.assertEqual(index.price_one_month_ago, None)
        self.assertEqual(index.price_one_week_ago, None)
        self.assertEqual(index.price_one_year_ago, None)
        self.assertEqual(index.price_six_months_ago, None)
        self.assertEqual(index.price_three_months_ago, None)
        self.assertEqual(index.price_three_years_ago, None)
        self.assertEqual(index.push_permitted, None)
        self.assertEqual(index.quote_updated, None)
        self.assertEqual(index.title, None)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_INDEX_URL.format(id=id), raise_for_status=True
        )
