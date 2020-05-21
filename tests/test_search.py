"""Test search."""
import json
import unittest
import urllib.error
from unittest.mock import patch

import pyavanza


class TestSearch(unittest.TestCase):
    """Tests that search for instruments."""

    def shortDescription(self):
        """Disable printing of docstring in test runner."""
        return None

    @patch("pyavanza.urllib.request.urlopen")
    def test_search_fail_url_error(self, mock_urlopen):
        """Test that url error can be handled."""
        query = "test"
        limit = 10
        mock_urlopen.side_effect = urllib.error.URLError("url error")

        data = pyavanza.search(query, limit=limit)
        self.assertEqual(len(data), 0)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_SEARCH_URL.format(query=query, limit=limit)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_search_fail_http_error(self, mock_urlopen):
        """Test that http error can be handled."""
        query = "test"
        limit = 10
        mock_urlopen.side_effect = urllib.error.HTTPError(
            "url", 404, "http error", None, None
        )

        data = pyavanza.search(query, limit=limit)
        self.assertEqual(len(data), 0)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_SEARCH_URL.format(query=query, limit=limit)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_search_success(self, mock_urlopen):
        """Test a successful request."""
        query = "test"
        limit = 10
        instrument = pyavanza.Instrument.STOCK
        mock_urlopen.return_value.read.return_value = json.dumps(
            {
                "totalNumberOfHits": 1,
                "hits": [
                    {"instrumentType": "STOCK", "numberOfHits": 1, "topHits": [{}]}
                ],
            }
        ).encode()

        data = pyavanza.search(query, limit=limit, instrument=instrument)
        self.assertEqual(len(data), 2)
        self.assertEqual(data["totalNumberOfHits"], 1)
        self.assertTrue(len(data["hits"]), 1)
        self.assertTrue(data["hits"][0]["instrumentType"], instrument.value)
        self.assertTrue(data["hits"][0]["numberOfHits"], 1)
        self.assertTrue(len(data["hits"][0]["topHits"]), 1)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_SEARCH_INSTRUMENT_URL.format(
                instrument=instrument.value, query=query, limit=limit
            )
        )
