"""Test stock."""
import json
import urllib.error
from unittest.mock import patch

import pyavanza
import tests.common as common


class TestStock(common.TestCase):
    """Tests that retrieve stock information."""

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_stock_fail_request_error(self, mock_urlopen):
        """Test that triggers a request error."""
        id = 1234
        mock_urlopen.side_effect = urllib.error.URLError(None)

        with self.assertRaises(pyavanza.AvanzaRequestError):
            pyavanza.get_stock(id)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_STOCK_URL.format(id=id)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_stock_fail_response_error(self, mock_urlopen):
        """Test that triggers a response error."""
        id = 1234
        mock_urlopen.side_effect = urllib.error.HTTPError(None, None, None, None, None)

        with self.assertRaises(pyavanza.AvanzaResponseError):
            pyavanza.get_stock(id)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_STOCK_URL.format(id=id)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_stock_fail_parse_error(self, mock_urlopen):
        """Test that triggers a parse error."""
        id = 1234
        mock_urlopen.return_value.read.return_value = b""

        with self.assertRaises(pyavanza.AvanzaParseError):
            pyavanza.get_stock(id)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_STOCK_URL.format(id=id)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_stock_success(self, mock_urlopen):
        """Test a successful request and response."""
        id = 1234
        mock_urlopen.return_value.read.return_value = json.dumps({"id": id}).encode()

        data = pyavanza.get_stock(id)
        self.assertEqual(len(data), 1)
        self.assertTrue("id" in data)
        self.assertEqual(data["id"], id)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_STOCK_URL.format(id=id)
        )
