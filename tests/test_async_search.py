"""Test stock search."""
import json
from unittest.mock import Mock

import aiohttp
from aiohttp.test_utils import make_mocked_coro

import pyavanza
import tests.common as common


class TestSearchAsync(common.TestCase):
    """Tests that search for instruments asynchronously."""

    def setUp(self):
        """Set up, runs before each test."""
        self.mock_session = Mock()
        mock_get = make_mocked_coro()
        self.mock_session.get = mock_get

    @common.sync
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

    @common.sync
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

    @common.sync
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

    @common.sync
    async def test_search_success_no_hits(self):
        """Test a successful request and response without hits."""
        query = "test"
        limit = 10
        instrument = pyavanza.InstrumentType.STOCK
        mock_resp = Mock()
        mock_resp.json = make_mocked_coro(
            return_value={"totalNumberOfHits": 1, "hits": []}
        )
        self.mock_session.get = make_mocked_coro(return_value=mock_resp)

        instruments = await pyavanza.search_async(
            self.mock_session, query, limit=limit, instrument=instrument
        )
        self.assertEqual(len(instruments), 0)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_SEARCH_INSTRUMENT_URL.format(
                instrument=instrument.value, query=query, limit=limit
            ),
            raise_for_status=True,
        )

    @common.sync
    async def test_search_success_low_limit(self):
        """Test a successful request and response, limit is lower than number of hits."""
        query = "test"
        limit = 10
        mock_resp = Mock()
        mock_resp.json = make_mocked_coro(
            return_value={
                "totalNumberOfHits": 2,
                "hits": [
                    {
                        "instrumentType": "STOCK",
                        "numberOfHits": 1,
                        "topHits": [
                            {
                                "tradable": True,
                                "id": "1234",
                                "tickerSymbol": "TEST",
                                "name": "Test",
                            }
                        ],
                    },
                    {"instrumentType": "FUND", "numberOfHits": 1},
                ],
            }
        )
        self.mock_session.get = make_mocked_coro(return_value=mock_resp)

        instruments = await pyavanza.search_async(self.mock_session, query, limit=limit)
        self.assertEqual(len(instruments), 1)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_SEARCH_URL.format(query=query, limit=limit),
            raise_for_status=True,
        )

    @common.sync
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
                    {
                        "instrumentType": instrument.value,
                        "numberOfHits": 1,
                        "topHits": [
                            {
                                "tradable": True,
                                "id": "1234",
                                "tickerSymbol": "TEST",
                                "name": "Test",
                            }
                        ],
                    }
                ],
            }
        )
        self.mock_session.get = make_mocked_coro(return_value=mock_resp)

        instruments = await pyavanza.search_async(
            self.mock_session, query, limit=limit, instrument=instrument
        )
        self.assertEqual(len(instruments), 1)
        self.assertEqual(instruments[0].type, instrument)
        self.assertTrue(instruments[0].tradable)
        self.assertEqual(instruments[0].id, "1234")
        self.assertEqual(instruments[0].ticker_symbol, "TEST")
        self.assertEqual(instruments[0].name, "Test")
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_SEARCH_INSTRUMENT_URL.format(
                instrument=instrument.value, query=query, limit=limit
            ),
            raise_for_status=True,
        )
