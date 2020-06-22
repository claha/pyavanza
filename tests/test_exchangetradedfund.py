"""Test exchange traded fund."""
import copy
import json
import urllib.error
from unittest.mock import patch

import pyavanza
import tests.common as common


class TestExchangeTradedFund(common.TestCase):
    """Tests that retrieve exchange traded fund information."""

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_exchange_traded_fund_fail_request_error(self, mock_urlopen):
        """Test that triggers a request error."""
        id = 1234
        mock_urlopen.side_effect = urllib.error.URLError(None)

        with self.assertRaises(pyavanza.AvanzaRequestError):
            pyavanza.get_exchange_traded_fund(id)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_EXCHANGE_TRADED_FUND_URL.format(id=id)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_exchange_traded_fund_fail_response_error(self, mock_urlopen):
        """Test that triggers a response error."""
        id = 1234
        mock_urlopen.side_effect = urllib.error.HTTPError(None, None, None, None, None)

        with self.assertRaises(pyavanza.AvanzaResponseError):
            pyavanza.get_exchange_traded_fund(id)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_EXCHANGE_TRADED_FUND_URL.format(id=id)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_exchange_traded_fund_fail_parse_error(self, mock_urlopen):
        """Test that triggers a parse error."""
        id = 1234
        mock_urlopen.return_value.read.return_value = b""

        with self.assertRaises(pyavanza.AvanzaParseError):
            pyavanza.get_exchange_traded_fund(id)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_EXCHANGE_TRADED_FUND_URL.format(id=id)
        )

    @patch("pyavanza.urllib.request.urlopen")
    def test_get_exchange_traded_fund_success(self, mock_urlopen):
        """Test a successful request and response."""
        id = 1234
        data = copy.deepcopy(common.JSON_EXCHANGE_TRADED_FUND_DATA)
        data["id"] = id
        mock_urlopen.return_value.read.return_value = json.dumps(data).encode()

        exchange_traded_fund = pyavanza.get_exchange_traded_fund(id)
        self.assertEqual(exchange_traded_fund.asset_root_category, None)
        self.assertEqual(exchange_traded_fund.asset_sub_category, None)
        self.assertEqual(exchange_traded_fund.asset_sub_sub_category, None)
        self.assertEqual(exchange_traded_fund.buy_price, None)
        self.assertEqual(exchange_traded_fund.change, None)
        self.assertEqual(exchange_traded_fund.change_percent, None)
        self.assertEqual(exchange_traded_fund.currency, None)
        self.assertEqual(exchange_traded_fund.direction, None)
        self.assertEqual(exchange_traded_fund.flag_code, None)
        self.assertEqual(exchange_traded_fund.has_investment_fees, None)
        self.assertEqual(exchange_traded_fund.highest_price, None)
        self.assertEqual(exchange_traded_fund.id, id)
        self.assertEqual(exchange_traded_fund.isin, None)
        self.assertEqual(exchange_traded_fund.issuer_name, None)
        self.assertEqual(exchange_traded_fund.last_price, None)
        self.assertEqual(exchange_traded_fund.last_price_updated, None)
        self.assertEqual(exchange_traded_fund.leverage, None)
        self.assertEqual(exchange_traded_fund.loan_factor, None)
        self.assertEqual(exchange_traded_fund.lowest_price, None)
        self.assertEqual(exchange_traded_fund.management_fee, None)
        self.assertEqual(exchange_traded_fund.market_place, None)
        self.assertEqual(exchange_traded_fund.name, None)
        self.assertEqual(exchange_traded_fund.price_at_start_of_year, None)
        self.assertEqual(exchange_traded_fund.price_five_years_ago, None)
        self.assertEqual(exchange_traded_fund.price_one_month_ago, None)
        self.assertEqual(exchange_traded_fund.price_one_week_ago, None)
        self.assertEqual(exchange_traded_fund.price_one_year_ago, None)
        self.assertEqual(exchange_traded_fund.price_six_months_ago, None)
        self.assertEqual(exchange_traded_fund.price_three_months_ago, None)
        self.assertEqual(exchange_traded_fund.price_three_years_ago, None)
        self.assertEqual(exchange_traded_fund.priip_document_url, None)
        self.assertEqual(exchange_traded_fund.prospectus, None)
        self.assertEqual(exchange_traded_fund.push_permitted, None)
        self.assertEqual(exchange_traded_fund.quote_updated, None)
        self.assertEqual(exchange_traded_fund.sell_price, None)
        self.assertEqual(exchange_traded_fund.spread, None)
        self.assertEqual(exchange_traded_fund.start_date, None)
        self.assertEqual(exchange_traded_fund.ticker_symbol, None)
        self.assertEqual(exchange_traded_fund.total_value_traded, None)
        self.assertEqual(exchange_traded_fund.total_volume_traded, None)
        self.assertEqual(exchange_traded_fund.tradable, None)
        self.assertEqual(exchange_traded_fund.underlying_orderbook, None)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_EXCHANGE_TRADED_FUND_URL.format(id=id)
        )

    def test_exchange_traded_fund_no_data(self):
        """Test create Exchange_traded_fund without data."""
        with self.assertRaises(pyavanza.AvanzaParseError):
            pyavanza.ExchangeTradedFund({})

    def test_exchange_traded_fund_missinng_data(self):
        """Test create exchange_traded_fund with missing data."""
        for key in common.JSON_EXCHANGE_TRADED_FUND_DATA:
            with self.subTest(key=key):
                data = copy.deepcopy(common.JSON_EXCHANGE_TRADED_FUND_DATA)
                del data[key]
                if (
                    key
                    not in common.JSON_EXCHANGE_TRADED_FUND_DATA_ALLOWED_MISSING_KEYS
                ):
                    with self.assertRaises(pyavanza.AvanzaParseError) as context:
                        pyavanza.ExchangeTradedFund(data)
                    self.assertEqual(context.exception.args[0], key)
                else:
                    try:
                        pyavanza.ExchangeTradedFund(data)
                    except pyavanza.AvanzaParseError:
                        self.fail("Unexpected AvanzaParseError, key: {}".format(key))

    def test_exchange_traded_fund_string(self):
        """Test string representation of a exchange_traded_fund."""
        data = copy.deepcopy(common.JSON_EXCHANGE_TRADED_FUND_DATA)
        data["id"] = 1234
        data["name"] = "Test"
        exchange_traded_fund = pyavanza.ExchangeTradedFund(data)
        self.assertEqual(str(exchange_traded_fund), "Exchange Traded Fund[1234]: Test")
