"""Test certificate async."""
import copy
import json
from unittest.mock import Mock

import aiohttp
from aiohttp.test_utils import make_mocked_coro

import pyavanza
import tests.common as common


class TestCertificateAsync(common.TestCase):
    """Tests that retrieve certificate information asynchronously."""

    def setUp(self):
        """Set up, runs before each test."""
        self.mock_session = Mock()
        mock_get = make_mocked_coro()
        self.mock_session.get = mock_get

    @common.sync
    async def test_get_certificate_fail_request_error(self):
        """Test that triggers a request error."""
        id = 1234
        self.mock_session.get.side_effect = aiohttp.ClientConnectionError(None)

        with self.assertRaises(pyavanza.AvanzaRequestError):
            await pyavanza.get_certificate_async(self.mock_session, id)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_CERTIFICATE_URL.format(id=id), raise_for_status=True
        )

    @common.sync
    async def test_get_certificate_fail_response_error(self):
        """Test that triggers a response error.."""
        id = 1234
        self.mock_session.get.side_effect = aiohttp.ClientResponseError(None, None)

        with self.assertRaises(pyavanza.AvanzaResponseError):
            await pyavanza.get_certificate_async(self.mock_session, id)
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_CERTIFICATE_URL.format(id=id), raise_for_status=True
        )

    @common.sync
    async def test_get_certificate_parse_error(self):
        """Test that triggers a parse error."""
        id = 1234
        mock_resp = Mock()
        mock_resp.json = make_mocked_coro()
        mock_resp.json.side_effect = json.JSONDecodeError(None, "", 0)
        self.mock_session.get = make_mocked_coro(return_value=mock_resp)

        with self.assertRaises(pyavanza.AvanzaParseError):
            await pyavanza.get_certificate_async(self.mock_session, id)

    @common.sync
    async def test_get_certificate_success(self):
        """Test a successful request and response."""
        id = 1234
        data = copy.deepcopy(common.JSON_CERTIFICATE_DATA)
        data["id"] = id
        mock_resp = Mock()
        mock_resp.json = make_mocked_coro(return_value=data)
        self.mock_session.get = make_mocked_coro(return_value=mock_resp)

        certificate = await pyavanza.get_certificate_async(self.mock_session, id)
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
        self.mock_session.get.assert_called_once_with(
            pyavanza.AVANZA_API_CERTIFICATE_URL.format(id=id), raise_for_status=True
        )
