"""Test."""
import json
import unittest
import urllib.error
from unittest.mock import patch

import pyavanza


class TestStock(unittest.TestCase):
    """Tests that retrieve stock information."""

    def shortDescription(self):
        """Disable printing of docstring in test runner."""
        return None

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_stock_fail_url_error(self, mock_urlopen):
        """Test that url error can be handled."""
        id = 1234
        mock_urlopen.side_effect = urllib.error.URLError("url error")

        data = pyavanza.get_stock(id)
        self.assertEqual(len(data), 0)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_STOCK_URL.format(id=id)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_stock_fail_http_error(self, mock_urlopen):
        """Test that http error can be handled."""
        id = 1234
        mock_urlopen.side_effect = urllib.error.HTTPError(
            "url", 404, "http error", None, None
        )

        data = pyavanza.get_stock(id)
        self.assertEqual(len(data), 0)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_STOCK_URL.format(id=id)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_stock_success(self, mock_urlopen):
        """Test a successful request."""
        id = 1234
        mock_urlopen.return_value.read.return_value = json.dumps({"id": id}).encode()

        data = pyavanza.get_stock(id)
        self.assertEqual(len(data), 1)
        self.assertTrue("id" in data)
        self.assertEqual(data["id"], id)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_STOCK_URL.format(id=id)
        )
