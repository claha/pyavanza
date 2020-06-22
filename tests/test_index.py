"""Test index."""
import copy
import json
import urllib.error
from unittest.mock import patch

import pyavanza
import tests.common as common


class TestIndex(common.TestCase):
    """Tests that retrieve index information."""

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_index_fail_request_error(self, mock_urlopen):
        """Test that triggers a request error."""
        id = 1234
        mock_urlopen.side_effect = urllib.error.URLError(None)

        with self.assertRaises(pyavanza.AvanzaRequestError):
            pyavanza.get_index(id)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_INDEX_URL.format(id=id)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_index_fail_response_error(self, mock_urlopen):
        """Test that triggers a response error."""
        id = 1234
        mock_urlopen.side_effect = urllib.error.HTTPError(None, None, None, None, None)

        with self.assertRaises(pyavanza.AvanzaResponseError):
            pyavanza.get_index(id)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_INDEX_URL.format(id=id)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_index_fail_parse_error(self, mock_urlopen):
        """Test that triggers a parse error."""
        id = 1234
        mock_urlopen.return_value.read.return_value = b""

        with self.assertRaises(pyavanza.AvanzaParseError):
            pyavanza.get_index(id)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_INDEX_URL.format(id=id)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_index_success(self, mock_urlopen):
        """Test a successful request and response."""
        id = 1234
        data = copy.deepcopy(common.JSON_INDEX_DATA)
        data["id"] = id
        mock_urlopen.return_value.read.return_value = json.dumps(data).encode()

        index = pyavanza.get_index(id)
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
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_INDEX_URL.format(id=id)
        )

    def test_index_no_data(self):
        """Test create Index without data."""
        with self.assertRaises(pyavanza.AvanzaParseError):
            pyavanza.Index({})

    def test_index_missinng_data(self):
        """Test create index with missing data."""
        for key in common.JSON_INDEX_DATA:
            with self.subTest(key=key):
                data = copy.deepcopy(common.JSON_INDEX_DATA)
                del data[key]
                if key not in common.JSON_INDEX_DATA_ALLOWED_MISSING_KEYS:
                    with self.assertRaises(pyavanza.AvanzaParseError) as context:
                        pyavanza.Index(data)
                    self.assertEqual(context.exception.args[0], key)
                else:
                    try:
                        pyavanza.Index(data)
                    except pyavanza.AvanzaParseError:
                        self.fail("Unexpected AvanzaParseError, key: {}".format(key))

    def test_index_string(self):
        """Test string representation of a index."""
        data = copy.deepcopy(common.JSON_INDEX_DATA)
        data["id"] = 1234
        data["name"] = "Test"
        index = pyavanza.Index(data)
        self.assertEqual(str(index), "Index[1234]: Test")
