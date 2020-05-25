"""Test stock async."""
import copy
import json
from unittest.mock import Mock

import aiohttp
from aiohttp.test_utils import make_mocked_coro

import pyavanza
import tests.common as common


class TestStockAsync(common.TestCase):
    """Tests that retrieve stock information asynchronously."""

    def setUp(self):
        """Set up, runs before each test."""
        self.mock_session = Mock()
        mock_get = make_mocked_coro()
        self.mock_session.get = mock_get

    @common.sync
    async def test_get_stock_fail_request_error(self):
        """Test that triggers a request error."""
        id = 1234
        self.mock_session.get.side_effect = aiohttp.ClientConnectionError(None)

        with self.assertRaises(pyavanza.AvanzaRequestError):
            await pyavanza.get_stock_async(self.mock_session, id)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_STOCK_URL.format(id=id), raise_for_status=True
        )

    @common.sync
    async def test_get_stock_fail_response_error(self):
        """Test that triggers a response error.."""
        id = 1234
        self.mock_session.get.side_effect = aiohttp.ClientResponseError(None, None)

        with self.assertRaises(pyavanza.AvanzaResponseError):
            await pyavanza.get_stock_async(self.mock_session, id)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_STOCK_URL.format(id=id), raise_for_status=True
        )

    @common.sync
    async def test_get_stock_parse_error(self):
        """Test that triggers a parse error."""
        id = 1234
        mock_resp = Mock()
        mock_resp.json = make_mocked_coro()
        mock_resp.json.side_effect = json.JSONDecodeError(None, "", 0)
        self.mock_session.get = make_mocked_coro(return_value=mock_resp)

        with self.assertRaises(pyavanza.AvanzaParseError):
            await pyavanza.get_stock_async(self.mock_session, id)

    @common.sync
    async def test_get_stock_success(self):
        """Test a successful request and response."""
        id = 1234
        data = copy.deepcopy(common.JSON_STOCK_DATA)
        data["id"] = id
        mock_resp = Mock()
        mock_resp.json = make_mocked_coro(return_value=data)
        self.mock_session.get = make_mocked_coro(return_value=mock_resp)

        stock = await pyavanza.get_stock_async(self.mock_session, id)
        self.assertEqual(stock.annual_meetings, None)
        self.assertEqual(stock.broker_trade_summary, None)
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
        self.assertEqual(stock.short_sellable, None)
        self.assertEqual(stock.super_loan, None)
        self.assertEqual(stock.ticker_symbol, None)
        self.assertEqual(stock.total_value_traded, None)
        self.assertEqual(stock.total_volume_traded, None)
        self.assertEqual(stock.tradable, None)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_STOCK_URL.format(id=id), raise_for_status=True
        )
