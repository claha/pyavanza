"""Test certificate."""
import copy
import json
import urllib.error
from unittest.mock import patch

import pyavanza
import tests.common as common


class TestCertificate(common.TestCase):
    """Tests that retrieve certificate information."""

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_certificate_fail_request_error(self, mock_urlopen):
        """Test that triggers a request error."""
        id = 1234
        mock_urlopen.side_effect = urllib.error.URLError(None)

        with self.assertRaises(pyavanza.AvanzaRequestError):
            pyavanza.get_certificate(id)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_CERTIFICATE_URL.format(id=id)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_certificate_fail_response_error(self, mock_urlopen):
        """Test that triggers a response error."""
        id = 1234
        mock_urlopen.side_effect = urllib.error.HTTPError(None, None, None, None, None)

        with self.assertRaises(pyavanza.AvanzaResponseError):
            pyavanza.get_certificate(id)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_CERTIFICATE_URL.format(id=id)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_certificate_fail_parse_error(self, mock_urlopen):
        """Test that triggers a parse error."""
        id = 1234
        mock_urlopen.return_value.read.return_value = b""

        with self.assertRaises(pyavanza.AvanzaParseError):
            pyavanza.get_certificate(id)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_CERTIFICATE_URL.format(id=id)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_certificate_success(self, mock_urlopen):
        """Test a successful request and response."""
        id = 1234
        data = copy.deepcopy(common.JSON_CERTIFICATE_DATA)
        data["id"] = id
        mock_urlopen.return_value.read.return_value = json.dumps(data).encode()

        certificate = pyavanza.get_certificate(id)
        self.assertEqual(certificate.administration_fee, None)
        self.assertEqual(certificate.asset_root_category, None)
        self.assertEqual(certificate.asset_sub_category, None)
        self.assertEqual(certificate.asset_sub_sub_category, None)
        self.assertEqual(certificate.change, None)
        self.assertEqual(certificate.change_percent, None)
        self.assertEqual(certificate.currency, None)
        self.assertEqual(certificate.direction, None)
        self.assertEqual(certificate.end_date, None)
        self.assertEqual(certificate.flag_code, None)
        self.assertEqual(certificate.has_investment_fees, None)
        self.assertEqual(certificate.highest_price, None)
        self.assertEqual(certificate.id, id)
        self.assertEqual(certificate.isin, None)
        self.assertEqual(certificate.issuer_name, None)
        self.assertEqual(certificate.last_price, None)
        self.assertEqual(certificate.last_price_updated, None)
        self.assertEqual(certificate.leverage, None)
        self.assertEqual(certificate.lowest_price, None)
        self.assertEqual(certificate.market_place, None)
        self.assertEqual(certificate.name, None)
        self.assertEqual(certificate.price_at_start_of_year, None)
        self.assertEqual(certificate.price_five_years_ago, None)
        self.assertEqual(certificate.price_one_month_ago, None)
        self.assertEqual(certificate.price_one_week_ago, None)
        self.assertEqual(certificate.price_one_year_ago, None)
        self.assertEqual(certificate.price_six_months_ago, None)
        self.assertEqual(certificate.price_three_months_ago, None)
        self.assertEqual(certificate.price_three_years_ago, None)
        self.assertEqual(certificate.priip_document_url, None)
        self.assertEqual(certificate.prospectus, None)
        self.assertEqual(certificate.push_permitted, None)
        self.assertEqual(certificate.quote_updated, None)
        self.assertEqual(certificate.short_name, None)
        self.assertEqual(certificate.ticker_symbol, None)
        self.assertEqual(certificate.total_value_traded, None)
        self.assertEqual(certificate.total_volume_traded, None)
        self.assertEqual(certificate.tradable, None)
        self.assertEqual(certificate.underlying_currency, None)
        self.assertEqual(certificate.underlying_orderbook, None)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_CERTIFICATE_URL.format(id=id)
        )

    def test_certificate_no_data(self):
        """Test create Certificate without data."""
        with self.assertRaises(pyavanza.AvanzaParseError):
            pyavanza.Certificate({})

    def test_certificate_missinng_data(self):
        """Test create certificate with missing data."""
        for key in common.JSON_CERTIFICATE_DATA:
            with self.subTest(key=key):
                data = copy.deepcopy(common.JSON_CERTIFICATE_DATA)
                del data[key]
                if key not in common.JSON_CERTIFICATE_DATA_ALLOWED_MISSING_KEYS:
                    with self.assertRaises(pyavanza.AvanzaParseError) as context:
                        pyavanza.Certificate(data)
                    self.assertEqual(context.exception.args[0], key)
                else:
                    try:
                        pyavanza.Certificate(data)
                    except pyavanza.AvanzaParseError:
                        self.fail("Unexpected AvanzaParseError, key: {}".format(key))

    def test_certificate_string(self):
        """Test string representation of a certificate."""
        data = copy.deepcopy(common.JSON_CERTIFICATE_DATA)
        data["id"] = 1234
        data["name"] = "Test"
        certificate = pyavanza.Certificate(data)
        self.assertEqual(str(certificate), "Certificate[1234]: Test")
