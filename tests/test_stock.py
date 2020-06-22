"""Test stock."""
import copy
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
        data = copy.deepcopy(common.JSON_STOCK_DATA)
        data["id"] = id
        mock_urlopen.return_value.read.return_value = json.dumps(data).encode()

        stock = pyavanza.get_stock(id)
        self.assertEqual(stock.annual_meetings, None)
        self.assertEqual(stock.broker_trade_summary, None)
        self.assertEqual(stock.buy_price, None)
        self.assertEqual(stock.change, None)
        self.assertEqual(stock.change_percent, None)
        self.assertEqual(stock.company, None)
        self.assertEqual(stock.company_owners, None)
        self.assertEqual(stock.company_reports, None)
        self.assertEqual(stock.country, None)
        self.assertEqual(stock.currency, None)
        self.assertEqual(stock.dividends, None)
        self.assertEqual(stock.flag_code, None)
        self.assertEqual(stock.has_investment_fees, None)
        self.assertEqual(stock.highest_price, None)
        self.assertEqual(stock.id, id)
        self.assertEqual(stock.isin, None)
        self.assertEqual(stock.key_ratios, None)
        self.assertEqual(stock.last_price, None)
        self.assertEqual(stock.last_price_updated, None)
        self.assertEqual(stock.latest_trades, None)
        self.assertEqual(stock.loan_factor, None)
        self.assertEqual(stock.lowest_price, None)
        self.assertEqual(stock.market_list, None)
        self.assertEqual(stock.market_maker_expected, None)
        self.assertEqual(stock.market_place, None)
        self.assertEqual(stock.market_trades, None)
        self.assertEqual(stock.morning_star_fact_sheet_url, None)
        self.assertEqual(stock.name, None)
        self.assertEqual(stock.number_of_owners, None)
        self.assertEqual(stock.order_depth_levels, None)
        self.assertEqual(stock.order_depth_received_time, None)
        self.assertEqual(stock.price_at_start_of_year, None)
        self.assertEqual(stock.price_five_years_ago, None)
        self.assertEqual(stock.price_one_month_ago, None)
        self.assertEqual(stock.price_one_week_ago, None)
        self.assertEqual(stock.price_one_year_ago, None)
        self.assertEqual(stock.price_six_months_ago, None)
        self.assertEqual(stock.price_three_months_ago, None)
        self.assertEqual(stock.price_three_years_ago, None)
        self.assertEqual(stock.push_permitted, None)
        self.assertEqual(stock.quote_updated, None)
        self.assertEqual(stock.related_stocks, None)
        self.assertEqual(stock.sell_price, None)
        self.assertEqual(stock.short_sellable, None)
        self.assertEqual(stock.super_loan, None)
        self.assertEqual(stock.ticker_symbol, None)
        self.assertEqual(stock.total_value_traded, None)
        self.assertEqual(stock.total_volume_traded, None)
        self.assertEqual(stock.tradable, None)
        mock_urlopen.assert_called_once_with(
            pyavanza.AVANZA_API_STOCK_URL.format(id=id)
        )

    def test_stock_no_data(self):
        """Test create Stock without data."""
        with self.assertRaises(pyavanza.AvanzaParseError):
            pyavanza.Stock({})

    def test_stock_missinng_data(self):
        """Test create stock with missing data."""
        for key in common.JSON_STOCK_DATA:
            with self.subTest(key=key):
                data = copy.deepcopy(common.JSON_STOCK_DATA)
                del data[key]
                if key not in common.JSON_STOCK_DATA_ALLOWED_MISSING_KEYS:
                    with self.assertRaises(pyavanza.AvanzaParseError) as context:
                        pyavanza.Stock(data)
                    self.assertEqual(context.exception.args[0], key)
                else:
                    try:
                        pyavanza.Stock(data)
                    except pyavanza.AvanzaParseError:
                        self.fail("Unexpected AvanzaParseError, key: {}".format(key))

    def test_stock_string(self):
        """Test string representation of a stock."""
        data = copy.deepcopy(common.JSON_STOCK_DATA)
        data["id"] = 1234
        data["name"] = "Test"
        stock = pyavanza.Stock(data)
        self.assertEqual(str(stock), "Stock[1234]: Test")
