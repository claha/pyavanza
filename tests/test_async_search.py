"""Test stock search."""
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


class TestSearchAsync(unittest.TestCase):
    """Tests that search for instruments asynchronously."""

    def shortDescription(self):
        """Disable printing of docstring in test runner."""
        return None

    def setUp(self):
        """Set up, runs before each test."""
        self.mock_session = Mock()
        mock_get = make_mocked_coro()
        self.mock_session.get = mock_get

    @sync
    async def test_search_fail_request_error(self):
        """Test that triggers a request error."""
        query = "test"
        limit = 10
        self.mock_session.get.side_effect = aiohttp.ClientConnectionError(None)

        with self.assertRaises(pyavanza.AvanzaRequestError):
            await pyavanza.search_async(self.mock_session, query, limit=limit)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_SEARCH_URL.format(query=query, limit=limit),
            raise_for_status=True,
        )

    @sync
    async def test_search_fail_response_error(self):
        """Test that triggers a response error."""
        query = "test"
        limit = 10
        self.mock_session.get.side_effect = aiohttp.ClientResponseError(None, None)

        with self.assertRaises(pyavanza.AvanzaResponseError):
            await pyavanza.search_async(self.mock_session, query, limit=limit)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_SEARCH_URL.format(query=query, limit=limit),
            raise_for_status=True,
        )

    @sync
    async def test_search_fail_parse_error(self):
        """Test that triggers a parse error."""
        query = "test"
        limit = 10
        instrument = pyavanza.InstrumentType.STOCK
        mock_resp = Mock()
        mock_resp.json = make_mocked_coro()
        mock_resp.json.side_effect = json.JSONDecodeError(None, "", 0)
        self.mock_session.get = make_mocked_coro(return_value=mock_resp)

        with self.assertRaises(pyavanza.AvanzaParseError):
            await pyavanza.search_async(
                self.mock_session, query, limit=limit, instrument=instrument
            )

    @sync
    async def test_search_success(self):
        """Test a successful request and response."""
        query = "test"
        limit = 10
        instrument = pyavanza.InstrumentType.STOCK
        mock_resp = Mock()
        mock_resp.json = make_mocked_coro(
            return_value={
                "totalNumberOfHits": 1,
                "hits": [
                    {"instrumentType": "STOCK", "numberOfHits": 1, "topHits": [{}]}
                ],
            }
        )
        self.mock_session.get = make_mocked_coro(return_value=mock_resp)

        data = await pyavanza.search_async(
            self.mock_session, query, limit=limit, instrument=instrument
        )
        self.assertEqual(len(data), 2)
        self.assertEqual(data["totalNumberOfHits"], 1)
        self.assertTrue(len(data["hits"]), 1)
        self.assertTrue(data["hits"][0]["instrumentType"], instrument.value)
        self.assertTrue(data["hits"][0]["numberOfHits"], 1)
        self.assertTrue(len(data["hits"][0]["topHits"]), 1)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_SEARCH_INSTRUMENT_URL.format(
                instrument=instrument.value, query=query, limit=limit
            ),
            raise_for_status=True,
        )
