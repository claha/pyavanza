"""Test fund async."""
import copy
import json
from unittest.mock import Mock

import aiohttp
from aiohttp.test_utils import make_mocked_coro

import pyavanza
import tests.common as common


class TestFundAsync(common.TestCase):
    """Tests that retrieve fund information asynchronously."""

    def setUp(self):
        """Set up, runs before each test."""
        self.mock_session = Mock()
        mock_get = make_mocked_coro()
        self.mock_session.get = mock_get

    @common.sync
    async def test_get_fund_fail_request_error(self):
        """Test that triggers a request error."""
        id = 1234
        self.mock_session.get.side_effect = aiohttp.ClientConnectionError(None)

        with self.assertRaises(pyavanza.AvanzaRequestError):
            await pyavanza.get_fund_async(self.mock_session, id)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_FUND_URL.format(id=id), raise_for_status=True
        )

    @common.sync
    async def test_get_fund_fail_response_error(self):
        """Test that triggers a response error.."""
        id = 1234
        self.mock_session.get.side_effect = aiohttp.ClientResponseError(None, None)

        with self.assertRaises(pyavanza.AvanzaResponseError):
            await pyavanza.get_fund_async(self.mock_session, id)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_FUND_URL.format(id=id), raise_for_status=True
        )

    @common.sync
    async def test_get_fund_parse_error(self):
        """Test that triggers a parse error."""
        id = 1234
        mock_resp = Mock()
        mock_resp.json = make_mocked_coro()
        mock_resp.json.side_effect = json.JSONDecodeError(None, "", 0)
        self.mock_session.get = make_mocked_coro(return_value=mock_resp)

        with self.assertRaises(pyavanza.AvanzaParseError):
            await pyavanza.get_fund_async(self.mock_session, id)

    @common.sync
    async def test_get_fund_success(self):
        """Test a successful request and response."""
        id = 1234
        data = copy.deepcopy(common.JSON_FUND_DATA)
        data["id"] = id
        mock_resp = Mock()
        mock_resp.json = make_mocked_coro(return_value=data)
        self.mock_session.get = make_mocked_coro(return_value=mock_resp)

        fund = await pyavanza.get_fund_async(self.mock_session, id)
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
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_FUND_URL.format(id=id), raise_for_status=True
        )
