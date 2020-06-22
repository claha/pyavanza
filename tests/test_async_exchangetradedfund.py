"""Test exchange traded fund async."""
import copy
import json
from unittest.mock import Mock

import aiohttp
from aiohttp.test_utils import make_mocked_coro

import pyavanza
import tests.common as common


class TestExchangeTradedFundAsync(common.TestCase):
    """Tests that retrieve exchange traded fund information asynchronously."""

    def setUp(self):
        """Set up, runs before each test."""
        self.mock_session = Mock()
        mock_get = make_mocked_coro()
        self.mock_session.get = mock_get

    @common.sync
    async def test_get_exchange_traded_fund_fail_request_error(self):
        """Test that triggers a request error."""
        id = 1234
        self.mock_session.get.side_effect = aiohttp.ClientConnectionError(None)

        with self.assertRaises(pyavanza.AvanzaRequestError):
            await pyavanza.get_exchange_traded_fund_async(self.mock_session, id)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_EXCHANGE_TRADED_FUND_URL.format(id=id),
            raise_for_status=True,
        )

    @common.sync
    async def test_get_exchange_traded_fund_fail_response_error(self):
        """Test that triggers a response error.."""
        id = 1234
        self.mock_session.get.side_effect = aiohttp.ClientResponseError(None, None)

        with self.assertRaises(pyavanza.AvanzaResponseError):
            await pyavanza.get_exchange_traded_fund_async(self.mock_session, id)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_EXCHANGE_TRADED_FUND_URL.format(id=id),
            raise_for_status=True,
        )

    @common.sync
    async def test_get_exchange_traded_fund_parse_error(self):
        """Test that triggers a parse error."""
        id = 1234
        mock_resp = Mock()
        mock_resp.json = make_mocked_coro()
        mock_resp.json.side_effect = json.JSONDecodeError(None, "", 0)
        self.mock_session.get = make_mocked_coro(return_value=mock_resp)

        with self.assertRaises(pyavanza.AvanzaParseError):
            await pyavanza.get_exchange_traded_fund_async(self.mock_session, id)

    @common.sync
    async def test_get_exchange_traded_fund_success(self):
        """Test a successful request and response."""
        id = 1234
        data = copy.deepcopy(common.JSON_EXCHANGE_TRADED_FUND_DATA)
        data["id"] = id
        mock_resp = Mock()
        mock_resp.json = make_mocked_coro(return_value=data)
        self.mock_session.get = make_mocked_coro(return_value=mock_resp)

        exchange_traded_fund = await pyavanza.get_exchange_traded_fund_async(
            self.mock_session, id
        )
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
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_EXCHANGE_TRADED_FUND_URL.format(id=id),
            raise_for_status=True,
        )
