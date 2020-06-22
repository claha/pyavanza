"""Test fund."""
import copy
import json
import urllib.error
from unittest.mock import patch

import pyavanza
import tests.common as common


class TestFund(common.TestCase):
    """Tests that retrieve fund information."""

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_fund_fail_request_error(self, mock_urlopen):
        """Test that triggers a request error."""
        id = 1234
        mock_urlopen.side_effect = urllib.error.URLError(None)

        with self.assertRaises(pyavanza.AvanzaRequestError):
            pyavanza.get_fund(id)
        mock_urlopen.assert_called_once_with(pyavanza.AVANZA_API_FUND_URL.format(id=id))

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_fund_fail_response_error(self, mock_urlopen):
        """Test that triggers a response error."""
        id = 1234
        mock_urlopen.side_effect = urllib.error.HTTPError(None, None, None, None, None)

        with self.assertRaises(pyavanza.AvanzaResponseError):
            pyavanza.get_fund(id)
        mock_urlopen.assert_called_once_with(pyavanza.AVANZA_API_FUND_URL.format(id=id))

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_fund_fail_parse_error(self, mock_urlopen):
        """Test that triggers a parse error."""
        id = 1234
        mock_urlopen.return_value.read.return_value = b""

        with self.assertRaises(pyavanza.AvanzaParseError):
            pyavanza.get_fund(id)
        mock_urlopen.assert_called_once_with(pyavanza.AVANZA_API_FUND_URL.format(id=id))

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_fund_success(self, mock_urlopen):
        """Test a successful request and response."""
        id = 1234
        data = copy.deepcopy(common.JSON_FUND_DATA)
        data["id"] = id
        mock_urlopen.return_value.read.return_value = json.dumps(data).encode()

        fund = pyavanza.get_fund(id)
        self.assertEqual(fund.nav, None)
        self.assertEqual(fund.nav_last_updated, None)
        self.assertEqual(fund.administrators, None)
        self.assertEqual(fund.auto_portfolio, None)
        self.assertEqual(fund.buy_fee, None)
        self.assertEqual(fund.buyable, None)
        self.assertEqual(fund.capital, None)
        self.assertEqual(fund.change_since_five_years, None)
        self.assertEqual(fund.change_since_one_day, None)
        self.assertEqual(fund.change_since_one_month, None)
        self.assertEqual(fund.change_since_one_week, None)
        self.assertEqual(fund.change_since_one_year, None)
        self.assertEqual(fund.change_since_six_months, None)
        self.assertEqual(fund.change_since_ten_years, None)
        self.assertEqual(fund.change_since_three_months, None)
        self.assertEqual(fund.change_since_three_years, None)
        self.assertEqual(fund.change_since_turn_of_the_year, None)
        self.assertEqual(fund.description, None)
        self.assertEqual(fund.domicile, None)
        self.assertEqual(fund.fund_company, None)
        self.assertEqual(fund.has_investment_fees, None)
        self.assertEqual(fund.id, id)
        self.assertEqual(fund.isin, None)
        self.assertEqual(fund.loan_factor, None)
        self.assertEqual(fund.management_fee, None)
        self.assertEqual(fund.name, None)
        self.assertEqual(fund.norman_amount, None)
        self.assertEqual(fund.number_of_owners, None)
        self.assertEqual(fund.other_fees, None)
        self.assertEqual(fund.prospectus, None)
        self.assertEqual(fund.rating, None)
        self.assertEqual(fund.related_funds, None)
        self.assertEqual(fund.risk, None)
        self.assertEqual(fund.risk_level, None)
        self.assertEqual(fund.sell_fee, None)
        self.assertEqual(fund.sellable, None)
        self.assertEqual(fund.sharpe_ratio, None)
        self.assertEqual(fund.standard_deviation, None)
        self.assertEqual(fund.start_date, None)
        self.assertEqual(fund.sub_category, None)
        self.assertEqual(fund.trading_currency, None)
        self.assertEqual(fund.type, None)
        mock_urlopen.assert_called_once_with(pyavanza.AVANZA_API_FUND_URL.format(id=id))

    def test_fund_no_data(self):
        """Test create Fund without data."""
        with self.assertRaises(pyavanza.AvanzaParseError):
            pyavanza.Fund({})

    def test_fund_missinng_data(self):
        """Test create fund with missing data."""
        for key in common.JSON_FUND_DATA:
            with self.subTest(key=key):
                data = copy.deepcopy(common.JSON_FUND_DATA)
                del data[key]
                if key not in common.JSON_FUND_DATA_ALLOWED_MISSING_KEYS:
                    with self.assertRaises(pyavanza.AvanzaParseError) as context:
                        pyavanza.Fund(data)
                    self.assertEqual(context.exception.args[0], key)
                else:
                    try:
                        pyavanza.Fund(data)
                    except pyavanza.AvanzaParseError:
                        self.fail("Unexpected AvanzaParseError, key: {}".format(key))

    def test_fund_string(self):
        """Test string representation of a fund."""
        data = copy.deepcopy(common.JSON_FUND_DATA)
        data["id"] = 1234
        data["name"] = "Test"
        fund = pyavanza.Fund(data)
        self.assertEqual(str(fund), "Fund[1234]: Test")
