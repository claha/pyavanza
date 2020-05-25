"""Test search."""
import json
import urllib.error
from unittest.mock import patch

import pyavanza
import tests.common as common


class TestSearch(common.TestCase):
    """Tests that search for instruments."""

    @patch("pyavanza.urllib.request.urlopen")
    def test_search_fail_request_error(self, mock_urlopen):
        """Test that triggers a request error."""
        query = "test"
        limit = 10
        mock_urlopen.side_effect = urllib.error.URLError(None)

        with self.assertRaises(pyavanza.AvanzaRequestError):
            pyavanza.search(query, limit=limit)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_SEARCH_URL.format(query=query, limit=limit)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_search_fail_response_error(self, mock_urlopen):
        """Test that triggers a response error."""
        query = "test"
        limit = 10
        mock_urlopen.side_effect = urllib.error.HTTPError(None, None, None, None, None)

        with self.assertRaises(pyavanza.AvanzaResponseError):
            pyavanza.search(query, limit=limit)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_SEARCH_URL.format(query=query, limit=limit)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_search_fail_parse_error(self, mock_urlopen):
        """Test that triggers a parse error."""
        query = "test"
        limit = 10
        mock_urlopen.return_value.read.return_value = b""

        with self.assertRaises(pyavanza.AvanzaParseError):
            pyavanza.search(query, limit=limit)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_SEARCH_URL.format(query=query, limit=limit)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_search_success_no_hits(self, mock_urlopen):
        """Test a successful request and response without hits."""
        query = "test"
        limit = 10
        instrument = pyavanza.InstrumentType.STOCK
        mock_urlopen.return_value.read.return_value = json.dumps(
            {"totalNumberOfHits": 0, "hits": []}
        ).encode()

        instruments = pyavanza.search(query, limit=limit, instrument=instrument)
        self.assertEqual(len(instruments), 0)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_SEARCH_INSTRUMENT_URL.format(
                instrument=instrument.value, query=query, limit=limit
            )
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_search_success_low_limit(self, mock_urlopen):
        """Test a successful request and response, limit is lower than number of hits."""
        query = "test"
        limit = 1
        mock_urlopen.return_value.read.return_value = json.dumps(
            {
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
        ).encode()

        instruments = pyavanza.search(query, limit=limit)
        self.assertEqual(len(instruments), 1)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_SEARCH_URL.format(query=query, limit=limit)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_search_success(self, mock_urlopen):
        """Test a successful request and response."""
        query = "test"
        limit = 10
        instrument = pyavanza.InstrumentType.STOCK
        mock_urlopen.return_value.read.return_value = json.dumps(
            {
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
        ).encode()

        instruments = pyavanza.search(query, limit=limit, instrument=instrument)
        self.assertEqual(len(instruments), 1)
        self.assertEqual(instruments[0].type, instrument)
        self.assertTrue(instruments[0].tradable)
        self.assertEqual(instruments[0].id, "1234")
        self.assertEqual(instruments[0].ticker_symbol, "TEST")
        self.assertEqual(instruments[0].name, "Test")
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_SEARCH_INSTRUMENT_URL.format(
                instrument=instrument.value, query=query, limit=limit
            )
        )
